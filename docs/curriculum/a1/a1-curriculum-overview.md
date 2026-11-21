# A1 Curriculum Overview – Tổng quan chương trình A1

> Phase 1 · Phạm vi: **chỉ A1** · Nguồn trình tự chính: **Netzwerk neu A1** (Klett) · Chuẩn đầu ra: **CEFR A1**
> Cập nhật: 2026-11-21

## 1. Mục tiêu

Xây dựng một chương trình A1 hoàn chỉnh trên nền tảng Deutsch-lernen để **người Việt bắt đầu từ con số 0 có thể tự học không cần giáo viên**:
mở bài đầu tiên, học theo hướng dẫn tiếng Việt, luyện tập, làm bài kiểm tra và theo dõi tiến độ, cho đến khi đạt chuẩn A1.

## 2. Người học mục tiêu

| Đặc điểm | Hệ quả thiết kế |
|---|---|
| Người Việt, chưa biết tiếng Đức | Tiếng Việt là ngôn ngữ giải thích chính; mọi ví dụ tiếng Đức có bản dịch |
| Có thể đã biết một ít tiếng Anh | So sánh với tiếng Anh khi hữu ích (không bắt buộc) |
| Tự học, không có giáo viên | Mỗi bài có mục tiêu rõ, giải thích từng bước, đáp án **kèm giải thích**, tự kiểm tra (self_check), tiêu chí tự chấm cho viết/nói |
| Thói quen của tiếng Việt (thanh điệu, không chia động từ, không có giống, bỏ âm cuối) | Mỗi chủ điểm có mục *so sánh với tiếng Việt* và *lỗi thường gặp*; phần nhập môn tập trung vào phát âm |

## 3. Phạm vi Phase 1

**Trong phạm vi:** nghiên cứu Netzwerk neu A1; chuẩn đầu ra CEFR A1; phần nhập môn; nội dung 12 Kapitel; ngữ pháp và từ vựng A1; bài tập và đáp án; ôn tập (Plattform) và đánh giá tổng kết; tài liệu hướng dẫn tự học.

**Ngoài phạm vi:** mọi nội dung A2–C2; thiết kế chi tiết chương trình các cấp độ sau; thay thế Netzwerk neu A1 bằng giáo trình khác.
Khi một chủ điểm có phần mở rộng ở A2, tài liệu chỉ ghi chú ranh giới (trường `next_level_note_vi`), không phát triển nội dung.

## 4. Chuẩn đầu ra CEFR A1

Danh mục can-do đầy đủ nằm ở [`content/a1/cefr-a1.yaml`](../../../content/a1/cefr-a1.yaml) (20 mã). Mỗi bài học tham chiếu các mã này.

| Kỹ năng | Mã | Người học có thể… |
|---|---|---|
| **Nghe** | A1.H1 | nhận ra từ quen thuộc và cụm từ rất cơ bản về bản thân, gia đình, môi trường xung quanh (nói chậm, rõ) |
| | A1.H2 | hiểu câu hỏi, chỉ dẫn ngắn nói chậm và làm theo |
| | A1.H3 | nhận ra số, số điện thoại, giá tiền, giờ, ngày trong tuần |
| | A1.H4 | nắm thông tin cụ thể (ai, ở đâu, khi nào, cái gì) trong hội thoại/thông báo rất ngắn |
| **Đọc** | A1.L1 | hiểu tên, từ quen thuộc, câu rất đơn giản (biển báo, áp phích, danh thiếp) |
| | A1.L2 | hiểu tin nhắn, thiệp, email ngắn đơn giản |
| | A1.L3 | tìm thông tin cụ thể trong biểu mẫu, thông báo, quảng cáo, lịch, thực đơn |
| | A1.L4 | làm theo chỉ dẫn viết ngắn, đơn giản |
| **Nói – tương tác** | A1.SI1 | chào hỏi, giới thiệu, cảm ơn, xin lỗi; phân biệt du/Sie |
| | A1.SI2 | hỏi và trả lời về thông tin cá nhân |
| | A1.SI3 | giao tiếp khi người đối diện nói chậm và giúp đỡ; biết báo là chưa hiểu |
| | A1.SI4 | yêu cầu/đưa đồ vật; xử lý số lượng, giá, thời gian |
| | A1.SI5 | hỏi – đáp đơn giản trong tình huống nhu cầu tức thời (hẹn, đường đi, sức khỏe, mua sắm) |
| **Nói – độc thoại** | A1.SP1 | giới thiệu bản thân, nơi sống, người quen |
| | A1.SP2 | nói về công việc, sở thích, thói quen, gia đình bằng câu đơn giản |
| | A1.SP3 | phát âm đủ rõ để được hiểu (dù còn cố gắng) |
| **Viết** | A1.S1 | điền biểu mẫu thông tin cá nhân |
| | A1.S2 | viết câu đơn giản về bản thân và người khác |
| | A1.S3 | viết tin nhắn, bưu thiếp, email ngắn |
| | A1.S4 | chép chính xác từ quen thuộc; đánh vần và viết đúng thông tin cá nhân |

