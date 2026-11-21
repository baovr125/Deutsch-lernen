# web

Frontend Next.js (App Router) cho người học và admin.

## Cấu trúc và quy tắc

| Thư mục | Trách nhiệm |
|---|---|
| `src/app/` | **Chỉ routing**, layout và ghép feature. Không chứa logic. Nhóm route: `(marketing)` SSR/SEO, `(auth)`, `(learn)` cần đăng nhập, `(admin)` |
| `src/features/<feature>/` | Module giao diện tự chứa: `components/`, `hooks/`, `api/` (hook TanStack Query bọc `@packages/api-client`), `store/` khi cần, `index.ts` là public API. Không import file bên trong feature khác |
| `src/features/exercises/types/` | Renderer cho từng loại bài tập. Thêm loại mới nghĩa là thêm renderer và đăng ký vào `registry.ts`; lesson player không cần sửa |
| `src/components/ui` | Primitive (shadcn/ui), không biết gì về nghiệp vụ |
| `src/components/layout` | AppShell, Sidebar, Header |
| `src/components/common` | AudioPlayer, CefrBadge, EmptyState… |
| `src/hooks/` | Hook dùng chung, không gắn nghiệp vụ |
| `src/lib/` | Cấu hình api-client, query client, session, utils |
| `src/stores/` | Zustand cho trạng thái UI toàn cục. **Dữ liệu từ server thuộc TanStack Query**, không chép sang store |
| `src/config/` | `cefr.ts`: giao diện và tính năng theo level, ví dụ A1–A2 hiện bản dịch tiếng Việt, C1–C2 chỉ dùng tiếng Đức |
| `src/i18n/messages/` | Ngôn ngữ giao diện (`vi.json`, sau này `en.json`). Nội dung tiếng Đức nằm trong DB |
| `tests/` | Test component và integration (dùng MSW để mock API) |

## Gọi API

- `/api/v1/*` → core-service; `/api/v1/ai/*` → ai-service (gateway định tuyến).
- Mọi kiểu dữ liệu lấy từ `packages/api-client` (sinh tự động), không viết tay.
