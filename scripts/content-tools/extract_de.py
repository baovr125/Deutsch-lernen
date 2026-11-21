"""Extract all German strings from content/<level> YAML + CSV for proofreading.
Usage: python -I extract_de.py <level_dir> <out_file>"""
import csv
import pathlib
import sys

import yaml

sys.stdout.reconfigure(encoding="utf-8")
lvl = pathlib.Path(sys.argv[1])
out = []
DE_KEYS = {"de", "text_de", "model_de", "example_de", "answer", "model_answer", "prompt", "tts", "pattern"}


def walk(node, path, src):
    if isinstance(node, dict):
        typ = node.get("type")
        for k, v in node.items():
            if k in DE_KEYS and isinstance(v, str):
                out.append(f"{src}|{path}.{k}|{v.strip()}")
            elif k == "answer" and isinstance(v, list):
                out.append(f"{src}|{path}.answer|{' / '.join(map(str, v))}")
            elif k == "accept" and isinstance(v, list):
                out.append(f"{src}|{path}.accept|{v}")
            elif k == "options" and isinstance(v, list):
                out.append(f"{src}|{path}.options|{' | '.join(v)}")
            else:
                walk(v, f"{path}.{k}", src)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            walk(v, f"{path}[{i}]", src)


for p in sorted(lvl.rglob("*.yaml")):
    walk(yaml.safe_load(p.read_text(encoding="utf-8")), "", p.relative_to(lvl))
for p in sorted((lvl / "vocabulary").glob("*.csv")):
    for r in csv.DictReader(p.open(encoding="utf-8")):
        out.append(f"{p.name}|{r['id']}|{r['article']} {r['lemma']} ({r['plural']}) [{r['forms']}] :: {r['example_de']}")
pathlib.Path(sys.argv[2]).write_text("\n".join(out), encoding="utf-8")
print(len(out), "dòng")
