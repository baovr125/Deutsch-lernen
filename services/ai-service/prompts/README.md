# prompts/

Prompt là **dữ liệu có version**, tách khỏi code.

## Quy ước

- Đường dẫn: `prompts/<task>/<tên>.v<N>.md`, ví dụ `writing-eval/rubric.v1.md`, `tutor-chat/system.v2.md`.
- Tên thư mục phải trùng với tên task trong `src/tasks/`.
- Mỗi file có frontmatter, ví dụ:

  ```yaml
  ---
  task: writing-eval
  version: 1
  model_profile: default        # tham chiếu config/models.yaml
  output_schema: WritingEvalResult
  levels: [A1, A2, B1, B2, C1, C2]
  ---
  ```

- **Không sửa version đã phát hành.** Muốn thay đổi thì tạo `v<N+1>`, chạy eval, rồi chuyển config sang version mới.
- Phần ổn định (system prompt, rubric) đặt ở đầu để tận dụng prompt caching. Phần thay đổi theo request đặt ở cuối.
- Bài làm của người học luôn được đặt trong khối dữ liệu riêng và được coi là **dữ liệu, không phải chỉ thị**.
