# A1 Lesson Content Specification – Đặc tả nội dung bài học

> ⚠️ **Đã lỗi thời (2026-11-21):** nội dung A1 đã chuyển sang **Content Standard v2** (`content/a1/modules/`, `content/a1/grammar/`). Các đường dẫn/định dạng cũ (`units/`, `vocabulary/*.csv`, `g-a1-*.yaml`, `validate_content.py`) không còn tồn tại. Chuẩn hiện hành: [docs/content/content-standard.md](../../content/content-standard.md). Tài liệu này giữ lại để tham khảo lịch sử và phạm vi sư phạm.


> Áp dụng cho mọi bài học A1 (và làm mẫu cho các cấp độ sau). Schema: [`content/_schemas/`](../../../content/_schemas). Cập nhật: 2026-11-21.

## 1. Bố cục file

```
content/
├── _schemas/
│   ├── common.schema.json          # kiểu dùng chung: source, example, dialogueLine, exercise…
│   ├── course.schema.json          # content/<level>/course.yaml
│   ├── unit.schema.json            # units/<NN>-<slug>/unit.yaml
│   ├── lesson.schema.json          # units/<NN>-<slug>/lesson-NN.yaml, review.yaml
│   ├── grammar-topic.schema.json   # grammar/<id>.yaml
│   ├── vocabulary-row.schema.json  # mỗi dòng của vocabulary/*.csv
│   └── cefr.schema.json            # cefr-<level>.yaml
└── a1/
    ├── course.yaml                 # lộ trình: Einstieg, 12 Kapitel, 4 Plattform, Abschlusstest
    ├── cefr-a1.yaml                # 20 mã can-do A1
    ├── grammar/g-a1-*.yaml         # chủ điểm ngữ pháp
    ├── vocabulary/<NN>-<slug>.csv  # từ vựng theo unit
    └── units/
        ├── 00-einstieg/            # unit.yaml, lesson-01…04.yaml, audio/
        └── 01-guten-tag/           # unit.yaml, lesson-01…05.yaml, review.yaml, audio/
```

**Quy ước tên:** thư mục unit `<NN>-<slug>` (slug tiếng Đức, không dấu, kebab-case, theo tên Kapitel: *Guten Tag!* → `guten-tag`). Bài học `lesson-NN.yaml` theo trường `order`; bài tổng kết là `review.yaml`.

**Quyết định về thư mục ngữ pháp:** chủ điểm A1 đặt ở `content/a1/grammar/` (giải thích ở đúng mức A1). Thư mục dùng chung `content/grammar/` được giữ nguyên, để dành cho chỉ mục ngữ pháp liên cấp độ sau này (ví dụ làm nguồn RAG). *Cần bạn xác nhận – xem báo cáo Phase 1.*

## 2. Mã định danh (ID)

| Đối tượng | Mẫu | Ví dụ |
|---|---|---|
| Unit | `a1-u00` (nhập môn), `a1-kNN` (Kapitel), `a1-pN` (Plattform), `a1-final` | `a1-k01` |
| Lesson | `<unit>-lNN`, review: `<unit>-review` | `a1-k01-l03` |
| Từ vựng | `<unit>-vNNN` | `a1-k01-v046` |
| Chủ điểm ngữ pháp | `g-a1-<slug>` | `g-a1-w-fragen` |
| Bài tập | `<lesson-id>-exNN` hoặc `<grammar-id>-exNN` | `a1-k01-l03-ex05` |
| Redemittel | `<lesson-id>-rNN` | `a1-k01-l02-r03` |
| Khối kỹ năng | `<lesson-id>-listen-NN` / `-read-NN` / `-speak-NN` / `-write-NN` | `a1-k01-l04-listen-01` |
| Mục tiêu bài | `o1`, `o2`… (trong phạm vi bài); bài tập trong chủ điểm ngữ pháp dùng `r1`, `r2`… (tham chiếu quy tắc) | |
| CEFR | `A1.H1`…, `A1.L1`…, `A1.SI1`…, `A1.SP1`…, `A1.S1`… | |

## 3. Cấu trúc một bài học (ánh xạ yêu cầu → trường dữ liệu)

