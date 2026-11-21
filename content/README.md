# content/

Nội dung học dạng file, quản lý version bằng git, được **validate trong CI** và **import vào DB** bằng script (`scripts/`). Sau này `content-admin` (CMS) sẽ dần thay thế việc soạn bằng file.

## Cấu trúc

```text
content/
├── _schemas/                 # schema validate file nội dung
├── a1/
│   ├── course.yaml           # metadata khóa học: tiêu đề, mô tả, thứ tự unit
│   ├── units/
│   │   └── 01-begruessung/   # <số thứ tự>-<slug tiếng Đức, không dấu, kebab-case>
│   │       ├── lesson-01.yaml
│   │       └── audio/
│   └── vocabulary/           # danh sách từ dạng CSV
├── a2/ b1/ b2/ c1/ c2/
└── grammar/                  # thư viện ngữ pháp dùng chung mọi level (nguồn cho RAG của AI)
```

## Cột dự kiến cho file từ vựng (CSV)

`lemma, article, plural, pos, level, meaning_vi, example_de, example_vi, tags`

- `article`: `der` / `die` / `das` (với danh từ)
- Động từ: ghi chú tách được, dạng Präteritum/Perfekt, cách đi kèm trong `tags` (sẽ chốt trong `_schemas`)

## Quy tắc

- **Không dùng tài liệu có bản quyền** (giáo trình, đề thi) khi chưa có giấy phép. Ghi nguồn trong metadata.
- Nội dung do AI hỗ trợ soạn phải được **người duyệt** trước khi merge.
- Mọi thay đổi nội dung đi qua PR.
