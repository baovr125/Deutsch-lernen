# ai-bridge

Phía core của giao tiếp với `ai-service` (Phase 4). Xem [ADR-0004](../../../../../docs/adr/0004-inter-service-communication.md).

- `application/`: kiểm tra quota AI theo người dùng hoặc gói; implement `practice/domain/ports/FreeTextGrader`; xử lý kết quả trả về (idempotent).
- `infrastructure/`: producer và consumer BullMQ (`ai.*.requested` / `core.*.completed`), dùng contract từ `packages/contracts`.

Module này **không** chứa prompt, không gọi LLM, và không biết provider nào đang được dùng.
