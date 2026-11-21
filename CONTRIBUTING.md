# Hướng dẫn đóng góp

## Quy trình

1. Tạo nhánh từ `main`: `feat/<mô-tả>`, `fix/<mô-tả>`, `docs/<mô-tả>`, `chore/<mô-tả>`.
2. Commit theo [Conventional Commits](https://www.conventionalcommits.org/), ví dụ `feat(practice): thêm loại bài gap-fill`.
3. Mở PR. CI phải xanh (lint, typecheck, test, kiểm tra ranh giới module, kiểm tra OpenAPI).
4. Thay đổi kiến trúc phải có ADR mới trong `docs/adr/`.

## Nguyên tắc

- Tôn trọng ranh giới module: xem `services/core-service/src/modules/README.md`.
- Thay đổi API, dữ liệu hoặc AI thì cập nhật tài liệu tương ứng trong cùng PR.
- Không commit `.env` hoặc bất kỳ secret nào.
