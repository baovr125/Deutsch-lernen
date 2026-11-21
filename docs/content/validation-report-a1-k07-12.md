# Báo cáo kiểm tra – A1 Kapitel 7–12 (modules a1.m07 – a1.m12)

> Ngày: 2026-11-21 · Chuẩn: Content Standard v2 · Trạng thái dữ liệu: `draft` (chưa có người duyệt thứ hai)

## 1. Tự động

Lệnh: `python -I scripts/content-tools/validate_content_v2.py .` (và `validate_content.py . a1` cho hệ cũ — vẫn 0 lỗi).

| Chỉ số | Kết quả |
|---|---|
| Lỗi / cảnh báo | **0 / 0** |
| Module đã đăng ký trong `course.yaml` | 6 (m07–m12) |
| Bài học | 24 |
| Chủ điểm ngữ pháp (dùng chung) | 21 |
| Từ vựng / biểu thức | 280 / 73 |
| Bài tập | 215 (trong đó 48 bài tập thuộc bài kiểm tra); 641 câu hỏi |
| ID duy nhất | 1579 |
| Dạng bài | đủ 10 dạng của yêu cầu |

Kiểm thử âm tính (đợt Kapitel 7): sửa tạm một bản sao (bỏ `article`, đáp án ngoài options, tham chiếu từ không tồn tại, lệch `lesson_refs`) → validator báo đúng 4 lỗi.

## 2. Đã sửa trong quá trình soạn

- Loại bỏ cấu trúc vượt trình độ ở nhiều chỗ: Perfekt trước K10, đại từ Dativ trước K11, tính từ có đuôi (attributive) vì chưa học, `weil`, `zu + Infinitiv`.
- Lỗi token sắp xếp từ (chữ hoa/dấu chấm), gợi ý lộ đáp án, ví dụ không chứa từ vựng.
- Mở rộng schema: `forms.perfekt` (từ K10).

## 3. Soát thủ công (tự soát, chưa có người thứ hai)

**Tiếng Đức** — đã đọc lại Artikel/Plural, chia động từ bất quy tắc và Partizip II. Cần người bản ngữ/giáo viên xem: tính tự nhiên của các câu bài tập, cách dùng „Wie war's?“, „Kann ich Ihnen helfen?“, các cụm học thuộc có đại từ Dativ trước K11 („Ihnen“, „mir“ trong cụm cố định).
**Tiếng Việt** — thuật ngữ nhất quán (Dativ = tặng cách, Akkusativ = đối cách, Perfekt = quá khứ hoàn thành khi nói…). Câu dịch ưu tiên nghĩa tự nhiên.
**Sư phạm** — mỗi mục tiêu bài/ngữ pháp/module có bài kiểm tra; mỗi bài học ≥ 6 dạng bài.

## 4. Giới hạn đã biết

1. **Chưa đối chiếu từng từ** với Kapitelwortschatz K7–12 (chưa đọc bản scan) → từ vựng là đề xuất theo chủ đề đã xác minh. Cần một lượt đối chiếu trước khi `reviewed`.
2. Audio: mọi nội dung nghe là `pending-tts`.
3. Validator kiểm tra cấu trúc và một số quy tắc ngôn ngữ đơn giản; **không** kiểm tra được ngữ pháp tiếng Đức tự động.
4. Ngưỡng 60% của bài kiểm tra chưa được xác nhận.
5. Plattform 3–4 và Abschlusstest A1 chưa soạn.
6. Perfekt với *sein* ở K10 là bổ sung của dự án (chưa xác minh với giáo trình).
7. Kapitel 1–6 chưa chuyển sang chuẩn v2 (Phase migration riêng).

## 5. Toàn bộ A1 sau migration Kapitel 1–6 (cập nhật 2026-11-21)

Kapitel 1–6, Einstieg và Plattform 1–2 đã được chuyển sang v2 ([migration](content-migration-guidelines.md) §5); toàn bộ A1 hiện dùng một chuẩn.

| Chỉ số | Kết quả |
|---|---|
| Lỗi / cảnh báo | **0 / 0** (125 từ vựng của Kapitel 1–6 từng thiếu `usage_vi` đã được bổ sung) |
| Module | 18 (m00–m12, p1–p4, f-abschlusstest), tất cả đăng ký trong `course.yaml` |
| Bài học | 81 (gồm 6 bài ôn `review`) |
| Chủ điểm ngữ pháp | 46 |
| Từ vựng / biểu thức | 1109 / 224 |
| Bài tập | 215 + 415 trong bài học + 53 trong ngữ pháp (xem validator) |

Lưu ý: nội dung Kapitel 1–6 đã qua soát của phiên trước và được đối chiếu số lượng 100% với bản cũ; đợt này **chưa** có người đọc lại tiếng Đức/tiếng Việt của Kapitel 1–6.

## 6. Plattform 3–4, Abschlusstest A1, tên quy tắc ngữ pháp (cập nhật 2026-11-21)

- **Plattform 3 và 4** (`p3-plattform-3`, `p4-plattform-4`): mỗi module 3 bài (Wiederholen und trainieren · Landeskunde · Prüfungstraining), đề luyện tự soạn. Phạm vi phần thi: Plattform 3 – Lesen 2, Hören 3, Sprechen 3; Plattform 4 – Hören 2, Lesen 3, Schreiben 2.
- **Abschlusstest A1** (`f-abschlusstest`): hai đề tương đương A và B, mỗi đề 14 bài tập chia 5 phần (Hören 15 · Lesen 15 · Schreiben 15 · Sprechen 15 · Wortschatz & Grammatik 20 điểm danh nghĩa). Số câu ít hơn bản thiết kế gốc (cỡ ~38 câu/đề so với ~60 nếu điểm = số câu). Điều kiện ‘độ phủ CEFR 20/20’ và ‘độ nhớ từ vựng nhóm nwn-lern ≥ 80%’ thuộc hệ thống tiến độ, chưa có trong dữ liệu.
- **Tên quy tắc ngữ pháp Kapitel 1–6:** 77 quy tắc / 25 chủ điểm đã được đặt tên và viết lại mục tiêu cho đúng nghĩa.
- Giới hạn mới: bài ôn/luyện thi Plattform 3–4 và đề Abschlusstest chưa có người duyệt thứ hai; audio là `pending-tts`; từ vựng chủ đề văn hóa của Plattform là đề xuất.
