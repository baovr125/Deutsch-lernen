# Content Architecture v2

> Tài liệu này trả lời: **nội dung được chia thành các tệp nào, đặt ở đâu, liên kết với nhau ra sao** và vì sao.
> Định nghĩa trường: [content-standard.md](content-standard.md).

## 1. Mô hình khái niệm

```text
Curriculum (content/<level>/course.yaml; mỗi bước trỏ tới một module qua trường `module`)
└── Level (A1…C2)
    └── Module (= một Kapitel; module.yaml)
        ├── Lesson ×N (lessons/lNN.yaml)       ← dạy: mục tiêu + khối nội dung
        │     └─ tham chiếu (ID) tới Vocabulary / Grammar / Expressions / ExerciseSet
        ├── Vocabulary (vocabulary.yaml)       ← kho từ của module
        ├── Expressions (expressions.yaml)
        ├── ExerciseSet ×N (exercises/lNN.yaml) ← 1 bộ / bài học
        └── Assessment (assessment.yaml)       ← kiểm tra cuối module, đủ 4 kỹ năng
```

Skills Practice (Hören/Sprechen/Lesen/Schreiben) **không** là tệp riêng: nó là (a) các **khối** `listening`/`reading`/`dialogue` trong Lesson và (b) các **exercise** có `skill` tương ứng. Lợi ích: một khái niệm duy nhất (`skill`) để lọc, thống kê tiến độ theo kỹ năng.

## 2. Cây thư mục

```text
content/
├── _schemas/v2/content.schema.json         # schema duy nhất của chuẩn v2
└── a1/
    ├── course.yaml                         # LỘ TRÌNH: thứ tự học; bước có `module:` trỏ tới module v2
    ├── grammar/                            # NGỮ PHÁP DÙNG CHUNG cả level (id a1.g.<slug>)
    │   └── konjunktionen.yaml, mit-dativ.yaml, ortspraepositionen.yaml, …
    └── modules/
        └── m07-arbeitsalltag/
            ├── module.yaml                 # khai báo grammar bằng đường dẫn ../../grammar/<slug>.yaml
            ├── vocabulary.yaml
            ├── expressions.yaml
            ├── lessons/ l01.yaml … l04.yaml
            ├── exercises/ l01.yaml … l04.yaml
            └── assessment.yaml
```

Thư mục module đặt tên `mNN-<slug>` (`NN` = số Kapitel, `m00` = Einstieg) hoặc `pN-<slug>` (Plattform N). Hệ định dạng cũ (units/CSV/schema cũ) đã được chuyển hoàn toàn sang v2 và xóa (xem [content-migration-guidelines.md](content-migration-guidelines.md) §5); toàn bộ nội dung A1 hiện dùng một chuẩn duy nhất.

## 3. Quyết định thiết kế và đánh đổi

| Quyết định | Lý do | Đánh đổi |
|---|---|---|
| Tách Vocabulary/Grammar/Exercises khỏi Lesson, nối bằng ID | Một nguồn sự thật; ôn tập, flashcard, AI Tutor truy vấn thẳng kho từ/ngữ pháp mà không phải bóc từ bài học | Cần validator kiểm tra tham chiếu (đã có) |
| Từ vựng là **một tệp/module**, không theo bài | Từ có thể xuất hiện ở nhiều bài; dễ xuất sang SRS | Tệp dài hơn (~100 mục); chia theo `lesson_refs` |
| Ngữ pháp **một tệp/chủ điểm, đặt ở cấp level** (`a1/grammar/`), ID không mang tiền tố module | Diff nhỏ; Kapitel sau chỉ cần tham chiếu ID, không copy | Phải nhớ chủ điểm thuộc module nào dạy đầu tiên (`introduced_in`) |
| Exercise **kèm `objective_refs`** | Đo được "mục tiêu nào đã đạt" → tiến độ học theo mục tiêu, không chỉ theo bài | Tác giả phải gắn mục tiêu cho từng bài tập |
| Một schema nhiều nhánh `if/then` | Một điểm cập nhật; dễ nhúng vào backend | Thông báo lỗi dài hơn schema riêng từng loại |
| YAML thay CSV cho từ vựng | Có ví dụ, ghi chú, mảng; không lỗi dấu ngoặc | Không mở trực tiếp bằng Excel |

## 4. Tích hợp

- **Lộ trình**: web đọc `course.yaml` → `module.yaml` → các tệp con (và `a1/grammar/` cho ngữ pháp), tất cả nối bằng ID.
- **Frontend**: render theo `blocks[].kind` và `exercise.type`; không cần suy đoán định dạng.
- **Backend**: nạp YAML → bảng/collection theo `content_type`; khóa chính = `id`; `version` để cache-bust.
- **Tiến độ học**: lưu theo `id` của lesson, exercise item, vocab entry, objective.
- **AI Tutor**: truy xuất theo `id`/`tags`; `usage_vi` và `common_mistakes` là ngữ cảnh giải thích sẵn có.
- **Audio**: `audio_status: pending-tts` đánh dấu nội dung chờ sinh âm thanh; transcript luôn có sẵn trong dữ liệu.
