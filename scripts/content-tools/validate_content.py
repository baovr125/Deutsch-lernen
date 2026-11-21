"""Validate content/<level> against content/_schemas + cross-reference checks.

Usage: python -I validate_content.py <repo_root> <level>
Exit code 0 = no errors (warnings allowed).
"""
import csv
import json
import pathlib
import re
import sys
from collections import Counter, defaultdict

import yaml
from jsonschema import Draft202012Validator
from referencing import Registry, Resource

sys.stdout.reconfigure(encoding="utf-8")
root = pathlib.Path(sys.argv[1])
level = sys.argv[2].lower()
content = root / "content"
lvl = content / level
errors: list[str] = []
warnings: list[str] = []


def err(where, msg):
    errors.append(f"[ERROR] {where}: {msg}")


def warn(where, msg):
    warnings.append(f"[WARN]  {where}: {msg}")


# ---------- schemas ----------
schemas = {}
resources = []
for p in sorted((content / "_schemas").glob("*.schema.json")):
    s = json.loads(p.read_text(encoding="utf-8"))
    schemas[p.name.replace(".schema.json", "")] = s
    resources.append((s["$id"], Resource.from_contents(s)))
registry = Registry().with_resources(resources)
validators = {k: Draft202012Validator(v, registry=registry) for k, v in schemas.items()}


