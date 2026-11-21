# platform/

Hạ tầng kỹ thuật dùng chung cho mọi module của core-service. **Không chứa nghiệp vụ** và **không được import từ `modules/`**.

| Thư mục | Trách nhiệm |
|---|---|
| `http/` | Global exception filter (Problem Details), zod validation pipe, interceptor (logging, request-id), decorator (`@Public()`, `@Roles()`, `@CurrentUser()`) |
| `database/` | Drizzle client, transaction helper |
| `events/` | Event bus trong process giữa các module, kèm outbox |
| `queue/` | Cấu hình BullMQ (dùng cho job nội bộ và giao tiếp với ai-service) |
| `cache/` | Redis cache helper |
| `storage/` | Adapter lưu trữ chuẩn S3, presigned URL |
| `observability/` | Logger (pino), correlation ID, (sau này) tracing |
| `errors/` | Lớp lỗi domain: `DomainError`, `NotFoundError`, `ForbiddenError`… |

Phần nào dùng chung với `ai-service` thì đặt ở `packages/service-kit` thay vì ở đây.
