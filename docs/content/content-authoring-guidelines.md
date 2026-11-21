# Content Authoring Guidelines

> Tài liệu này dành cho **người biên soạn**: viết thế nào cho đúng, đủ, nhất quán. Cấu trúc dữ liệu: [content-standard.md](content-standard.md). Kiểm tra tự động: [content-validation-rules.md](content-validation-rules.md).

## 1. Bản quyền và nguồn

- Giáo trình (Netzwerk neu A1) chỉ dùng để tham chiếu **chủ đề, trình tự, phạm vi ngữ pháp/từ vựng, mục tiêu giao tiếp**.
- Không chép hoặc dịch sát bài đọc, hội thoại, bài tập, đáp án, transcript, hình ảnh. Mọi ví dụ, hội thoại, bài đọc, bài tập phải do mình viết (tên nhân vật, tình huống, số liệu đều khác sách).
- Ghi phần nào đã xác minh với giáo trình (`verified`), phần nào do dự án đề xuất (`proposed`) trong `metadata.references`.

## 2. Tiếng Đức

1. Chính tả và ngữ pháp chuẩn Hochdeutsch; dùng `ä ö ü ß` (không viết `ae/oe/ue/ss` thay thế trong câu).
2. **Danh từ luôn có Artikel** khi đứng một mình (`der Termin`, không `Termin`), có `plural`; danh từ không đếm được dùng `no_plural: true`.
3. Mỗi ví dụ là câu hoàn chỉnh: viết hoa đầu câu, có dấu câu cuối. Ngoại lệ: mẫu câu/cụm trong `expressions` được phép là cụm.
4. Câu tự nhiên, ngắn (A1: thường ≤ 10–12 từ); thì hiện tại là chủ yếu; Perfekt chỉ xuất hiện khi chương trình đã tới (Kapitel 10 trở đi), `Präteritum` chỉ `war/hatte`.
5. Không dùng cấu trúc vượt trình độ mà không giải thích. Nếu bắt buộc (ví dụ cụm cố định), ghi chú trong `usage_vi`: "học thuộc như cụm".
6. Dùng `du` cho tình huống thân mật, `Sie` cho trang trọng; ghi rõ `register` ở expressions.
7. Số liệu, ngày giờ, tên người/địa danh đa dạng (D-A-CH), không cố định một nhân vật.

## 3. Tiếng Việt

- Giải thích ngắn, thân thiện, ưu tiên ví dụ rồi mới đến quy tắc; so sánh với tiếng Việt khi giúp tránh lỗi quen (vd. tiếng Việt không có chia động từ).
- Thuật ngữ nhất quán (giữ nguyên tiếng Đức, kèm tên Việt lần đầu): *Akkusativ* (đối cách), *Dativ* (tặng cách), *Artikel* (mạo từ), *Präposition* (giới từ), *Konjunktion* (liên từ), *Verb/Satzposition* (vị trí động từ), *Modalverb* (động từ khuyết thiếu), *Imperativ* (mệnh lệnh).
- Bản dịch `vi` là **nghĩa tự nhiên**, không dịch từng chữ; không bỏ sót ý.

## 4. Từ vựng

- Mỗi mục: nghĩa, loại từ, Artikel + số nhiều (danh từ), IPA, 1 câu ví dụ + dịch, `usage_vi` (ngữ cảnh, kết hợp từ, lưu ý lỗi hay gặp).
- Một lemma một mục; từ nhiều nghĩa chỉ nêu nghĩa thuộc phạm vi A1, nghĩa khác ghi trong `usage_vi`.
- Ví dụ phải chứa chính từ đó (dạng chia hoặc số nhiều được chấp nhận).
- Số lượng gợi ý: 35–60 từ/module tự biên soạn (ưu tiên từ giao tiếp thật sự cần, không nhồi nhét).

## 5. Ngữ pháp

Một chủ điểm theo thứ tự: **tóm tắt → khi nào dùng → quy tắc (kèm bảng nếu cần) → cấu trúc câu → ví dụ → lỗi thường gặp → bài tập**. Mỗi quy tắc có ví dụ riêng. Lỗi thường gặp có dạng sai, dạng đúng và lý do. Chỉ dạy một ý chính mỗi quy tắc.

## 6. Bài học

- 1–3 mục tiêu/bài, viết dạng "Bạn có thể…" (can-do), mỗi mục tiêu gắn một `skill`.
- Cấu trúc khuyến nghị: dẫn nhập → hội thoại/bài đọc (có dịch) → giải thích → phát âm (nếu có) → luyện tập (ở tệp exercises).
- Hội thoại 6–10 lượt lời, bài đọc 40–80 từ, nghe: transcript ngắn, `audio_status: pending-tts`.

## 7. Bài tập

- Mỗi bài học có **≥ 5 dạng bài khác nhau** và mỗi mục tiêu có ít nhất một bài kiểm tra nó (`objective_refs`).
- Mọi item có đáp án và `explanation_vi` nêu **vì sao** đúng (và vì sao phương án gây nhiễu sai khi hữu ích).
- Trắc nghiệm: 3–4 lựa chọn, nhiễu hợp lý, vị trí đáp án đúng đa dạng.
- Điền chỗ trống: một chỗ `___`, liệt kê mọi đáp án chấp nhận. Sắp xếp từ: token đã xáo, có `translation_vi`. Dịch: liệt kê các cách dịch chấp nhận. Viết/nói: đáp án mẫu + rubric kiểm được (3–4 tiêu chí).
- Bài đo kiến thức vừa dạy; không dùng từ/cấu trúc chưa học.

## 8. Danh sách tự kiểm tra trước khi nộp

- [ ] Chạy `python -I scripts/content-tools/validate_content_v2.py . <module_dir>` → 0 lỗi.
- [ ] Đọc lại toàn bộ câu tiếng Đức (Artikel, chia động từ, vị trí động từ, chính tả).
- [ ] Không có đoạn nào chép từ sách.
- [ ] `status` đặt `draft`; chỉ chuyển `reviewed` sau khi người thứ hai đọc.
