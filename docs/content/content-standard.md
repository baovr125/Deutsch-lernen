# Content Standard v2

> Phiên bản: 2.0 · Phạm vi áp dụng: mọi nội dung học (A1–C2). Hiện mới áp dụng cho A1 Kapitel 7–12.
> Tài liệu này định nghĩa **cái gì** là một đơn vị nội dung hợp lệ (định dạng, trường dữ liệu, ID, metadata).
> Cách tổ chức thư mục: [content-architecture.md](content-architecture.md). Cách viết: [content-authoring-guidelines.md](content-authoring-guidelines.md). Cách kiểm tra: [content-validation-rules.md](content-validation-rules.md). Chuyển nội dung cũ: [content-migration-guidelines.md](content-migration-guidelines.md).

## 1. Nguyên tắc

1. **Mỗi tệp một loại nội dung** (trường `content_type`), mỗi loại có nhánh riêng trong một schema duy nhất: [content.schema.json](../../content/_schemas/v2/content.schema.json).
2. **Định dạng YAML** (dễ đọc, dễ review diff, hỗ trợ chuỗi nhiều dòng tiếng Việt), kiểm tra bằng **JSON Schema 2020-12** (YAML được parse thành JSON trước khi kiểm tra).
3. **Tham chiếu bằng ID, không lồng nội dung**: bài học chỉ chứa danh sách ID từ vựng/ngữ pháp/biểu thức; nội dung gốc nằm đúng một chỗ (tái sử dụng, không lệch dữ liệu).
4. **Mọi nội dung đều tự biên soạn** (`metadata.origin: original`); giáo trình chỉ là tham chiếu phạm vi, ghi trong `metadata.references` với nhãn `verified` hoặc `proposed`.
5. **Mọi câu tiếng Đức đi kèm bản dịch tiếng Việt; mọi câu bài tập có lời giải (`explanation_vi`).**

## 2. Các loại nội dung (`content_type`)

| content_type | Tệp | Vai trò |
|---|---|---|
| `module` | `module.yaml` | Gốc của một Kapitel: mục tiêu, danh sách tệp con, ánh xạ giáo trình |
| `lesson` | `lessons/lNN.yaml` | Bài học: mục tiêu, tham chiếu, các khối dạy (hội thoại, bài đọc, nghe, phát âm…) |
| `vocabulary-set` | `vocabulary.yaml` | Toàn bộ từ vựng của module |
| `grammar-topic` | `content/<level>/grammar/<slug>.yaml` | Một chủ điểm ngữ pháp, **dùng chung cho cả level** (không nằm trong module) |
| `expression-set` | `expressions.yaml` | Mẫu câu/Redemittel theo chức năng giao tiếp |
| `exercise-set` | `exercises/lNN.yaml` | Bài tập của một bài học |
| `assessment` | `assessment.yaml` | Bài kiểm tra cuối module (đủ 4 kỹ năng) |

## 3. Trường chung (mọi tệp)

| Trường | Kiểu | Ý nghĩa |
|---|---|---|
| `schema_version` | `"2.0"` | Phiên bản chuẩn |
| `content_type` | enum | Xem bảng §2 |
| `id` | string | ID duy nhất toàn hệ thống (§4) |
| `level` | `A1`…`C2` | Cấp CEFR |
| `version` | semver | Phiên bản nội dung (tăng khi sửa: patch = lỗi chính tả, minor = thêm mục, major = đổi cấu trúc/ID) |
| `status` | `draft` / `reviewed` / `published` | Vòng đời duyệt |
| `language` | `{target: de, explanation: vi}` | Ngôn ngữ học / ngôn ngữ giải thích |
| `metadata` | object | `authors`, `created`, `updated`, `origin`, `references[]`, `tags[]`, `notes_vi` |

Trường riêng từng loại: xem schema. Trường `difficulty` (1 = dễ, 2 = vừa, 3 = khó trong phạm vi A1) có ở lesson và exercise; `module` có ở mọi tệp thuộc module (lesson, vocabulary, expressions, exercise-set, assessment). Riêng `grammar-topic` dùng `introduced_in` (module dạy chủ điểm lần đầu) thay cho `module`.

## 4. Quy ước ID

