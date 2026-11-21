# A1 Assessment Specification – Đặc tả ôn tập và đánh giá

> Áp dụng cho A1. Dữ liệu đề bài nằm trong `exercises[]` của bài học, `review.yaml` (Kapitel) và các unit Plattform/Abschlusstest (kế hoạch).
> Phần lưu kết quả và tính toán sẽ do module `practice` và `progress` của core-service thực hiện (theo kiến trúc đã chốt). Cập nhật: 2026-11-21.

## 1. Năm tầng đánh giá

| Tầng | Ở đâu | Mục đích | Trạng thái nội dung |
|---|---|---|---|
| 1. Câu hỏi | `exercises[].items[]` | Phản hồi tức thì + giải thích | ✅ Einstieg, Kapitel 1 |
| 2. Bài học | mọi bài tập của bài | Xác định hoàn thành bài, phát hiện mục tiêu yếu | ✅ |
| 3. Kapitel | `review.yaml` (Kurz und klar – Test) | Kiểm tra 4 kỹ năng sau mỗi Kapitel | ✅ Kapitel 1 |
| 4. Plattform | `a1-p1` … `a1-p4` | Ôn 3 Kapitel + luyện dạng đề A1 | ⏳ |
| 5. Abschlusstest A1 | `a1-final` | Kết luận đạt A1 | ⏳ (đặc tả ở §6) |

Ngoài ra: **ôn từ vựng SRS** hằng ngày (Vocabulary Retention).

## 2. Chấm điểm câu hỏi

| Dạng | Cách chấm | Điểm |
|---|---|---|
| multiple-choice, true-false, matching (từng cặp), ordering, dictation | Tự động, đúng/sai | 1 điểm/câu (matching: 1 điểm/cặp) |
| gap-fill | Tự động, từng chỗ trống; chấp nhận `accept` | 1 điểm/chỗ trống |
| translation, sentence-building | Tự động: so khớp chuẩn hóa với `answer` + `accept`; không khớp → cho người học tự đánh giá có so sánh với đáp án (sau này: AI) | 1 điểm/câu |
| writing, speaking | Theo `rubric` (điểm từng tiêu chí). Hiện tại: **tự chấm** có hướng dẫn; sau này: AI chấm (ai-service) + người học xác nhận | Tổng điểm rubric |

