# ADR-0004: Giao tiếp giữa các service

- **Trạng thái:** Đã chấp nhận
- **Ngày:** 2026-11-21

## Bối cảnh

Có 2 service (`core-service`, `ai-service`) và web client. Cần cơ chế giao tiếp tin cậy, đơn giản, không thêm hạ tầng khi chưa thật sự cần.

## Quyết định

### 1. Bất đồng bộ: BullMQ trên Redis

- Dùng cho job dài: chấm bài viết, chấm phát âm, tạo embedding, sinh nội dung hàng loạt.
- Tên hàng đợi theo dạng `<service-nhận>.<task>.<sự-kiện>`, ví dụ `ai.writing-eval.requested` và `core.writing-eval.completed`.
- Payload được định nghĩa và **đánh version** trong `packages/contracts/events`.
- Consumer phải **idempotent** (khóa theo `jobId` hoặc `attemptId`). Có retry với backoff và dead-letter.
- Bên gửi dùng **outbox pattern** để không mất job khi ghi DB thành công nhưng đẩy job thất bại.

Redis đã có sẵn cho cache, nên chưa cần thêm broker riêng.

### 2. Đồng bộ nội bộ: REST `/internal/v1`

- Hiện chỉ có một hướng: **ai → core**, ví dụ `GET /internal/v1/learners/:id/context`.
- Xác thực bằng service token. Không expose qua gateway.
- Contract định nghĩa trong `packages/contracts/internal-api`.
- **core không gọi đồng bộ sang ai trong luồng học chính.**

### 3. Public qua gateway

- `/api/v1/*` → `core-service`; `/api/v1/ai/*` → `ai-service`.
- JWT RS256 do `identity` phát hành. `ai-service` xác thực bằng JWKS.
- Streaming AI dùng SSE.

### 4. Quan sát hệ thống

- Mọi request và job mang **correlation ID** (`x-request-id`, truyền qua metadata của job).
- Log JSON (pino), định dạng thống nhất qua `packages/service-kit`.
- Tracing OpenTelemetry được thêm ở Phase 5. Correlation ID có từ Phase 1.

## Giới hạn đã biết và điều kiện thay đổi

BullMQ là hàng đợi **point-to-point** (mỗi job có một bên nhận), không phải pub/sub. Khi cần **một event gửi đến nhiều bên nhận** (ví dụ thêm `analytics-service` hoặc `notification-service`), hoặc khi có từ 3 service trở lên, thì chuyển sang **RabbitMQ hoặc NATS JetStream** và viết ADR mới. Contract trong `packages/contracts/events` giữ nguyên, chỉ đổi phần truyền tải trong `service-kit/messaging`.
