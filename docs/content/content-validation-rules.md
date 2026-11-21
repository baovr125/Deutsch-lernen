# Content Validation Rules

> Tài liệu này liệt kê **quy tắc kiểm tra** (tự động và thủ công). Công cụ: [validate_content_v2.py](../../scripts/content-tools/validate_content_v2.py). Chuẩn dữ liệu: [content-standard.md](content-standard.md).

Chạy: `python -I scripts/content-tools/validate_content_v2.py <repo_root> [content/a1/modules/m07-arbeitsalltag]` — mã thoát 0 khi không có ERROR.

## 1. Tự động – ERROR (chặn merge)

| Mã | Quy tắc |
|---|---|
| S1 | YAML parse được; khớp schema v2 (trường bắt buộc, kiểu, enum, pattern) |
| S2 | ID duy nhất trong toàn module (mọi cấp: mục tiêu, khối, từ, bài tập, câu hỏi) |
| S3 | ID có tiền tố = ID module (ngoại lệ: ngữ pháp dùng chung `<level>.g.…`) |
| S4 | `id` trong tệp = `id` khai báo ở `module.yaml`; `module` của tệp con khớp |
| R1 | Mọi tệp khai báo trong module tồn tại |
| R2 | `vocabulary_refs`, `grammar_refs`, `expression_refs`, `exercise_set_ref` của bài học trỏ tới ID có thật |
| R3 | `lesson_refs` của từ vựng/biểu thức trỏ tới bài học có thật |
| R4 | `exercise_refs` của ngữ pháp trỏ tới bài tập có thật |
| R5 | `objective_refs` của bài tập trỏ tới mục tiêu có thật |
| C1 | Mỗi mục tiêu (module, bài học, ngữ pháp) được ≥ 1 bài tập/đánh giá kiểm tra (bài học: bộ bài tập của chính bài đó; ngữ pháp: chỉ kiểm tra ở module `introduced_in`) |
| C2 | Bước trong `course.yaml` có trường `module` phải trỏ tới thư mục có `module.yaml` |
| V1 | Danh từ viết hoa; có Artikel và `plural` hoặc `no_plural` (schema) |
| V2 | Động từ có `forms.er` (schema) |
| E1 | Trắc nghiệm: mọi `answer` nằm trong `options`; không có hai lựa chọn giống hệt |
| E2 | Điền chỗ trống: số `___` trong `prompt` = số phần tử của `answers`; mỗi tổ hợp `accept` có cùng số phần tử |
| E3 | Sắp xếp từ: đa tập hợp `tokens` = đa tập hợp từ của `answer` (bỏ dấu câu ở đầu/cuối từ khi so) |
| E4 | Xây câu: nếu có `required_words`, mỗi đáp án mẫu chứa mọi từ đó |
| E5 | Matching: vế phải không trùng nhau (trong cả bài tập, hoặc trong từng nhóm `pairs`) |
| E6 | Nghe/đọc có `stimulus` (schema); `stimulus.ref` phải trỏ tới khối có thật của bài học |
| E8 | Assessment có `sections`: mọi `exercise_refs` tồn tại và mỗi bài tập thuộc đúng một phần |
| E7 | Course: `course.yaml` và `cefr-<level>.yaml` hợp lệ schema; bước `ready/draft` phải có `module` |

## 2. Tự động – WARNING (phải xem xét)

| Mã | Quy tắc |
|---|---|
| W1 | Câu Đức không viết hoa đầu câu / thiếu dấu câu cuối |
| W2 | Ví dụ không chứa từ vựng (có thể do biến cách – kiểm tra tay) |
| W3 | Từ vựng không được bài học nào tham chiếu; lemma lặp |
| W4 | Mọi đáp án trắc nghiệm cùng một vị trí; sắp xếp từ chưa xáo |
| W5 | Bài đánh giá thiếu một trong 4 kỹ năng |

## 3. Thủ công (người duyệt thứ hai)

**Ngôn ngữ Đức**: ngữ pháp, chính tả, Artikel/Plural đúng, ví dụ tự nhiên, từ đúng ngữ cảnh. Gợi ý trích mọi chuỗi `de:` thành một danh sách để đọc nhanh.
**Giải thích Việt**: dịch đúng nghĩa, dễ hiểu, thuật ngữ theo [content-authoring-guidelines.md](content-authoring-guidelines.md) §3.
**Chất lượng sư phạm**: đúng trình độ A1; thứ tự kiến thức hợp lý; bài tập chỉ dùng kiến thức đã dạy; đáp án đúng; mỗi bài ≥ 5 dạng bài tập.
**Bản quyền**: không có đoạn nào trùng/dịch sát giáo trình.

## 4. Báo cáo

Mỗi đợt biên soạn kèm một báo cáo (vd. [validation-report-a1-k07-12.md](validation-report-a1-k07-12.md)): kết quả validator, danh sách phát hiện thủ công, giới hạn đã biết.
