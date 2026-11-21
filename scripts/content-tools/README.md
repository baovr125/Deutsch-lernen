# content-tools (tạm thời)

Công cụ Python dùng khi biên soạn nội dung `content/` theo **Content Standard v2** ([docs/content/content-standard.md](../../docs/content/content-standard.md)). Tạm thời viết bằng Python vì tooling TypeScript của dự án chưa được khởi tạo; sẽ thay bằng `scripts/content-validate` (TS) sau.

Yêu cầu: Python 3.11+, `pyyaml`, `jsonschema`, `pymupdf` (chỉ cho render_pdf). Chạy với `python -I`.

| Script | Dùng để | Lệnh |
|---|---|---|
| `validate_content_v2.py` | Kiểm tra schema, ID, tham chiếu chéo, độ phủ mục tiêu, đáp án bài tập; kiểm tra `course.yaml` và `cefr-<level>.yaml` | `python -I scripts/content-tools/validate_content_v2.py .` |
| `extract_de.py` | Trích toàn bộ chuỗi tiếng Đức để soát lỗi | `python -I scripts/content-tools/extract_de.py content/a1 de.txt` |
| `render_pdf.py` | Chuyển trang PDF (dạng ảnh scan) thành PNG để đọc | `python -I scripts/content-tools/render_pdf.py file.pdf out_dir 1.5 17-22` |
| `fix_quotes.py` | Đổi ngoặc kép kiểu CSV `""x""` trong YAML thành “x” | `python -I scripts/content-tools/fix_quotes.py file.yaml` |

Quy tắc kiểm tra: [content-validation-rules.md](../../docs/content/content-validation-rules.md).

Lưu ý: file PDF tài liệu của Klett **không** được lưu trong repo (bản quyền) – tải lại theo đường dẫn trong `docs/curriculum/a1/handoff.md`.

Lịch sử: bộ chuyển đổi hệ cũ → v2 (`migrate_v1_to_v2.py`) và validator cũ đã bị xóa sau khi migration Kapitel 1–6 hoàn tất; bản lưu nằm trong `.backup-content-v1/` (cục bộ, không đưa lên git).
