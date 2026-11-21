"""Trích toàn bộ chuỗi tiếng Đức từ content/<level> (Content Standard v2) để soát lỗi.

Usage: python -I extract_de.py <level_dir> <out_file>
Ví dụ: python -I extract_de.py content/a1 de.txt
Mỗi dòng: <tệp>  <đường dẫn trường>  <nội dung>
"""
import pathlib
import sys

import yaml

sys.stdout.reconfigure(encoding="utf-8")
lvl = pathlib.Path(sys.argv[1])
out_file = pathlib.Path(sys.argv[2])
# Trường chứa văn bản tiếng Đức (list hoặc chuỗi)
DE_KEYS = {"de", "title_de", "source", "tts", "answer", "answers", "model_answer", "pattern", "wrong", "right", "prompt", "text_de",
           "left", "right", "tokens", "word_bank", "required_words", "plural"}
SKIP_FILES = {"cefr-a1.yaml", "course.yaml"}
lines = []


def walk(node, path, fname):
    if isinstance(node, dict):
        for k, v in node.items():
            if k in DE_KEYS and k in ("tokens", "answers", "word_bank", "required_words") and isinstance(v, list):
                lines.append(f"{fname}\t{path}/{k}\t{' | '.join(str(x) for x in v)}")
            elif k in DE_KEYS and isinstance(v, str):
                lines.append(f"{fname}\t{path}/{k}\t{v}")
            else:
                walk(v, f"{path}/{k}", fname)
    elif isinstance(node, list):
        for i, x in enumerate(node):
            walk(x, f"{path}[{i}]", fname)


files = sorted(lvl.glob("modules/*/**/*.yaml")) + sorted(lvl.glob("grammar/*.yaml"))
for f in files:
    if f.name in SKIP_FILES:
        continue
    walk(yaml.safe_load(f.read_text(encoding="utf-8")), "", str(f.relative_to(lvl)))
out_file.write_text("\n".join(lines), encoding="utf-8")
print(f"{len(lines)} dòng từ {len(files)} tệp -> {out_file}")
