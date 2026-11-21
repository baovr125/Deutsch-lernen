"""Validator cho Content Standard v2.

Usage: python -I validate_content_v2.py <repo_root> [module_dir ...]
  Không truyền module_dir → quét mọi content/<level>/modules/*/module.yaml.
Exit code 0 = không có lỗi (cảnh báo được phép).
Quy tắc: docs/content/content-validation-rules.md
"""
import json
import pathlib
import re
import sys
from collections import Counter

import yaml
from jsonschema import Draft202012Validator

sys.stdout.reconfigure(encoding="utf-8")
root = pathlib.Path(sys.argv[1])
schema = json.loads((root / "content/_schemas/v2/content.schema.json").read_text(encoding="utf-8"))
validator = Draft202012Validator(schema)
errors, warnings = [], []
stats = Counter()
LEVEL = r"(a1|a2|b1|b2|c1|c2)"


def err(w, m):
    errors.append(f"[ERROR] {w}: {m}")


def warn(w, m):
    warnings.append(f"[WARN]  {w}: {m}")


_cache = {}


def load(path):
    if path in _cache:
        return _cache[path]
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        err(path.name, f"YAML không hợp lệ: {e}")
        _cache[path] = None
        return None
    for e in sorted(validator.iter_errors(data), key=lambda x: list(x.absolute_path)):
        loc = "/".join(str(p) for p in e.absolute_path)
        err(f"{path.name}:{loc}", e.message[:200])
    _cache[path] = data
    return data


SENT_END = re.compile(r"[.!?…]$|[.!?]['\"“”„]$")


def check_de_sentence(where, s, allow_fragment=False):
    s = s.strip()
    if not s or allow_fragment or len(s.split()) < 4:
        return  # cụm từ ngắn (< 4 từ) được coi là mảnh câu
    words = s.split()
    if all(w[0].isupper() for w in words if w[0].isalpha()):
        return  # danh sách danh từ (thứ, tháng…)
    if s[0].islower() and not SENT_END.search(s):
        return  # danh sách từ viết thường (lộ trình, thứ tự…)
    if not SENT_END.search(s):
        warn(where, f"câu Đức không kết thúc bằng dấu câu: {s[:50]}")
    if s[0].isalpha() and s[0].islower():
        warn(where, f"câu Đức không viết hoa đầu câu: {s[:50]}")


def walk_ids(node, bucket, where):
    """Thu mọi trường 'id' kiểu a1.xxx để kiểm tra trùng lặp."""
    if isinstance(node, dict):
        v = node.get("id")
        if isinstance(v, str) and re.match(rf"^{LEVEL}\.", v):
            bucket.append((v, where))
        for x in node.values():
            walk_ids(x, bucket, where)
    elif isinstance(node, list):
        for x in node:
            walk_ids(x, bucket, where)


def norm_tokens(tokens):
    out = [x.strip(".,!?;:") for x in tokens]
    return [x for x in out if x]


