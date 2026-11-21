# e2e/

Test end-to-end bằng Playwright, chạy trên **stack đầy đủ** (web, core-service, ai-service với provider `mock`).

- `tests/`: kịch bản theo luồng người dùng, ví dụ đăng ký → mở bài A1 → làm bài → xem tiến độ.
- `fixtures/`: dữ liệu và trạng thái chuẩn bị sẵn.

Unit test đặt cạnh code (`*.spec.ts`). Integration test nằm trong `test/` của từng service.
