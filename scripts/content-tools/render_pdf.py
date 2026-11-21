"""Render PDF pages to PNG. Usage: python -I render_pdf.py <pdf> <out_dir> <zoom> [first-last]"""
import sys
import pathlib
import pymupdf

pdf_path, out_dir, zoom = sys.argv[1], pathlib.Path(sys.argv[2]), float(sys.argv[3])
out_dir.mkdir(parents=True, exist_ok=True)
doc = pymupdf.open(pdf_path)
first, last = 1, doc.page_count
if len(sys.argv) > 4:
    a, b = sys.argv[4].split("-")
    first, last = int(a), int(b)
print(f"pages={doc.page_count}")
for i in range(first - 1, min(last, doc.page_count)):
    page = doc[i]
    pix = page.get_pixmap(matrix=pymupdf.Matrix(zoom, zoom))
    out = out_dir / f"p{i + 1:02d}.png"
    pix.save(out)
    print(out.name, pix.width, "x", pix.height)
