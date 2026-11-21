# Deutsch-lernen

Nền tảng web học tiếng Đức theo lộ trình CEFR **A1 → C2**, có các tính năng AI hỗ trợ người học.

> **Trạng thái hiện tại:** đã có cấu trúc thư mục và tài liệu kiến trúc.
> Chưa khởi tạo project (chưa có `package.json`), chưa cài package, chưa có source code.

## Kiến trúc

**Hybrid:** một Modular Monolith (`core-service`) và một AI service tách riêng (`ai-service`).

- Lý do lựa chọn: [ADR-0001](docs/adr/0001-hybrid-architecture.md)
- Tổng quan kiến trúc và sơ đồ: [docs/architecture/overview.md](docs/architecture/overview.md)

## Cấu trúc thư mục

| Thư mục | Nội dung |
|---|---|
| [`apps/web`](apps/web) | Frontend (Next.js) cho người học và admin |
| [`services/core-service`](services/core-service) | Backend chính (NestJS, Modular Monolith): identity, curriculum, vocabulary, practice, progress, media… |
| [`services/ai-service`](services/ai-service) | Toàn bộ tính năng AI: tutor, chấm bài viết, giải thích ngữ pháp, hội thoại, phát âm |
| [`packages/contracts`](packages/contracts) | Hợp đồng giao tiếp giữa các service (event, internal API) |
| [`packages/service-kit`](packages/service-kit) | Thư viện backend dùng chung (log, tracing, auth, lỗi, messaging) |
| [`packages/api-client`](packages/api-client) | Client TypeScript sinh tự động từ OpenAPI, dùng cho web và mobile |
| [`packages/shared`](packages/shared) | Kiểu và hằng số domain (CEFR level, skill, exercise type) |
| [`packages/config`](packages/config) | Cấu hình tsconfig, eslint, vitest dùng chung |
| [`content`](content) | Nội dung học dạng file (A1–C2), quản lý version bằng git |
| [`e2e`](e2e) | Test end-to-end (Playwright) |
| [`infra`](infra) | Docker, gateway, compose, observability |
| [`scripts`](scripts) | Script tự động hóa |
| [`docs`](docs) | Tài liệu dự án và ADR |

## Công nghệ đã chốt

| Lớp | Công nghệ |
|---|---|
| Ngôn ngữ / repo | TypeScript (strict), pnpm workspaces + Turborepo |
| Backend | NestJS trên Node.js LTS, Drizzle ORM |
| Frontend | Next.js (App Router), Tailwind CSS, shadcn/ui, TanStack Query, Zustand, React Hook Form + Zod, next-intl |
| Dữ liệu | PostgreSQL + pgvector, Redis (cache, rate limit, BullMQ), lưu trữ chuẩn S3 (MinIO / R2) |
| AI | Claude (Anthropic SDK) chạy sau lớp provider của `ai-service`; embedding qua Voyage AI; speech qua Azure AI Speech |
| API | REST `/api/v1`, OpenAPI 3.1, lỗi theo RFC 9457 Problem Details |
| Kiểm thử | Vitest, Testing Library, MSW, Testcontainers, Playwright, AI evals |
| Vận hành | Docker Compose, Caddy, GitHub Actions, Sentry, Langfuse |

## Lộ trình

1. **Phase 1:** nền tảng dự án (monorepo, tooling, docker-compose, khung service, CI)
2. **Phase 2:** core backend và frontend (auth, curriculum, lesson player)
3. **Phase 3:** hệ thống học tập (exercise engine, vocabulary + SRS, progress, nội dung A1)
4. **Phase 4:** tích hợp AI (writing evaluation → grammar → tutor → vocabulary → conversation)
5. **Phase 5:** kiểm thử, tối ưu và triển khai

Chi tiết ở [docs/architecture/overview.md](docs/architecture/overview.md#roadmap).
