"""Replace CSV-style doubled quotes ""x"" inside YAML files with typographic “x”.
Usage: python -I fix_quotes.py <file> [<file> ...]"""
import re
import sys
import pathlib

sys.stdout.reconfigure(encoding="utf-8")
for f in sys.argv[1:]:
    p = pathlib.Path(f)
    s = p.read_text(encoding="utf-8")
    new, n = re.subn(r'""([^"\n]*?)""', r"“\1”", s)
    if n:
        p.write_text(new, encoding="utf-8", newline="\n")
    print(f"{p.name}: {n} thay thế")