def check_exercise(ex, where, obj_ids, covered, block_ids=None):
    for r in ex.get("objective_refs", []):
        if r not in obj_ids:
            err(where, f"objective_ref không tồn tại: {r}")
        covered.add(r)
    ref = (ex.get("stimulus") or {}).get("ref")
    if ref and block_ids is not None and ref not in block_ids:
        err(where, f"stimulus.ref không trỏ tới khối nào của bài học: {ref}")
    t = ex.get("type")
    stats["exercises"] += 1
    stats[f"type:{t}"] += 1
    items = ex.get("items", [])
    stats["items"] += len(items)
    open_no_rubric = False
    for it in items:
        w = f"{where}/{it.get('id')}"
        if t in ("multiple-choice", "reading-comprehension", "listening-practice"):
            opt = [o["id"] for o in it.get("options", [])]
            if len(set(opt)) != len(opt):
                err(w, "option id trùng")
            for a in it.get("answer", []):
                if a not in opt:
                    err(w, f"đáp án {a} không nằm trong options")
            texts = [o["text"] for o in it.get("options", [])]
            if len(set(texts)) != len(texts):
                err(w, "hai lựa chọn có nội dung giống hệt")
        elif t == "fill-blank":
            blanks = it["prompt"].count("___")
            if blanks != len(it["answers"]):
                err(w, f"số chỗ trống ___ ({blanks}) ≠ số đáp án ({len(it['answers'])})")
            for alt in it.get("accept", []):
                if len(alt) != blanks:
                    err(w, "một tổ hợp accept có số phần tử ≠ số chỗ trống")
        elif t == "word-order":
            if sorted(norm_tokens(it["tokens"])) != sorted(norm_tokens(it["answer"].split())):
                err(w, "tokens không khớp đúng với đáp án (so sánh đa tập hợp, bỏ dấu câu ở đầu/cuối)")
            if it["tokens"] == it["answer"].split():
                warn(w, "thứ tự tokens đã trùng đáp án – nên xáo trộn")
            check_de_sentence(w, it["answer"])
        elif t == "translation":
            if it["direction"] == "vi-de":
                for a in it["answers"]:
                    check_de_sentence(w, a)
            else:
                check_de_sentence(w, it["source"], allow_fragment=True)
        elif t == "sentence-construction":
            for a in it["answers"]:
                check_de_sentence(w, a)
                for rw in it.get("required_words", []):
                    if rw.lower() not in a.lower():
                        err(w, f"đáp án mẫu thiếu từ bắt buộc: {rw}")
        elif t == "dictation":
            pass  # chính tả có thể là danh sách từ, không kiểm tra dấu câu
        elif t in ("writing-practice", "speaking-practice"):
            if not it.get("rubric_vi") and not ex.get("rubric"):
                open_no_rubric = True
    if open_no_rubric:
        warn(where, "bài viết/nói không có rubric")
    if t == "matching":
        flat = [i["right"] for i in items if "right" in i]
        if len(set(flat)) != len(flat):
            err(where, "matching có vế phải trùng nhau")
        for i in items:
            if "pairs" in i:
                rights = [x["right"] for x in i["pairs"]]
                if len(set(rights)) != len(rights):
                    err(f"{where}/{i['id']}", "matching có vế phải trùng nhau")
    if t in ("multiple-choice", "reading-comprehension", "listening-practice"):
        pos = Counter(i["answer"][0] for i in items if len(i.get("answer", [])) == 1)
        if len(items) >= 4 and len(pos) == 1:
            warn(where, "mọi đáp án đúng cùng một vị trí")
    if t == "listening-practice":
        stats["listening"] += 1


# ---- đăng ký toàn cục (tham chiếu chéo module) ----
mod_files = sorted((root / "content").glob("*/modules/*/module.yaml"))
if len(sys.argv) > 2:
    dirs = [root / p for p in sys.argv[2:]]
else:
    dirs = [p.parent for p in mod_files]

global_vocab, global_grammar = set(), {}
for mf in mod_files:
    m = load(mf)
    if not m or m.get("content_type") != "module":
        continue
    vd = load(mf.parent / m["vocabulary"]["file"]) if m.get("vocabulary") else None
    for e in (vd or {}).get("entries", []):
        global_vocab.add(e["id"])
for gf in sorted((root / "content").glob("*/grammar/*.yaml")):
    head = gf.read_text(encoding="utf-8")[:200]
    if "schema_version" not in head:
        continue  # tệp định dạng cũ (v1) – không thuộc chuẩn v2
    g = load(gf)
    if isinstance(g, dict) and g.get("content_type") == "grammar-topic":
        global_grammar[g["id"]] = g


