# packages/

Thư viện dùng chung trong monorepo. Một package **không được** import từ `apps/` hoặc `services/`.

| Package | Nội dung | Được dùng bởi |
|---|---|---|
| `contracts/` | `events/`: schema payload job/event giữa các service (zod/JSON Schema, có version). `internal-api/`: kiểu request/response của `/internal/v1` | core-service, ai-service |
| `api-client/` | `openapi.json` (snapshot từ 2 service) và client TS + hook TanStack Query sinh bằng orval. CI dùng oasdiff để chặn breaking change | web, (sau này) mobile |
| `service-kit/` | Thư viện backend: `logging/` (pino), `tracing/` (correlation ID, OpenTelemetry), `auth/` (xác thực JWT/JWKS, service token), `http-errors/` (Problem Details), `messaging/` (BullMQ producer/consumer idempotent, outbox) | core-service, ai-service |
| `shared/` | TS thuần: `cefr/` (CefrLevel, sub-level), `constants/` (Skill, ExerciseType…), `schemas/` (zod dùng chung) | Mọi nơi |
| `config/` | Preset `typescript/`, `eslint/`, `vitest/` | Mọi package |

**Quy tắc:** chỉ đưa code vào `packages/` khi có từ 2 nơi trở lên cần dùng. Đừng tạo package "phòng khi cần".