Định dạng: `<level>.<module>[.<phần>…]`, chữ thường, `a–z 0–9` và dấu `-`, các cấp nối bằng dấu `.`.

| Đối tượng | Mẫu | Ví dụ |
|---|---|---|
| Module | `a1.m07` | `a1.m07` |
| Mục tiêu module | `a1.m07.obj.<slug>` | `a1.m07.obj.tagesablauf` |
| Lesson | `a1.m07.l01` | |
| Mục tiêu bài | `a1.m07.l01.obj1` | |
| Khối trong bài | `a1.m07.l01.b1` | |
| Từ vựng | `a1.m07.v.<lemma-slug>` | `a1.m07.v.buero` |
| Biểu thức | `a1.m07.x.<slug>` | `a1.m07.x.termin-fragen` |
| Ngữ pháp (dùng chung level) | `a1.g.<slug>` | `a1.g.mit-dativ` |
| Quy tắc / mục tiêu ngữ pháp | `a1.g.<slug>.r1`, `a1.g.<slug>.obj1` | |
| Bộ bài tập | `a1.m07.l01.ex` | |
| Bài tập | `a1.m07.l01.ex.01` | |
| Câu hỏi | `a1.m07.l01.ex.01.q1` | |
| Bài đánh giá | `a1.m07.test` | |

Quy tắc: ID **bất biến** sau khi `published` (đổi nội dung được, đổi ID thì không — tiến độ học của người dùng bám vào ID). Slug lemma: bỏ dấu (`ä→ae`, `ö→oe`, `ü→ue`, `ß→ss`), chữ thường, khoảng trắng → `-`. Tiền tố bắt buộc = ID module chứa nó; ngoại lệ duy nhất là ngữ pháp dùng chung (`<level>.g.…`). Module dùng chủ điểm bằng cách khai báo ID trong `module.yaml › grammar` và `lesson › grammar_refs`.

## 5. Từ vựng (`vocabulary-set.entries[]`)

Bắt buộc: `id, de, pos, vi, ipa, example{de,vi}, usage_vi, lesson_refs`.

- `pos`: `noun, verb, adjective, adverb, preposition, conjunction, pronoun, numeral, particle, phrase`.
- Danh từ: bắt buộc `article` (`der/die/das`, hoặc `pl` nếu chỉ có số nhiều) và **một trong** `plural` (dạng số nhiều, không kèm Artikel) hoặc `no_plural: true`.
- Động từ: bắt buộc `forms.er` (ngôi 3 số ít, vd. `arbeitet`, `fährt`); `forms.separable: true` với động từ tách. Tùy chọn `forms.perfekt` (vd. `hat gekocht`, `ist gefahren`) từ Kapitel 10 trở đi.
- `ipa`: bọc trong `/…/`. `lemma` danh từ viết hoa; từ loại khác viết thường.

## 6. Ngữ pháp (`grammar-topic`)

Bắt buộc: `title_de, title_vi, summary_vi, usage_vi (khi nào dùng), objectives, rules[], sentence_structures[], examples (≥4), common_mistakes (≥1), exercise_refs (≥1)`.
Mỗi `rule` có `title_vi, body_vi, examples (≥1)` và tùy chọn `table{header, rows}` để hiển thị bảng chia.

## 7. Bài tập (`exercise`)

Chung: `id, type, skill, difficulty, objective_refs, instructions_vi, items[]` (+ `stimulus`, `word_bank` tùy dạng).

| `type` | Dạng `item` |
|---|---|
| `multiple-choice`, `reading-comprehension`, `listening-practice` | `prompt, options[{id a–e, text}], answer[ids], explanation_vi` |
| `fill-blank` | `prompt` (≥ 1 chỗ `___`), `answers[]` (đáp án của từng chỗ trống theo thứ tự; số phần tử = số chỗ trống), `accept?` (các tổ hợp thay thế), `hint_vi?` |
| `matching` | `left, right` (mỗi item là một cặp) **hoặc** `pairs[{left,right}]` (một item chứa cả nhóm ≥ 2 cặp) |
| `word-order` | `tokens[]` (đã xáo), `answer`, `translation_vi` |
| `translation` | `direction: vi-de/de-vi, source, answers[]` |
| `sentence-construction` | `prompt_vi, required_words[], answers[]` |
| `writing-practice`, `speaking-practice` | `prompt_vi, model_answer{de,vi}, rubric_vi[]` |

