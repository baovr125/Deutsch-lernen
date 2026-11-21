# content/

Nội dung học dạng file, quản lý version bằng git, được **validate theo schema** và sẽ được **import vào DB** bằng script (`scripts/`). Sau này `content-admin` (CMS) sẽ dần thay thế việc soạn bằng file.

Đặc tả đầy đủ: [docs/curriculum/a1/a1-lesson-content-spec.md](../docs/curriculum/a1/a1-lesson-content-spec.md).

## Cấu trúc

```text
content/
├── _schemas/                     # JSON Schema (draft 2020-12) cho mọi loại file nội dung
│   ├── common.schema.json        #   kiểu dùng chung (source, example, exercise…)
│   ├── course / unit / lesson / grammar-topic / vocabulary-row / cefr .schema.json
├── a1/
│   ├── course.yaml               # lộ trình cấp độ: unit theo thứ tự + trạng thái
│   ├── cefr-a1.yaml              # danh mục can-do CEFR của cấp độ
│   ├── grammar/g-a1-*.yaml       # chủ điểm ngữ pháp (giải thích ở mức của cấp độ)
│   ├── vocabulary/<NN>-<slug>.csv
│   └── units/
│       └── <NN>-<slug>/          # <số thứ tự>-<slug tiếng Đức, không dấu, kebab-case>, vd. 01-guten-tag
│           ├── unit.yaml
│           ├── lesson-01.yaml …  # bài học
│           ├── review.yaml       # tổng kết + kiểm tra cuối unit
│           └── audio/
├── a2/ b1/ b2/ c1/ c2/           # chưa có nội dung
└── grammar/                      # để dành cho chỉ mục ngữ pháp liên cấp độ (nguồn RAG) – chưa dùng
```

## File từ vựng (CSV)

UTF-8 không BOM, có header, phân cách bằng dấu phẩy:

`id, unit, lesson, lemma, article, plural, pos, forms, ipa, meaning_vi, example_de, example_vi, usage_vi, level, tags, source`

- `article`: `der` / `die` / `das` – bắt buộc với danh từ; `plural`: dạng số nhiều đầy đủ hoặc `—`.
- `forms`: dạng động từ cần nhớ (vd. `du sprichst, er spricht`).
- `ipa`: phiên âm trong `[ ]`.
- `tags`: phân cách bằng `;` (vd. `zahl;aussprache`, `sg-only`, `mehrdeutig`, `mit-artikel`).
- `source`: `nwn-lern` (Lernwortschatz của giáo trình) · `nwn` (có trong danh sách từ của giáo trình) · `supplement` (bổ sung).

## Quy tắc

- **Giáo trình chỉ dùng làm tham chiếu** cho trình tự, chủ đề, phạm vi ngữ pháp/từ vựng. **Không sao chép** hội thoại, bài đọc, bài tập, đáp án, audio hay video của giáo trình; mọi nội dung là tự biên soạn. Ghi nguồn tham chiếu trong trường `source`.
- Không dùng tài liệu có bản quyền khác (đề thi, sách) khi chưa có giấy phép.
- Nội dung do AI hỗ trợ soạn phải được **người duyệt** trước khi merge.
- Mọi thay đổi nội dung đi qua PR và phải qua validator (0 lỗi).