**Không đưa vào chuẩn đầu ra A1** (thuộc A2+): hiểu hội thoại tốc độ tự nhiên; kể chuyện quá khứ chi tiết; viết văn bản có liên kết bằng câu phụ (weil, dass…); diễn đạt ý kiến có lập luận.

## 5. Cấu trúc chương trình

```
Einstieg (nhập môn, 4 bài – bổ sung)
 └─ Kapitel 1–3 → Plattform 1
 └─ Kapitel 4–6 → Plattform 2
 └─ Kapitel 7–9 → Plattform 3
 └─ Kapitel 10–12 → Plattform 4
 └─ Abschlusstest A1 (đánh giá tổng kết)
```

- **Einstieg** – bổ sung, không thuộc giáo trình: chữ cái, phát âm, trọng âm/ngữ điệu, câu đầu tiên.
- **Kapitel** – theo đúng tên và trình tự của Netzwerk neu A1; mỗi Kapitel gồm 4–6 bài (theo các mục của giáo trình) và 1 bài *Kurz und klar – Test*.
- **Plattform** – ôn tập sau mỗi 3 Kapitel, gồm luyện dạng đề thi A1.
- **Abschlusstest A1** – đánh giá 4 kỹ năng, không chỉ dựa vào điểm trung bình (xem [a1-assessment-spec.md](a1-assessment-spec.md)).

Chi tiết từng Kapitel: [netzwerk-neu-a1-mapping.md](netzwerk-neu-a1-mapping.md). Lộ trình và thời lượng: [a1-learning-roadmap.md](a1-learning-roadmap.md).

## 6. Nguyên tắc biên soạn

1. **Tiếng Việt trước:** giải thích, đề bài, đáp án và lời giải bằng tiếng Việt; thuật ngữ tiếng Đức luôn kèm giải thích.
2. **Không sao chép giáo trình:** Netzwerk neu A1 chỉ dùng để xác định trình tự, chủ đề, phạm vi ngữ pháp/từ vựng và mục tiêu giao tiếp. Hội thoại, bài đọc, bài tập, đáp án, audio đều tự biên soạn. Video (Film „Die Netzwerk-WG“) và audio gốc không được sử dụng.
3. **Danh từ luôn có mạo từ và số nhiều.** Không dạy danh từ trần.
4. **Mỗi từ được dạy mới đúng một lần** (ở bài đầu tiên xuất hiện); các bài sau tham chiếu lại để ôn.
5. **Không vượt phạm vi:** ví dụ chỉ dùng từ/ngữ pháp đã học; nếu buộc phải dùng từ mới thì có bản dịch hoặc chú thích.
6. **Mỗi bài tập kiểm tra một mục tiêu cụ thể** (trường `objectives`); mỗi mục tiêu có ít nhất một bài tập.
7. **Mọi đáp án có giải thích** (trường `explanation_vi` bắt buộc).
8. **Dữ liệu dùng trực tiếp được:** nội dung ở dạng YAML/CSV có schema, được kiểm tra tự động.

## 7. Trạng thái

| Phần | Trạng thái |
|---|---|
| Nghiên cứu Netzwerk neu A1 (12 Kapitel, 4 Plattform) | ✅ Đã xác minh từ tài liệu chính thức của Klett |
| Chuẩn đầu ra CEFR A1 (`cefr-a1.yaml`) | ✅ |
| Schema nội dung | ✅ |
| Einstieg (4 bài) | ✅ Sẵn sàng |
| Kapitel 1 (5 bài + Test) | ✅ Sẵn sàng |
| Kapitel 2 (6 bài + Test) | ✅ Sẵn sàng |
| Kapitel 3 (6 bài + Test) | ✅ Sẵn sàng |
| Plattform 1 (3 bài) | ✅ Sẵn sàng |
| Kapitel 4–12, Plattform 2–4, Abschlusstest | ⏳ Kế hoạch (đã có đặc tả) |

Chi tiết: [phase-1-report.md](phase-1-report.md).
