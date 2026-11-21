# scripts/

Script tự động hóa cho dev và CI. Dự kiến (Phase 1–3):

| Script | Mục đích |
|---|---|
| `setup` | Cài dependency, tạo `.env` từ `.env.example`, khởi động docker-compose, chạy migration và seed |
| `db-migrate` / `db-seed` | Chạy migration và seed cho từng service |
| `content-validate` | Validate `content/` theo `content/_schemas` (chạy trong CI) |
| `content-import` | Import `content/` vào DB core |
| `gen-api-client` | Xuất OpenAPI từ 2 service, sinh `packages/api-client` |
| `backup-db` / `restore-db` | Sao lưu và khôi phục PostgreSQL |