| Yêu cầu | Trường | Bắt buộc |
|---|---|---|
| **6.1 Lesson Overview** – ID, tiêu đề, chủ đề, mục tiêu, cấp độ CEFR, thời lượng, điều kiện tiên quyết | `id`, `title_de`, `title_vi`, `topic_vi`, `objectives[]`, `level` + `cefr[]`, `estimated_minutes`, `prerequisites[]`; thêm `source` (mục giáo trình tương ứng hoặc `supplement`) và `intro_vi` (lời dẫn) | ✅ |
| **6.2 Vocabulary** | `vocabulary.file`, `vocabulary.new[]`, `vocabulary.review[]` → dòng trong CSV có đủ: từ, nghĩa, từ loại, mạo từ, số nhiều, IPA, câu ví dụ + dịch, ghi chú | ✅ |
| **6.3 Grammar** | `grammar.topics[]` (tham chiếu chủ điểm, kèm `focus_vi` – phần cần tập trung trong bài) và `grammar.notes[]` (ghi chú ngắn ngay trong bài) | ✅ |
| **6.4 Redemittel** | `redemittel[]`: `de`, `vi`, `context_vi`, `register` (formal/informal/neutral), `dialogue[]` (≥ 2 lượt) | ✅ |
| **Pronunciation** | `pronunciation[]`: trọng tâm, giải thích, ví dụ có IPA, cách luyện | ✅ (mảng có thể rỗng) |
| **Examples** | `examples[]`: `de`, `vi`, `note_vi` | ✅ ≥ 1 |
| **6.5 Four Skills** | `skills.listening[]` (kịch bản + trạng thái audio), `skills.reading[]` (văn bản + bản dịch + từ khó), `skills.speaking[]` (nhiệm vụ, các bước, mẫu), `skills.writing[]` (nhiệm vụ, bài mẫu, checklist) – mỗi khối liên kết tới bài tập | ✅ mỗi kỹ năng ≥ 1 |
| **6.6 Exercises** | `exercises[]`: `id`, `type`, `skill`, `objectives[]`, `difficulty` (1–3), `instructions_vi`, `items[]` có đáp án và `explanation_vi` | ✅ ≥ 1 |
| Tổng kết | `summary_vi`, `self_check[]` (danh sách “Tôi có thể…”) | ✅ |

## 4. Dạng bài tập

| `type` | Dùng cho | Đáp án | Chấm |
|---|---|---|---|
| `multiple-choice` | từ vựng, ngữ pháp, đọc/nghe hiểu | `answer` = một chuỗi nằm trong `options` | tự động |
| `true-false` | đọc/nghe hiểu, quy tắc | `answer` = true/false | tự động |
| `gap-fill` | chia động từ, điền từ | `prompt` chứa `___`; `answer` = mảng (mỗi chỗ trống một phần tử); `accept` = các phương án khác | tự động |
| `matching` | từ ↔ nghĩa, câu hỏi ↔ câu trả lời | `pairs[]` (vế trái/phải duy nhất) | tự động |
| `ordering` | trật tự từ trong câu | `tokens[]` (đã xáo trộn) + `answer` | tự động |
| `translation` | dịch vi→de hoặc de→vi (`direction`) | `answer` + `accept[]` | tự động (so khớp chuẩn hóa) / AI sau này |
| `sentence-building` | tạo câu từ từ gợi ý | `answer` + `accept[]` | tự động |
| `dictation` | nghe – viết | `tts` (văn bản đọc) + `answer` | tự động |
| `writing` | viết tin nhắn, đoạn văn, biểu mẫu | `model_answer` + `rubric[]` | `self` (nay), `ai` (khi có AI service) |
| `speaking` | nói, đóng vai | `model_answer` + `rubric[]` | `self` (nay), `ai` (khi có AI service) |

**Quy định chung:** mọi câu hỏi có `explanation_vi`; bài nghe/đọc tham chiếu khối kỹ năng qua `stimulus`; bài viết/nói có rubric chấm theo tiêu chí; mỗi mục tiêu `o*` của bài có ít nhất một bài tập kiểm tra; mỗi bài học thường có ≥ 5 dạng bài tập khác nhau.

