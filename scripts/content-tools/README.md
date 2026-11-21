# content-tools (tạm thời)

Công cụ Python dùng khi biên soạn nội dung `content/`. Tạm thời viết bằng Python vì tooling TypeScript của dự án chưa được khởi tạo; sẽ thay bằng `scripts/content-validate` (TS) sau.

Yêu cầu: Python 3.11+, `pyyaml`, `jsonschema` (+ `referencing`), `pymupdf` (chỉ cho render_pdf). Chạy với `python -I`.

| Script | Dùng để | Lệnh |
|---|---|---|
| `validate_content.py` | Kiểm tra schema + liên kết chéo của một cấp độ | `python -I scripts/content-tools/validate_content.py . a1` |
| `extract_de.py` | Trích toàn bộ câu tiếng Đức để soát lỗi | `python -I scripts/content-tools/extract_de.py content/a1 /tmp/de.txt` |
| `render_pdf.py` | Chuyển trang PDF (dạng ảnh scan) thành PNG để đọc | `python -I scripts/content-tools/render_pdf.py file.pdf out_dir 1.5 17-22` |
| `fix_quotes.py` | Đổi ngoặc kép kiểu CSV `""x""` trong YAML thành “x” | `python -I scripts/content-tools/fix_quotes.py file.yaml` |

Lưu ý: file PDF tài liệu của Klett **không** được lưu trong repo (bản quyền) – tải lại theo đường dẫn trong `docs/curriculum/a1/handoff.md`.
