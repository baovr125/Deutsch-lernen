# Tài liệu dự án

Tài liệu nằm cạnh code và được review cùng PR. Khi một thay đổi ảnh hưởng đến kiến trúc, API, dữ liệu hoặc AI, hãy cập nhật tài liệu tương ứng trong cùng PR.

## Mục lục

| Thư mục | Nội dung | Trạng thái |
|---|---|---|
| [`architecture/`](architecture) | [overview.md](architecture/overview.md): tổng quan, sơ đồ, luồng chính, roadmap. `diagrams/`: sơ đồ bổ sung | Đã có overview |
| [`adr/`](adr) | Architecture Decision Records. Dùng [0000-template.md](adr/0000-template.md) cho quyết định mới | 0001–0004 |
| `requirements/` | `srs.md`, `cefr-mapping.md` (can-do statements → tính năng/nội dung), `user-stories/` | Phase 1 |
| `database/` | `erd.md`, `data-dictionary.md`, `migration-policy.md` | Phase 1–2 |
| `api/` | `conventions.md` (đặt tên, versioning, lỗi, phân trang), `authentication.md`, `deprecation-policy.md`. Spec OpenAPI **sinh tự động**, không viết tay ở đây | Phase 1–2 |
| `ai/` | `overview.md`, `features/` (mỗi tính năng một file: mục tiêu, I/O, prompt, tiêu chí eval), `model-selection.md`, `evaluation.md`, `safety-privacy-cost.md` | Phase 4 |
| `guides/` | `getting-started.md`, `coding-standards.md`, `git-workflow.md`, `adding-a-module.md`, `adding-an-exercise-type.md`, `content-authoring.md` | Phase 1–3 |
| `deployment/` | `environments.md`, `runbook.md`, `backup-restore.md` | Phase 5 |
| `testing/` | `strategy.md`, `test-data.md` | Phase 1 |

## Quy ước

- Viết bằng tiếng Việt. Thuật ngữ kỹ thuật và tên định danh giữ nguyên tiếng Anh.
- Sơ đồ dùng Mermaid nhúng trong Markdown để diff được.
- ADR đã chấp nhận thì không sửa nội dung quyết định. Muốn thay đổi thì viết ADR mới và đánh dấu ADR cũ là "Bị thay thế".
