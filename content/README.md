# content/

Nội dung học dạng file, quản lý version bằng git, được **validate theo schema** và sẽ được **import vào DB** bằng script (`scripts/`). Sau này `content-admin` (CMS) sẽ dần thay thế việc soạn bằng file.

Chuẩn nội dung: **Content Standard v2** — xem [docs/content/content-standard.md](../docs/content/content-standard.md) (định nghĩa), [content-architecture.md](../docs/content/content-architecture.md) (tổ chức thư mục), [content-authoring-guidelines.md](../docs/content/content-authoring-guidelines.md) (cách biên soạn), [content-validation-rules.md](../docs/content/content-validation-rules.md) (kiểm tra).

## Cấu trúc

```text
content/
├── _schemas/v2/                  # JSON Schema (draft 2020-12): content / course / cefr
├── a1/
│   ├── course.yaml               # LỘ TRÌNH: thứ tự học, mỗi bước trỏ tới một module
│   ├── cefr-a1.yaml              # danh mục can-do CEFR của cấp độ
│   ├── grammar/<slug>.yaml       # NGỮ PHÁP dùng chung cả cấp độ (id a1.g.<slug>)
│   └── modules/
│       └── <mNN|pN>-<slug>/      # mNN = Kapitel NN (m00 = Einstieg); pN = Plattform N
│           ├── module.yaml
│           ├── vocabulary.yaml
│           ├── expressions.yaml
│           ├── lessons/ l01.yaml … (review.yaml là bài ôn tập, kind: review)
│           ├── exercises/ l01.yaml …
│           └── assessment.yaml   # chỉ có ở m07–m12
│   (f-abschlusstest/ = Abschlusstest A1: assessment-a.yaml + assessment-b.yaml, hai đề tương đương)
├── a2/ b1/ b2/ c1/ c2/           # chưa có nội dung
└── grammar/                      # để dành cho chỉ mục ngữ pháp liên cấp độ – chưa dùng
```

Kiểm tra: `python -I scripts/content-tools/validate_content_v2.py .` (phải 0 lỗi trước khi merge).

## Quy tắc

- **Giáo trình chỉ dùng làm tham chiếu** cho trình tự, chủ đề, phạm vi ngữ pháp/từ vựng. **Không sao chép** hội thoại, bài đọc, bài tập, đáp án, audio hay video của giáo trình; mọi nội dung là tự biên soạn. Ghi nguồn tham chiếu trong `metadata.references`.
- Không dùng tài liệu có bản quyền khác (đề thi, sách) khi chưa có giấy phép.
- Nội dung do AI hỗ trợ soạn phải được **người duyệt** trước khi merge.
- Mọi thay đổi nội dung đi qua PR và phải qua validator (0 lỗi).
