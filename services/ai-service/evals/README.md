# evals/

Bộ đánh giá chất lượng cho các tính năng AI. Đây là **cổng chất lượng** khi đổi prompt, model hoặc provider.

| Thư mục | Nội dung |
|---|---|
| `datasets/` | Dữ liệu có nhãn: bài viết mẫu kèm band CEFR và lỗi kỳ vọng, câu hỏi ngữ pháp kèm đáp án đúng, hội thoại mẫu… Không chứa dữ liệu cá nhân thật |
| `runners/` | Script chạy eval cho từng task và chấm điểm (so khớp quy tắc, hoặc LLM-as-judge có rubric) |
| `reports/` | Kết quả mỗi lần chạy, để so sánh giữa các version (có thể không commit báo cáo lớn) |

## Khi nào chạy

- Thủ công trước khi phát hành prompt hoặc model mới.
- Hằng đêm qua `.github/workflows` (Phase 4–5).
- **Không chạy ở mỗi PR** vì tốn chi phí API.

Ngưỡng đạt của từng task được ghi trong `docs/ai/evaluation.md`.
