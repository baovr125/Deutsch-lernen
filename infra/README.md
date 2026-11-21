# infra/

Đóng gói và triển khai. Tách khỏi code ứng dụng.

| Thư mục | Nội dung | Phase |
|---|---|---|
| `docker/` | `web.Dockerfile`, `core-service.Dockerfile`, `ai-service.Dockerfile` (multi-stage) | 1 |
| `gateway/` | `Caddyfile`: TLS, nén, rate limit thô, định tuyến | 1 |
| `compose/` | `docker-compose.prod.yml` và override theo môi trường. File compose cho dev nằm ở gốc repo | 1 / 5 |
| `observability/` | Cấu hình otel-collector, dashboard | 5 |
| `terraform/` | Hạ tầng cloud dạng code, chỉ dùng khi thật sự cần | Sau |

## Định tuyến của gateway

| Đường dẫn | Đích |
|---|---|
| `/api/v1/ai/*` | ai-service |
| `/api/v1/*`, `/.well-known/jwks.json` | core-service |
| `/internal/*` | **Chặn**, không expose ra ngoài |
| `/*` | web |

## Môi trường dev (docker-compose.yml ở gốc, Phase 1)

PostgreSQL + pgvector (2 database `core` và `ai`), Redis, MinIO, Mailpit.
