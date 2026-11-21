# ADR-0002: TypeScript cho toàn hệ thống, monorepo pnpm + Turborepo

- **Trạng thái:** Đã chấp nhận
- **Ngày:** 2026-11-21

## Bối cảnh

Hệ thống gồm 1 frontend, 2 backend service và (sau này) mobile. Đội nhỏ, cần chia sẻ kiểu dữ liệu và contract giữa các phần, và cần môi trường dễ thiết lập cho người mới.

## Quyết định

| Hạng mục | Lựa chọn | Phương án thay thế đã cân nhắc |
|---|---|---|
| Ngôn ngữ | TypeScript (strict) cho FE và cả 2 service | Python (FastAPI) cho backend: hệ sinh thái AI mạnh hơn nhưng mất phần kiểu dùng chung |
| Repo | **Monorepo**, pnpm workspaces + Turborepo | Polyrepo (quá tốn công cho đội nhỏ); Nx (mạnh nhưng nặng) |
| Backend framework | NestJS: module system khớp với modular monolith, DI giúp dễ test, có sẵn Swagger, guard, pipe | Fastify/Hono (nhẹ hơn nhưng phải tự dựng cấu trúc) |
| ORM | Drizzle: schema chia theo module, SQL minh bạch, hỗ trợ pgvector | Prisma (DX dễ hơn, hỗ trợ pgvector kém hơn) |
| Frontend | Next.js (App Router): SEO cho landing, layout lồng nhau | Vite + React Router (đơn giản hơn nếu không cần SEO) |
| Test runner | Vitest cho toàn bộ monorepo | Jest |

`ai-service` cũng dùng TypeScript. Nếu sau này phần speech cần thư viện Python, có thể tách riêng một worker Python sau `SpeechProvider` mà không ảnh hưởng phần còn lại.

## Hệ quả

- Contract (`packages/contracts`) và client sinh tự động (`packages/api-client`) được dùng trực tiếp ở mọi nơi.
- Một bộ lint, format và test dùng chung (`packages/config`).
- Ranh giới module được kiểm tra bằng dependency-cruiser trong CI.
