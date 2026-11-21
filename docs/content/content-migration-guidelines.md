# Content Migration Guidelines (Lektion 1–6 → Content Standard v2)

> Tài liệu này mô tả **cách** chuyển nội dung hệ cũ sang chuẩn v2. **Đã thực hiện cho A1 Kapitel 1–6 ngày 2026-11-21** — xem §5.
> Chuẩn đích: [content-standard.md](content-standard.md).

## 1. Điều kiện bắt đầu

1. Chuẩn v2 đã `published` và Kapitel 7–12 đã qua validator.
2. Quyết định hệ cũ: giữ song song (đọc cả hai) hay thay thế (khuyến nghị: thay thế sau khi migration xong, để backend chỉ hỗ trợ một định dạng).
3. Tạo nhánh git riêng; không sửa tại chỗ — sinh dữ liệu mới vào `content/a1/modules/…`, hệ cũ chỉ bị xóa ở bước cuối sau khi đối chiếu.

## 2. Ánh xạ khái niệm (cấp cao)

| Hệ cũ (tên khái niệm) | Chuẩn v2 |
|---|---|
| Course / Unit | Module (1 Kapitel = 1 module) |
| Lesson | Lesson (khối nội dung → `blocks`) |
| Bảng từ vựng dạng bảng phẳng | `vocabulary.yaml` (thêm `ipa`, `usage_vi`, `forms`, `lesson_refs`) |
| Chủ điểm ngữ pháp | `grammar/<slug>.yaml` (thêm `usage_vi`, `sentence_structures`, `common_mistakes`) |
| Bài tập | `exercises/lNN.yaml` (thêm `objective_refs`, `explanation_vi` đầy đủ) |
| Review/Test | `assessment.yaml` |

Chi tiết ánh xạ từng trường sẽ được lập khi bắt đầu Phase migration, sau khi đọc dữ liệu cũ (việc này có chủ ý **chưa** làm ở giai đoạn hiện tại).

## 3. Quy trình đề xuất

1. **Kiểm kê** từng Kapitel: đếm bài học, từ, ngữ pháp, bài tập; ghi vào bảng đối chiếu (nguồn dữ kiện duy nhất cho bước kiểm tra cuối).
2. **Sinh ID** theo [content-standard.md §4](content-standard.md). Lập bảng `id_cũ → id_mới` và lưu vào repo; tiến độ học đã có (nếu có người dùng thật) phải được ánh xạ theo bảng này.
3. **Chuyển bằng script**, không chỉnh tay hàng loạt; mỗi Kapitel một lần chạy, một commit.
4. **Bổ sung trường thiếu** (thường gặp): `ipa`, `usage_vi`, `forms.er`, `plural/no_plural`, `common_mistakes`, `objective_refs`, `explanation_vi`. Phần script không suy ra được → đánh dấu `status: draft` và `metadata.notes_vi: "Cần bổ sung: …"`, rồi biên soạn thủ công.
5. **Validate**: validator v2 đạt 0 lỗi; số lượng sau migration = số lượng kiểm kê (không mất từ/bài tập).
6. **Duyệt thủ công** theo [content-validation-rules.md §3](content-validation-rules.md); đổi `status` sang `reviewed`.
7. **Chuyển frontend/backend** sang đọc định dạng mới; chạy song song so sánh kết quả hiển thị; sau đó xóa hệ cũ.

## 4. Rủi ro và cách giảm

| Rủi ro | Giảm thiểu |
|---|---|
| Mất dữ liệu | Kiểm kê trước/sau; không xóa hệ cũ tới khi đối chiếu xong |
| Gãy tiến độ người dùng | Bảng `id_cũ → id_mới` và script chuyển tiến độ |
| Nội dung cũ thiếu trường bắt buộc mới | Đánh dấu `draft`, biên soạn bổ sung, không bịa tự động |
| Hai chuẩn tồn tại lâu | Đặt hạn chót cho Phase migration; ưu tiên làm ngay sau khi hoàn tất A1 |

## 5. Kết quả migration A1 Kapitel 1–6 (2026-11-21)

- **Phạm vi:** Einstieg (m00), Kapitel 1–6 (m01–m06), Plattform 1–2 (p1, p2) → 9 module, 51 bài học (45 bài + 6 bài ôn `review`), 819 từ vựng, 143 biểu thức, 25 chủ điểm ngữ pháp (dùng chung), 468 bài tập (415 trong bài học + 53 trong ngữ pháp).
- **Cách làm:** script chuyển đổi tự động (đã xóa sau khi xong), kiểm chứng bằng đối chiếu số lượng cũ–mới (từ vựng, nghĩa/ví dụ/IPA, khối kỹ năng, redemittel, hội thoại, bài tập, câu hỏi, giải thích từng câu, ngữ pháp: rules/tables/examples/common_mistakes/exercises) — **khớp 100%**.
- **Bảng ánh xạ ID:** [migration-id-map-a1.csv](migration-id-map-a1.csv) (id cũ → id mới cho lesson, vocabulary, expression, grammar).
- **Chuẩn hóa phát sinh (có chủ ý):**
  - Xáo trộn vị trí đáp án đúng của 322 câu trắc nghiệm (dữ liệu cũ: 141/149 câu 4 lựa chọn có đáp án ở vị trí đầu) và 2 câu sắp xếp từ đã đúng thứ tự.
  - Thêm dấu câu cuối cho 39 đáp án mẫu là câu Đức đầy đủ còn thiếu.
  - Mục tiêu (`objectives`) của bài học được gắn `skill` suy ra từ bài tập kiểm tra chúng; mục tiêu ngữ pháp và tên quy tắc được sinh tạm vì dữ liệu cũ không có — **đã được đặt lại tên thủ công cho cả 25 chủ điểm / 77 quy tắc (cùng ngày)**.
  - Từ nhiều ID cũ dạng `a1-k01-v001` → `a1.m01.v.<lemma>`.
- **Đã bổ sung sau migration:** 125 từ vựng thiếu `usage_vi` đã được viết bổ sung (cùng ngày), nên `usage_vi` vẫn là trường bắt buộc.
- **Tồn đọng:** audio chưa có (mọi phần nghe `pending-tts`; các thư mục `audio/` cũ chỉ chứa `.gitkeep`).
- **Đã xóa sau migration:** `content/a1/units/`, `content/a1/vocabulary/`, `content/a1/grammar/g-a1-*.yaml`, các schema cũ trong `content/_schemas/*.json`, `validate_content.py`. Bản sao lưu: `.backup-content-v1/` (cục bộ, bị bỏ qua bởi git).