**Chuẩn hóa khi chấm tự động (đề xuất cho exercise engine):** bỏ khoảng trắng thừa; không phân biệt dấu câu cuối; **phân biệt chữ hoa/thường** (vì danh từ phải viết hoa) – trừ khi bài tập ghi chú khác; chấp nhận `ae/oe/ue/ss` thay cho `ä/ö/ü/ß` nhưng hiển thị nhắc nhở.

## 5. Audio

- Mọi khối nghe có `script` đầy đủ (người nói, câu tiếng Đức, bản dịch) và `audio.status`.
- Hiện tại: `pending-tts` – audio sẽ được tạo bằng TTS giọng Đức chuẩn (dự kiến Azure AI Speech, theo ADR-0003), tốc độ `slow` cho bài học, `normal` cho bài kiểm tra.
- Khi có file: `status: recorded`, `file: audio/<id>.mp3` trong thư mục `audio/` của unit.
- Kịch bản và bản dịch chỉ hiển thị **sau** khi người học làm xong bài nghe.

## 6. Chiến lược giảng dạy cho người Việt (bắt buộc)

1. Tiếng Việt là ngôn ngữ giải thích; tiếng Đức xuất hiện trong ví dụ, Redemittel và đề bài song ngữ.
2. Thuật ngữ ngữ pháp luôn kèm giải thích bình dân, ví dụ: *Nominativ = cách của chủ ngữ – “ai/cái gì” làm hành động*.
3. Mỗi chủ điểm có mục **so sánh với tiếng Việt** và **lỗi thường gặp của người Việt**, ví dụ:
   - quên chia động từ (*Ich heißen*), bỏ động từ (*Ich Lan*);
   - quên mạo từ, viết thường danh từ;
   - đặt từ để hỏi ở cuối câu (*Du kommst woher?*), dịch từng chữ (*Was heißt du?*);
   - đọc đều mọi âm tiết như tiếng Việt, bỏ âm cuối, thêm thanh điệu;
   - nhầm er/sie (tiếng Việt “bạn ấy” dùng chung).
4. Ví dụ phải tự nhiên, sát đời sống người Việt ở Đức/Áo/Thụy Sĩ (đăng ký khóa học, cư trú, làm quen) và không vượt phạm vi đã học.

## 7. Quy trình biên soạn một Kapitel

1. Đọc các trang Stoffverteilungsplan và Kapitelwortschatz của Kapitel → ghi phạm vi vào [netzwerk-neu-a1-mapping.md](netzwerk-neu-a1-mapping.md).
2. Chia Kapitel thành bài theo các mục của giáo trình; viết `unit.yaml` (kể cả `not_covered_vi`).
3. Viết từ vựng (CSV) → chủ điểm ngữ pháp → từng bài học → `review.yaml`.
4. Chạy validator (xem §8), sửa đến khi **0 lỗi**.
5. Soát tiếng Đức (trích toàn bộ câu tiếng Đức ra một danh sách để đọc lại) và tiếng Việt.
6. Cập nhật `course.yaml` (status), các syllabus và báo cáo.

## 8. Kiểm tra tự động

Validator hiện chạy ngoài repo; sẽ chuyển thành `scripts/content-validate` khi khởi tạo tooling của dự án. Validator kiểm tra:

- Mọi file YAML/CSV hợp lệ theo schema.
- Tham chiếu chéo: unit ↔ lesson ↔ course; từ vựng `new`/`review` tồn tại và đúng thứ tự (không “ôn” từ chưa học); mỗi từ dạy mới đúng một lần; chủ điểm ngữ pháp và mã CEFR tồn tại; `prerequisites` đứng trước.
- Bài tập: ID duy nhất toàn cục; đáp án trắc nghiệm nằm trong lựa chọn; số `___` = số đáp án; `tokens` khớp `answer`; cặp nối không trùng; `stimulus` đúng khối; mỗi mục tiêu có bài tập kiểm tra.
- Từ vựng: danh từ có mạo từ và viết hoa; IPA trong `[ ]`; không trùng từ; UTF-8 không BOM.
