# core-service

Backend chính: **Modular Monolith** viết bằng NestJS. Chứa toàn bộ nghiệp vụ học tập, xác thực và quản lý nội dung.

## Cấu trúc

```text
src/
├── main.ts / worker.ts   # (Phase 1) entrypoint HTTP và entrypoint xử lý job — cùng code, 2 process
├── config/               # schema biến môi trường (zod), dừng khởi động nếu cấu hình thiếu hoặc sai
├── platform/             # hạ tầng kỹ thuật dùng chung — KHÔNG chứa nghiệp vụ
├── modules/              # các module nghiệp vụ — xem modules/README.md
└── database/
    ├── migrations/
    └── seeds/
test/
├── integration/          # Testcontainers: Postgres, Redis thật
├── fixtures/
└── helpers/
```

## API

| Tiền tố | Ai gọi | Xác thực |
|---|---|---|
| `/api/v1/*` | Web, mobile (qua gateway) | JWT (cookie httpOnly cho web, Bearer cho mobile) |
| `/internal/v1/*` | `ai-service` | Service token, không expose qua gateway |
| `/.well-known/jwks.json` | `ai-service`, gateway | Công khai |

Lỗi trả về theo RFC 9457 Problem Details. Spec OpenAPI được sinh từ code.

## Sở hữu dữ liệu

Database `core`. Mỗi bảng chỉ thuộc **một module**, khai báo trong `modules/<module>/infrastructure/`.
