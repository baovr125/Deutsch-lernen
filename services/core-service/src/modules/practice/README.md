# practice

Exercise engine của nền tảng.

- `domain/exercise-types/`: mỗi loại bài tập gồm **schema payload** (zod) và **grader**.
  Các loại dự kiến: `multiple-choice`, `gap-fill`, `matching`, `ordering`, `dictation`, `writing`, `speaking`.
- `domain/ports/`: interface module cần từ bên ngoài, ví dụ `FreeTextGrader` (do `ai-bridge` implement) cho bài viết và bài nói.
- Reading, Listening, Writing, Speaking **không phải module riêng**. Chúng là thuộc tính `skill` của bài tập.
- Payload bài tập lưu dạng JSONB và được validate theo schema của loại, nên thêm loại mới **không cần migration**.
- Bài tập đóng được chấm bằng code. Chỉ bài viết và bài nói mới cần AI.

Hướng dẫn thêm loại bài tập: `docs/guides/adding-an-exercise-type.md` (Phase 3).