def check_sections(asx, mid):
    """Các phần (sections) của bài đánh giá: tham chiếu đúng và mỗi bài tập thuộc đúng một phần."""
    if not asx or not asx.get("sections"):
        return
    ids = {e["id"] for e in asx["exercises"]}
    seen = Counter()
    for sec in asx["sections"]:
        for r in sec["exercise_refs"]:
            if r not in ids:
                err(asx["id"], f"section {sec['id']}: exercise_ref không tồn tại: {r}")
            seen[r] += 1
    for i in ids:
        if seen[i] != 1:
            err(asx["id"], f"bài tập {i} thuộc {seen[i]} phần (phải đúng 1)")
    stats["assessment_sections"] += len(asx["sections"])


def validate_module(mdir):
    mod = load(mdir / "module.yaml")
    if not mod or mod.get("content_type") != "module":
        return
    mid = mod["id"]
    stats["modules"] += 1
    ids = []
    walk_ids({k: v for k, v in mod.items() if k in ("id", "objectives")}, ids, "module.yaml")

    def need(ref):
        p = mdir / ref["file"]
        if not p.exists():
            err("module.yaml", f"file không tồn tại: {ref['file']}")
            return None
        d = load(p)
        if d is not None:
            walk_ids(d, ids, ref["file"])
            if d.get("id") != ref["id"]:
                err(ref["file"], f"id {d.get('id')} ≠ id khai báo trong module ({ref['id']})")
            if d.get("module") not in (None, mid):
                err(ref["file"], f"module {d.get('module')} ≠ {mid}")
        return d

    lessons = {r["id"]: need(r) for r in mod.get("lessons", [])}
    grammars = {r["id"]: need(r) for r in mod.get("grammar", [])}
    vocab = need(mod["vocabulary"]) if mod.get("vocabulary") else None
    expr = need(mod["expressions"]) if mod.get("expressions") else None
    assess_refs = ([mod["assessment"]] if mod.get("assessment") else []) + mod.get("assessments", [])
    assess_list = [need(r) for r in assess_refs]
    exsets = {r["id"]: need(r) for r in mod.get("exercises", [])}

    vocab_ids = {e["id"] for e in (vocab or {}).get("entries", [])}
    expr_ids = {e["id"] for e in (expr or {}).get("entries", [])}
    lesson_ids = set(lessons)
    ex_ids = set()
    obj_ids = {o["id"] for o in mod.get("objectives", [])}
    for d in list(lessons.values()) + list(grammars.values()):
        for o in (d or {}).get("objectives", []):
            obj_ids.add(o["id"])
    for g in grammars.values():
        for r in (g or {}).get("rules", []):
            obj_ids.add(r["id"])  # bài tập ngữ pháp có thể trỏ tới quy tắc
        for e in (g or {}).get("exercises", []):
            ex_ids.add(e["id"])
    for d in exsets.values():
        for e in (d or {}).get("exercises", []):
            ex_ids.add(e["id"])
    for asx in assess_list:
        for e in (asx or {}).get("exercises", []):
            ex_ids.add(e["id"])

    c = Counter(i for i, _ in ids)
    for i, n in c.items():
        if n > 1:
            err(mid, f"ID trùng ({n} lần): {i} tại {[w for x, w in ids if x == i]}")
        shared = re.match(rf"^{LEVEL}\.g\.", i)
        if not (i == mid or i.startswith(mid + ".") or shared):
            err(mid, f"ID không có tiền tố module {mid}: {i}")
    stats["ids"] += len(c)

    seen = set()
    for e in (vocab or {}).get("entries", []):
        w = e["id"]
        stats["vocab"] += 1
        key = (e["de"], e["pos"])
        if key in seen:
            warn(w, f"lemma lặp: {e['de']}")
        seen.add(key)
        if e["pos"] == "noun" and not e["de"][0].isupper():
            err(w, "danh từ phải viết hoa")
        if not e.get("usage_vi"):
            stats["vocab_missing_usage"] += 1
        for r in e["lesson_refs"]:
            if r not in lesson_ids:
                err(w, f"lesson_ref không tồn tại: {r}")
    for e in (expr or {}).get("entries", []):
        stats["expressions"] += 1
        check_de_sentence(e["id"], e["de"], allow_fragment=True)
        for r in e["lesson_refs"]:
            if r not in lesson_ids:
                err(e["id"], f"lesson_ref không tồn tại: {r}")

    covered = set()
    for sid, d in exsets.items():
        if not d:
            continue
        if d["lesson"] not in lesson_ids:
            err(sid, f"lesson không tồn tại: {d['lesson']}")
            blocks = None
        else:
            blocks = {b["id"] for b in (lessons[d["lesson"]] or {}).get("blocks", [])}
        for ex in d["exercises"]:
            check_exercise(ex, ex["id"], obj_ids, covered, blocks)
    for asx in assess_list:
        for ex in (asx or {}).get("exercises", []):
            check_exercise(ex, ex["id"], obj_ids, covered)
            stats["assessment_exercises"] += 1
        check_sections(asx, mid)
    for gid, g in grammars.items():
        if g and g["introduced_in"] == mid:
            for ex in g.get("exercises", []):
                check_exercise(ex, ex["id"], obj_ids, covered)
                stats["grammar_exercises"] += 1
    for asx in assess_list:
        if not asx:
            continue
        for sk in ("listening", "speaking", "reading", "writing"):
            if not any(e["skill"] == sk for e in asx["exercises"]):
                warn(asx["id"], f"bài đánh giá không có kỹ năng {sk}")

    for lid, l in lessons.items():
        if not l:
            continue
        stats["lessons"] += 1
        for r in l["vocabulary_refs"]:
            if r not in vocab_ids:
                err(lid, f"vocabulary_ref không tồn tại trong module: {r}")
        for r in l.get("review_vocabulary_refs", []):
            if r not in global_vocab:
                err(lid, f"review_vocabulary_ref không tồn tại: {r}")
        for r in l["grammar_refs"]:
            if r not in global_grammar:
                err(lid, f"grammar_ref không tồn tại: {r}")
        for r in l["expression_refs"]:
            if r not in expr_ids:
                err(lid, f"expression_ref không tồn tại: {r}")
        r = l.get("exercise_set_ref")
        if r and r not in exsets:
            err(lid, f"exercise_set_ref không tồn tại: {r}")
        for pre in l.get("prerequisites", []):
            pass
        for b in l["blocks"]:
            for ln in b.get("lines", []):
                check_de_sentence(b["id"], ln["de"], allow_fragment=True)
            prev = ""
            for p in b.get("paragraphs", []):
                t = p["de"].strip()
                frag = t.endswith(",") or t.startswith(("Viele Grüße", "Mit freundlichen")) or prev.endswith(",")
                check_de_sentence(b["id"], t, allow_fragment=frag or len(b["paragraphs"]) == 1)
                prev = t
        ex_obj = set()
        for d in [exsets.get(r)] if r else []:
            for ex in (d or {}).get("exercises", []):
                ex_obj.update(ex["objective_refs"])
        for o in l["objectives"]:
            if o["id"] not in ex_obj:
                err(lid, f"mục tiêu chưa có bài tập kiểm tra: {o['id']}")
        if not l["vocabulary_refs"] and l.get("kind") != "review" and mod.get("kind") != "plattform":
            warn(lid, "bài không gắn từ vựng nào")
    for e in (vocab or {}).get("entries", []):
        for lr in e["lesson_refs"]:
            if lr in lessons and lessons[lr] and e["id"] not in lessons[lr]["vocabulary_refs"]:
                err(e["id"], f"lesson_refs có {lr} nhưng bài đó không liệt kê từ này")
    vindex = {x["id"]: x for x in (vocab or {}).get("entries", [])}
    for lid, l in lessons.items():
        for vr in (l or {}).get("vocabulary_refs", []):
            ent = vindex.get(vr)
            if ent and lid not in ent["lesson_refs"]:
                err(lid, f"vocabulary_refs có {vr} nhưng từ đó không ghi bài này trong lesson_refs")
    used_vocab = set()
    for l in lessons.values():
        used_vocab.update((l or {}).get("vocabulary_refs", []))
    for v in vocab_ids - used_vocab:
        warn(v, "từ vựng không được bài học nào tham chiếu")

    for gid, g in grammars.items():
        if not g:
            continue
        if g["introduced_in"] != mid:
            continue  # kiểm tra ở module giới thiệu
        stats["grammar"] += 1
        for r in g.get("exercise_refs", []):
            if r not in ex_ids:
                err(gid, f"exercise_ref không tồn tại: {r}")
        for pair in g["examples"]:
            check_de_sentence(gid, pair["de"], allow_fragment=True)
        for o in g["objectives"]:
            if o["id"] not in covered:
                err(gid, f"mục tiêu ngữ pháp chưa có bài tập: {o['id']}")
    for o in mod.get("objectives", []):
        if o["id"] not in covered:
            err(mid, f"mục tiêu module chưa được bài tập/đánh giá nào kiểm tra: {o['id']}")