Mọi item đều có `explanation_vi`. `reading-comprehension` yêu cầu `stimulus.{text_de,text_vi}`; `listening-practice` yêu cầu `stimulus.{text_de,audio_status}` (`pending-tts` cho tới khi có audio).

## 8. Metadata và tham chiếu giáo trình

```yaml
metadata:
  authors: ["Deutsch-lernen"]
  created: "2026-11-21"
  updated: "2026-11-21"
  origin: original
  references:
    - { work: "Netzwerk neu A1 (A1.2)", scope: "Kapitel 7, Grammatik: mit + Dativ", verification: verified }
    - { work: "Dự án", scope: "Bài tập thêm về giới từ", verification: proposed }
  tags: ["arbeit"]
```

`verified` = có trong tài liệu chính thức đã đối chiếu (Stoffverteilungsplan, Kapitelwortschatz của Klett); `proposed` = bổ sung của dự án.

## 9. Phần mở rộng sau đợt migration Kapitel 1–6

Để hệ mới chứa được toàn bộ thông tin của Kapitel 1–6, chuẩn bổ sung (đều tùy chọn trừ khi ghi khác):

- **Module**: `kind` (`intro`/`kapitel`/`plattform`), `cefr[]`, `not_covered_vi[]`; `objectives`, `grammar`, `expressions`, `assessment` là tùy chọn. ID module: `a1.m00` (Einstieg), `a1.mNN` (Kapitel NN), `a1.pN` (Plattform N). `order` = vị trí trong `course.yaml`.
- **Lesson**: `kind: lesson|review` (bài ôn tập cuối Kapitel là lesson `review`, id `a1.mNN.review`), `topic_vi`, `cefr[]`, `prerequisites[]`, `review_vocabulary_refs[]` (từ ôn lại của module trước), `grammar_focus[{ref,focus_vi}]`, `summary_vi`, `self_check[]`.
- **Block**: thêm loại `examples`, `speaking` (`task_vi`, `steps_vi`, `lines`), `writing` (`task_vi`, `model`, `checklist_vi`); `examples[]`, `glossary[]`, `text_type_vi`, `situation_vi`, `audio{file,speed}` ở các loại phù hợp.
- **Từ vựng**: `pos` thêm `name`, `article`, `interrogative`, `interjection`; `forms.text` (dạng chia dạng văn bản), `source` (`nwn-lern`/`nwn`/`supplement`); `usage_vi` vẫn bắt buộc (đã bổ sung đủ cho mọi từ).
- **Ngữ pháp**: `exercises[]` ghi trực tiếp trong tệp (thay cho `exercise_refs`), `tables[]`, `comparison_vi`, `vietnamese_contrast_vi`, `recap_vi`, `prerequisites`, `next_level_note_vi`, `introduced_in_lesson`. Bài tập ngữ pháp có thể trỏ tới ID quy tắc (`a1.g.<slug>.rN`) như một mục tiêu.
- **Bài tập**: thêm loại `true-false` (item `prompt`, `answer: bool`) và `dictation` (item `tts`, `answers[]`); `stimulus.ref` trỏ tới khối của bài học làm ngữ liệu; `instructions_de`, `tip_vi`, `grading` (`auto|self|ai`), `rubric[{criterion_vi,points}]`; `word-order` có `prompt_vi?`, `translation_vi?`; `sentence-construction` có `required_words?`; `writing/speaking` có `model_answer{de,vi?}`.
- **Biểu thức**: `function` tùy chọn; `dialogue[]` (hội thoại minh họa).
- **Course**: bước trong `path` dùng `module: modules/<thư-mục>`; schema tại `_schemas/v2/course.schema.json`.
- **Module đánh giá** (`kind: assessment`, id `a1.final`): `lessons` và `vocabulary` tùy chọn; `assessments[]` liệt kê nhiều phiên bản đề tương đương.
- **Assessment**: `sections[]` (`skill_group`, `points`, `pass_percent`, `duration_min`, `exercise_refs[]`; mỗi bài tập thuộc đúng một phần), `version_label`, `equivalent_to`, `overall_pass_percent`, `pass_rule_vi`.