Chuẩn hóa: xem [a1-lesson-content-spec.md §4](a1-lesson-content-spec.md#4-dạng-bài-tập). Lỗi chữ hoa ở danh từ = sai (vì đây là mục tiêu học).

## 3. Tiêu chí hoàn thành

### 3.1 Hoàn thành bài học (Lesson Completion)
- Đã xem mọi phần (từ vựng, ngữ pháp, Redemittel, 4 kỹ năng);
- Làm **tất cả** bài tập ít nhất một lần;
- **Mỗi mục tiêu `o*`** đạt ≥ 70% (tính trên các bài tập gắn mục tiêu đó);
- Bài viết và nói đã nộp (tự chấm hoặc AI chấm).

### 3.2 Hoàn thành Kapitel
- Hoàn thành mọi bài học;
- Kurz und klar – Test: **mỗi kỹ năng ≥ 60%** (từ vựng, ngữ pháp, nghe, đọc, viết, nói) **và** tổng ≥ 70%.
- Nếu một kỹ năng < 60%: Kapitel ở trạng thái „hoàn thành – cần ôn“, hệ thống đề xuất bài ôn (§5).

> **Vì sao không chỉ dùng điểm trung bình?** Một người có thể đạt 90% đọc và 30% nghe, trung bình vẫn 60%. Nền tảng yêu cầu ngưỡng **riêng cho từng kỹ năng và từng mục tiêu** để không bỏ sót điểm yếu.

## 4. Mô hình mức độ thành thạo (mastery)

Mỗi người học có các chỉ số sau (lưu trong module progress):

| Chỉ số | Cách tính | Ngưỡng |
|---|---|---|
| **Objective mastery** (theo mục tiêu bài) | Trung bình có trọng số của **3 lần làm gần nhất** các bài tập gắn mục tiêu; lần gần nhất trọng số cao nhất | Yếu < 60% · Đang học 60–79% · Vững ≥ 80% |
| **Skill score** (từ vựng, ngữ pháp, phát âm, nghe, đọc, nói, viết) | Tổng hợp mastery các mục tiêu của kỹ năng | Như trên |
| **CEFR can-do coverage** | Tỷ lệ mã `A1.*` có ≥ 1 mục tiêu „vững“ trong các bài gắn mã đó | Báo cáo tiến độ |
| **Grammar understanding** | Mastery của bài tập trong chủ điểm ngữ pháp (`g-a1-*`, mục tiêu `r*`) + bài tập `skill: grammar` trong bài học | Như trên |
| **Vocabulary retention** | Từ SRS: tỷ lệ nhớ đúng (danh từ phải đúng cả mạo từ); số từ „đến hạn“ chưa ôn | ≥ 85% nhớ đúng là tốt |
| **Listening / Reading comprehension** | Điểm các bài `skill: listening/reading` | Như trên |
| **Writing / Speaking ability** | Điểm rubric (tự chấm/AI) | Như trên |

## 5. Phát hiện điểm yếu và đề xuất ôn tập

Quy tắc (bắt đầu bằng luật, không cần AI – đúng định hướng module `recommendation`):

1. **Mục tiêu yếu** (mastery < 60%) → đề xuất làm lại các bài tập của mục tiêu đó và đọc lại phần lý thuyết liên quan (chủ điểm ngữ pháp, Redemittel).
2. **Lỗi lặp lại theo mẫu** → gắn với chủ điểm ngữ pháp, ví dụ: sai đuôi động từ ở ≥ 3 câu → đề xuất `g-a1-verben-singular`; sai `wo/woher` → `g-a1-w-fragen`.
3. **Từ vựng:** từ trả lời sai ≥ 2 lần liên tiếp → rút ngắn chu kỳ SRS; danh từ sai mạo từ → thẻ luyện mạo từ riêng.
4. **Kỹ năng < 60% ở Kapitel test** → đề xuất cụ thể: nghe → nghe lại các khối `listen` của Kapitel ở tốc độ chậm; nói → làm lại bài `speaking` với checklist.
5. **Quá hạn:** mục tiêu „yếu“ quá 14 ngày → nhắc trên dashboard; trước Abschlusstest phải hết mục tiêu yếu.

Đề xuất hiển thị bằng tiếng Việt, có lý do: *“Bạn đúng 2/6 câu về woher/wo. Hãy xem lại phần ‘Câu hỏi W-’ (5 phút) rồi làm lại bài tập 1 của bài ‘Woher kommen Sie?’.”*

## 6. Abschlusstest A1 – bản thiết kế

Cấu trúc theo dạng đề A1 quen thuộc (tương tự Goethe-Zertifikat A1: Start Deutsch 1, mà 4 Plattform của Netzwerk neu A1 luyện tập) – **đề và audio hoàn toàn tự biên soạn**:

| Phần | Nội dung | Dạng bài | Thời gian | Điểm | Ngưỡng |
|---|---|---|---|---|---|
| Hören | T1: hội thoại ngắn hằng ngày · T2: thông báo · T3: tin nhắn thoại | multiple-choice, true-false | ~20 phút | 15 | ≥ 60% |
| Lesen | T1: tin nhắn/email ngắn · T2: quảng cáo/trang web (chọn thông tin) · T3: biển báo, thông báo | true-false, multiple-choice | 25 phút | 15 | ≥ 60% |
| Schreiben | T1: điền biểu mẫu · T2: viết tin nhắn/email ngắn (~30 từ) theo 3 ý cho trước | writing | 20 phút | 15 | ≥ 60% |
| Sprechen | T1: giới thiệu bản thân · T2: hỏi – đáp theo chủ đề · T3: đề nghị/yêu cầu theo thẻ tình huống | speaking | ~15 phút | 15 | ≥ 60% |
| Wortschatz & Grammatik (bổ sung của nền tảng) | Từ vựng và ngữ pháp trọng tâm của 12 Kapitel | gap-fill, multiple-choice, ordering | 20 phút | 20 | ≥ 60% |

**Kết luận “đạt A1”** khi **đồng thời**:
1. Mỗi phần ≥ 60%;
2. Tổng ≥ 70%;
3. CEFR coverage = 20/20 mã có ít nhất một mục tiêu „vững“;
4. Vocabulary retention của từ `nwn-lern` ≥ 80%.

Nếu chưa đạt: báo cáo chi tiết theo phần và theo mã CEFR, kèm kế hoạch ôn 1–2 tuần do hệ thống đề xuất; có thể thi lại sau khi hoàn thành kế hoạch ôn.

**Ngân hàng đề:** mỗi phần cần ≥ 2 phiên bản tương đương để thi lại không trùng đề.

## 7. Plattform (ôn tập sau mỗi 3 Kapitel)

Mỗi Plattform gồm: (1) trò chơi/ôn tập tổng hợp Redemittel và từ vựng của 3 Kapitel; (2) luyện nói theo tình huống; (3) Landeskunde D-A-CH; (4) **Prüfungstraining** đúng các phần đề mà giáo trình luyện ở Plattform đó (xem [netzwerk-neu-a1-mapping.md](netzwerk-neu-a1-mapping.md)), với đề tự biên soạn.

## 8. Dữ liệu cần lưu (gợi ý cho module progress)

`attempt(user, exercise_id, item_id, response, correct, score, graded_by[auto|self|ai], created_at)` · `objective_mastery(user, lesson_id, objective_id, value, updated_at)` · `skill_score(user, level, skill, value)` · `cefr_coverage(user, code, status)` · `srs_card(user, vocab_id, due_at, interval, ease, lapses)`.