def load_yaml(p):
    try:
        return yaml.safe_load(p.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        err(p.relative_to(root), f"YAML không đọc được: {e}")
        return None


def check_schema(kind, data, where):
    for e in sorted(validators[kind].iter_errors(data), key=lambda e: list(e.path)):
        path = "/".join(str(x) for x in e.path)
        err(where, f"schema {kind} @ {path or '(root)'}: {e.message[:300]}")


# ---------- CEFR ----------
cefr_file = lvl / f"cefr-{level}.yaml"
cefr = load_yaml(cefr_file) or {}
check_schema("cefr", cefr, cefr_file.relative_to(root))
cefr_ids = {d["id"] for d in cefr.get("descriptors", [])}
cefr_used = Counter()

# ---------- vocabulary ----------
vocab = {}
vocab_rows_by_file = defaultdict(list)
for p in sorted((lvl / "vocabulary").glob("*.csv")):
    raw = p.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        err(p.relative_to(root), "file có BOM; cần UTF-8 không BOM")
    with p.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        expected = schemas["vocabulary-row"]["required"]
        if reader.fieldnames != expected:
            err(p.relative_to(root), f"header sai.\n  có:  {reader.fieldnames}\n  cần: {expected}")
        for n, row in enumerate(reader, start=2):
            where = f"{p.relative_to(root)}:{n}"
            if None in row:
                err(where, f"dòng thừa cột: {row[None]}")
                continue
            check_schema("vocabulary-row", row, where)
            vid = row.get("id", "")
            if vid in vocab:
                err(where, f"id trùng: {vid}")
            vocab[vid] = {**row, "_file": p.name, "_where": where}
            vocab_rows_by_file[p.name].append(vid)
            if row.get("level", "").lower() != level:
                err(where, f"level {row.get('level')} khác {level.upper()}")
            if row.get("pos") not in ("noun", "name") and row.get("article"):
                warn(where, f"không phải danh từ nhưng có article ({row['lemma']})")
            if row.get("pos") == "noun" and row["lemma"][:1].islower():
                err(where, f"danh từ phải viết hoa: {row['lemma']}")
            if row.get("pos") == "noun" and "pl-only" not in row.get("tags", "") and "sg-only" not in row.get("tags", "") and row.get("plural") == "—":
                warn(where, f"danh từ không có số nhiều nhưng thiếu tag sg-only/pl-only: {row['lemma']}")
            if not row.get("ipa", "").startswith("["):
                err(where, f"IPA phải đặt trong [ ]: {row.get('ipa')}")

# duplicate lemma detection (same lemma+article+pos)
lemma_key = Counter((v["lemma"], v["article"], v["pos"]) for v in vocab.values())
for k, c in lemma_key.items():
    if c > 1:
        err("vocabulary", f"từ bị lặp {c} lần: {k}")

# ---------- grammar topics ----------
grammar = {}
for p in sorted((lvl / "grammar").glob("*.yaml")):
    g = load_yaml(p)
    if g is None:
        continue
    where = p.relative_to(root)
    check_schema("grammar-topic", g, where)
    if p.stem != g.get("id"):
        err(where, f"tên file phải trùng id ({g.get('id')})")
    grammar[g.get("id")] = {"data": g, "where": where}

# ---------- units & lessons ----------
course = load_yaml(lvl / "course.yaml") or {}
check_schema("course", course, f"content/{level}/course.yaml")

units = {}
lessons = {}
all_exercise_ids = Counter()
type_counter = Counter()
skill_counter = Counter()

for udir in sorted((lvl / "units").iterdir()):
    if not udir.is_dir():
        continue
    uf = udir / "unit.yaml"
    if not uf.exists():
        warn(udir.relative_to(root), "chưa có unit.yaml (bỏ qua)")
        continue
    u = load_yaml(uf)
    if u is None:
        continue
    check_schema("unit", u, uf.relative_to(root))
    units[u["id"]] = {"data": u, "dir": udir}
    for lf in sorted(list(udir.glob("lesson-*.yaml")) + list(udir.glob("review.yaml"))):
        l = load_yaml(lf)
        if l is None:
            continue
        check_schema("lesson", l, lf.relative_to(root))
        lessons[l.get("id")] = {"data": l, "where": lf.relative_to(root), "unit": u}

# course path consistency
for step in course.get("path", []):
    if step.get("status") in ("ready", "draft") and step["kind"] in ("intro", "kapitel"):
        if step["id"] not in units:
            err("course.yaml", f"path {step['id']} có status {step['status']} nhưng không có unit.yaml")
        else:
            d = units[step["id"]]["dir"]
            if step.get("dir") != f"units/{d.name}":
                err("course.yaml", f"dir của {step['id']} phải là units/{d.name}")
for uid in units:
    if uid not in {s["id"] for s in course.get("path", [])}:
        err("course.yaml", f"unit {uid} không có trong path")

# lesson order map for vocab review checks
lesson_seq = []
for step in sorted(course.get("path", []), key=lambda s: s["order"]):
    if step["id"] in units:
        u = units[step["id"]]["data"]
        lesson_seq += u["lessons"] + ([u["review"]] if u.get("review") else [])
lesson_pos = {lid: i for i, lid in enumerate(lesson_seq)}

assigned_new = Counter()

for uid, uinfo in units.items():
    u = uinfo["data"]
    for c in u.get("cefr", []):
        if c not in cefr_ids:
            err(f"unit {uid}", f"mã CEFR không tồn tại: {c}")
    for gid in u.get("grammar_topics", []):
        if gid not in grammar:
            err(f"unit {uid}", f"grammar topic không tồn tại: {gid}")
    for lid in u["lessons"] + ([u["review"]] if u.get("review") else []):
        if lid not in lessons:
            err(f"unit {uid}", f"lesson {lid} được khai báo nhưng không có file")

for lid, info in lessons.items():
    l, where = info["data"], info["where"]
    u = info["unit"]
    if l.get("unit") != u["id"]:
        err(where, f"unit = {l.get('unit')} nhưng file nằm trong {u['id']}")
    if lid not in u["lessons"] and lid != u.get("review"):
        err(where, "lesson không được liệt kê trong unit.yaml")
    expected_file = "review.yaml" if l.get("kind") == "review" else f"lesson-{l.get('order', 0):02d}.yaml"
    if where.name != expected_file:
        err(where, f"tên file phải là {expected_file}")
    if l.get("level", "").lower() != level:
        err(where, "level sai")
    for c in l.get("cefr", []):
        cefr_used[c] += 1
        if c not in cefr_ids:
            err(where, f"mã CEFR không tồn tại: {c}")
    for pr in l.get("prerequisites", []):
        if pr not in lessons:
            err(where, f"prerequisite không tồn tại: {pr}")
        elif lesson_pos.get(pr, -1) >= lesson_pos.get(lid, 10**6):
            err(where, f"prerequisite {pr} không đứng trước bài này")

    # vocabulary
    voc = l.get("vocabulary", {})
    if voc.get("file") and not (lvl / voc["file"]).exists():
        err(where, f"file từ vựng không tồn tại: {voc['file']}")
    for vid in voc.get("new", []):
        assigned_new[vid] += 1
        if vid not in vocab:
            err(where, f"vocab new không tồn tại: {vid}")
        elif vocab[vid]["lesson"] != lid:
            err(where, f"vocab {vid} khai báo lesson={vocab[vid]['lesson']} nhưng được dạy mới ở {lid}")
    for vid in voc.get("review", []):
        if vid not in vocab:
            err(where, f"vocab review không tồn tại: {vid}")
        else:
            src = vocab[vid]["lesson"]
            if lesson_pos.get(src, 10**6) >= lesson_pos.get(lid, -1):
                err(where, f"vocab review {vid} chưa được dạy trước bài này (dạy ở {src})")

    # grammar
    for t in l.get("grammar", {}).get("topics", []):
        if t["topic"] not in grammar:
            err(where, f"grammar topic không tồn tại: {t['topic']}")

    # exercises
    objectives = {o["id"] for o in l.get("objectives", [])}
    tested = Counter()
    ex_ids = set()
    stimuli = {b["id"] for b in l.get("skills", {}).get("listening", [])} | {b["id"] for b in l.get("skills", {}).get("reading", [])}
    for ex in l.get("exercises", []):
        exw = f"{where} › {ex.get('id')}"
        ex_ids.add(ex.get("id"))
        all_exercise_ids[ex.get("id")] += 1
        type_counter[ex.get("type")] += 1
        skill_counter[ex.get("skill")] += 1
        if not str(ex.get("id", "")).startswith(lid + "-"):
            err(exw, f"id bài tập phải bắt đầu bằng '{lid}-'")
        for o in ex.get("objectives", []):
            tested[o] += 1
            if o not in objectives:
                err(exw, f"objective {o} không có trong lesson")
        if ex.get("stimulus") and ex["stimulus"] not in stimuli:
            err(exw, f"stimulus {ex['stimulus']} không phải block listening/reading của bài")
        if ex.get("skill") in ("listening",) and not ex.get("stimulus") and ex.get("type") != "dictation":
            warn(exw, "bài nghe nên có stimulus")
        item_ids = Counter(it.get("id") for it in ex.get("items", []))
        for iid, c in item_ids.items():
            if c > 1:
                err(exw, f"item id trùng: {iid}")
        for it in ex.get("items", []):
            iw = f"{exw}/{it.get('id')}"
            t = ex.get("type")
            if t == "multiple-choice":
                opts = it.get("options", [])
                if it.get("answer") not in opts:
                    err(iw, f"đáp án '{it.get('answer')}' không nằm trong options")
                if len(set(opts)) != len(opts):
                    err(iw, "options bị trùng")
            elif t == "gap-fill":
                n = it.get("prompt", "").count("___")
                ans = it.get("answer", [])
                if n != len(ans):
                    err(iw, f"số chỗ trống ___ ({n}) khác số đáp án ({len(ans)})")
                acc = it.get("accept")
                if acc is not None and (not isinstance(acc, list) or any(not isinstance(a, list) or len(a) != n for a in acc)):
                    err(iw, "accept của gap-fill phải là danh sách các phương án, mỗi phương án đủ số chỗ trống")
            elif t == "ordering":
                toks = it.get("tokens", [])
                ans = re.sub(r"[.?!]$", "", it.get("answer", "")).replace(",", " ,").split()
                if sorted(toks) != sorted(ans):
                    err(iw, f"tokens không khớp đáp án.\n    tokens: {sorted(toks)}\n    answer: {sorted(ans)}")
                if toks == ans:
                    warn(iw, "tokens đang đúng sẵn thứ tự — cần xáo trộn")
            elif t == "matching":
                lefts = [p["left"] for p in it.get("pairs", [])]
                rights = [p["right"] for p in it.get("pairs", [])]
                if len(set(lefts)) != len(lefts) or len(set(rights)) != len(rights):
                    err(iw, "matching có vế trùng nhau → đáp án không duy nhất")
            elif t in ("translation", "sentence-building"):
                acc = it.get("accept")
                if acc is not None and not all(isinstance(a, str) for a in acc):
                    err(iw, "accept phải là danh sách chuỗi")
    for o in objectives:
        if tested[o] == 0:
            err(where, f"objective {o} chưa có bài tập nào kiểm tra")
    for kind in ("listening", "reading", "speaking", "writing"):
        for b in l.get("skills", {}).get(kind, []):
            for e in b.get("exercises", []):
                if e not in ex_ids:
                    err(where, f"skills.{kind}.{b['id']} tham chiếu bài tập không tồn tại: {e}")
    types = {ex.get("type") for ex in l.get("exercises", [])}
    if l.get("kind") == "lesson" and len(types) < 5:
        warn(where, f"ít dạng bài tập ({len(types)}): {sorted(types)}")

for gid, info in grammar.items():
    g, where = info["data"], info["where"]
    if g.get("introduced_in") not in lessons:
        err(where, f"introduced_in không tồn tại: {g.get('introduced_in')}")
    nrules = len(g.get("rules", []))
    for ex in g.get("exercises", []):
        all_exercise_ids[ex.get("id")] += 1
        type_counter[ex.get("type")] += 1
        if not str(ex.get("id", "")).startswith(gid + "-"):
            err(f"{where} › {ex.get('id')}", f"id bài tập phải bắt đầu bằng '{gid}-'")
        for o in ex.get("objectives", []):
            m = re.fullmatch(r"r([0-9]+)", o)
            if not m or not (1 <= int(m.group(1)) <= nrules):
                err(f"{where} › {ex.get('id')}", f"objective {o} phải là r1..r{nrules} (tham chiếu rules)")
        for it in ex.get("items", []):
            if ex.get("type") == "multiple-choice" and it.get("answer") not in it.get("options", []):
                err(f"{where} › {ex.get('id')}/{it.get('id')}", "đáp án không nằm trong options")
            if ex.get("type") == "gap-fill" and it.get("prompt", "").count("___") != len(it.get("answer", [])):
                err(f"{where} › {ex.get('id')}/{it.get('id')}", "số ___ khác số đáp án")
            if ex.get("type") == "ordering":
                ans = re.sub(r"[.?!]$", "", it.get("answer", "")).replace(",", " ,").split()
                if sorted(it.get("tokens", [])) != sorted(ans):
                    err(f"{where} › {ex.get('id')}/{it.get('id')}", "tokens không khớp đáp án")
    used = any(t["topic"] == gid for l in lessons.values() for t in l["data"].get("grammar", {}).get("topics", []))
    if not used:
        warn(where, "chủ điểm chưa được bài học nào tham chiếu")

for eid, c in all_exercise_ids.items():
    if c > 1:
        err("exercises", f"id bài tập trùng: {eid}")

for vid, v in vocab.items():
    if assigned_new[vid] == 0:
        err(v["_where"], f"từ {vid} ({v['lemma']}) chưa được bài nào dạy (vocabulary.new)")
    if assigned_new[vid] > 1:
        err(v["_where"], f"từ {vid} được dạy mới ở {assigned_new[vid]} bài")

# ---------- report ----------
print("=" * 70)
print(f"Units: {len(units)} | Lessons: {sum(1 for l in lessons.values() if l['data'].get('kind') == 'lesson')} "
      f"| Reviews: {sum(1 for l in lessons.values() if l['data'].get('kind') == 'review')} "
      f"| Grammar topics: {len(grammar)} | Vocabulary: {len(vocab)}")
n_items = sum(len(ex.get("items", [])) for l in lessons.values() for ex in l["data"].get("exercises", [])) + \
    sum(len(ex.get("items", [])) for g in grammar.values() for ex in g["data"].get("exercises", []))
print(f"Exercises: {sum(all_exercise_ids.values())} | Items: {n_items}")
print("Theo dạng:", dict(sorted(type_counter.items())))
print("Theo kỹ năng (lesson):", dict(sorted(skill_counter.items())))
print("CEFR đã dùng:", dict(sorted(cefr_used.items())))
print("CEFR chưa dùng:", sorted(cefr_ids - set(cefr_used)))
for f, ids in vocab_rows_by_file.items():
    pos = Counter(vocab[i]["pos"] for i in ids)
    src = Counter(vocab[i]["source"] for i in ids)
    print(f"  {f}: {len(ids)} từ | pos={dict(pos)} | source={dict(src)}")
print("=" * 70)
for w in warnings:
    print(w)
for e in errors:
    print(e)
print(f"\n{len(errors)} lỗi, {len(warnings)} cảnh báo")
sys.exit(1 if errors else 0)
