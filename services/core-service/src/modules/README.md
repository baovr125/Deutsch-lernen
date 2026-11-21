# modules/

Mỗi thư mục là một **module nghiệp vụ** có ranh giới rõ ràng.

## Danh sách module

| Module | Trách nhiệm | Phase |
|---|---|---|
| `identity` | Đăng ký, đăng nhập, Google OAuth, refresh token, user, role (learner / editor / admin), phát hành JWT + JWKS | 2 |
| `curriculum` | Level → Learning Path → Course → Unit → Lesson → ContentBlock; thư viện Grammar Topic | 2–3 |
| `vocabulary` | Lexeme (lemma, giống der/die/das, số nhiều, từ loại, cách đi kèm, ví dụ), word list, ôn tập SRS | 3 |
| `practice` | Exercise engine: loại bài tập (registry), quiz, attempt, chấm điểm | 3 |
| `progress` | Enrollment, hoàn thành bài, mức thành thạo theo kỹ năng × level, streak | 3 |
| `media` | Upload và phục vụ audio, ảnh (presigned URL) | 3 |
| `content-admin` | Import từ `content/`, soạn thảo, duyệt, publish | 3 |
| `ai-bridge` | Cầu nối sang ai-service: implement port `FreeTextGrader`, gửi job, nhận kết quả, quản lý quota AI | 4 |
| `recommendation` | Đề xuất bài học và ôn tập (bắt đầu bằng luật) | 4+ (chưa triển khai) |
| `notification` | Email, nhắc học | 5+ (chưa triển khai) |
| `analytics` | Thống kê học tập từ event | 5+ (chưa triển khai) |

## Cấu trúc bên trong một module

```text
<module>/
├── <module>.module.ts
├── index.ts          # PUBLIC API — chỉ export những gì module khác được phép dùng
├── api/              # controllers + DTO (zod) — tầng HTTP
├── application/      # use case / service
├── domain/           # logic thuần, không phụ thuộc NestJS hay DB (chỉ khi module có luật nghiệp vụ)
└── infrastructure/   # Drizzle schema (bảng do module sở hữu) + repository + adapter
```

Module CRUD đơn giản (`media`, `content-admin`) không cần `domain/`. Unit test đặt cạnh file (`*.spec.ts`).

## Quy tắc phụ thuộc (kiểm tra bằng dependency-cruiser trong CI)

1. Chỉ import từ `index.ts` của module khác, **không bao giờ** import file bên trong.
2. Mỗi bảng chỉ thuộc **một module**. Không join hoặc ghi vào bảng của module khác.
3. `platform/` không import `modules/`.
4. Module học tập **không phụ thuộc** `ai-bridge`. Ví dụ: `practice/domain/ports` định nghĩa `FreeTextGrader`, `ai-bridge` implement nó.
5. Phản ứng dây chuyền đi qua event (`AttemptGraded` → `progress`), không gọi vòng.
6. CEFR level là **thuộc tính dữ liệu**, không tạo module hay thư mục theo level.