for d in dirs:
    validate_module(d)

# ngữ pháp mồ côi + tham chiếu giữa các tệp
referenced = set()
for mf in mod_files:
    m = load(mf)
    for r in (m or {}).get("grammar", []):
        referenced.add(r["id"])
for gid in global_grammar:
    if gid not in referenced:
        warn(gid, "chủ điểm ngữ pháp không được module nào khai báo")

# course.yaml + cefr-<level>.yaml: kiểm tra schema; mọi bước có trường module phải trỏ tới thư mục module thật
course_validator = Draft202012Validator(json.loads((root / "content/_schemas/v2/course.schema.json").read_text(encoding="utf-8")))
cefr_validator = Draft202012Validator(json.loads((root / "content/_schemas/v2/cefr.schema.json").read_text(encoding="utf-8")))
for cef in sorted((root / "content").glob("*/cefr-*.yaml")):
    for e in cefr_validator.iter_errors(yaml.safe_load(cef.read_text(encoding="utf-8"))):
        err(cef.name, e.message[:200])
for cf in sorted((root / "content").glob("*/course.yaml")):
    course = yaml.safe_load(cf.read_text(encoding="utf-8"))
    for e in course_validator.iter_errors(course):
        err(f"{cf.parent.name}/course.yaml:" + "/".join(str(p) for p in e.absolute_path), e.message[:200])
    registered = {s["module"].split("/", 1)[1] for s in course.get("path", []) if "module" in s}
    for md in sorted((cf.parent / "modules").glob("*/module.yaml")):
        if md.parent.name not in registered:
            warn(f"{cf.parent.name}/course.yaml", f"module {md.parent.name} chưa được đăng ký trong path")
    for step in course.get("path", []):
        if "module" in step:
            md = cf.parent / step["module"]
            if not (md / "module.yaml").exists():
                err(f"{cf.parent.name}/course.yaml", f"{step['id']}: không có {step['module']}/module.yaml")
            else:
                stats["course_modules_registered"] += 1
        elif step.get("status") in ("ready", "draft"):
            err(f"{cf.parent.name}/course.yaml", f"{step['id']}: status {step['status']} nhưng chưa có trường module")

if stats["vocab_missing_usage"]:
    warn("vocabulary", f"{stats['vocab_missing_usage']} từ vựng chưa có usage_vi (khuyến nghị bổ sung)")
for line in errors + warnings:
    print(line)
print("\n=== TỔNG KẾT ===")
for k, v in sorted(stats.items()):
    print(f"  {k}: {v}")
print(f"  errors={len(errors)} warnings={len(warnings)}")
sys.exit(1 if errors else 0)
