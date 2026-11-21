# Báo cáo Phase 1 – Nội dung A1 (đợt 1)

> ⚠️ **Đã lỗi thời (2026-11-21):** nội dung A1 đã chuyển sang **Content Standard v2** (`content/a1/modules/`, `content/a1/grammar/`). Các đường dẫn/định dạng cũ (`units/`, `vocabulary/*.csv`, `g-a1-*.yaml`, `validate_content.py`) không còn tồn tại. Chuẩn hiện hành: [docs/content/content-standard.md](../../content/content-standard.md). Tài liệu này giữ lại để tham khảo lịch sử và phạm vi sư phạm.


> Ngày: 2026-11-21 · Nhánh: `content/a1-phase1` · Phạm vi: chỉ A1.

## 1. Tài liệu A1 đã nghiên cứu

| Tài liệu | Kết quả |
|---|---|
| Stoffverteilungsplan Netzwerk neu A1.1 (Klett, © 2023) | Đọc đủ 21/21 trang – cấu trúc Kapitel 1–6, Plattform 1–2 |
| Stoffverteilungsplan Netzwerk neu A1.2 (Klett, © 2023) | Đọc 20/21 trang – Kapitel 7–12, Plattform 3–4 (trang 20 chưa đọc) |
| Kapitelwortschatz Netzwerk neu A1 (Klett, © 2019) | Đọc trang 1–6/53 (toàn bộ Kapitel 1) |
| Trang sản phẩm Netzwerk neu A1.1 (Klett) | Tác giả, ISBN |
| CEFR 2001 (Table 1–2), CEFR Companion Volume 2020 | Chuẩn đầu ra → `content/a1/cefr-a1.yaml` (20 mã) |
| Goethe-Zertifikat A1 – Durchführungsbestimmungen | Đối chiếu cấu trúc đề A1 cho bài đánh giá tổng kết |

Nguồn và đường dẫn: [netzwerk-neu-a1-mapping.md §1](netzwerk-neu-a1-mapping.md#1-nguồn-đã-nghiên-cứu).

## 2. Phiên bản giáo trình

**Netzwerk neu A1** – Ernst Klett Sprachen; Dengler, Mayr-Sieber, Rusch, Schmitz; A1.1 ISBN 978-3-12-607161-1, A1.2 ISBN 978-3-12-607169-7.
Đơn vị bài gọi là **Kapitel**; 12 Kapitel + 4 Plattform. Năm in của sách chưa xác minh.

## 3. Danh sách Kapitel đã xác minh

1 Guten Tag! · 2 Freunde, Kollegen und ich · 3 In Hamburg · *Plattform 1* · 4 Guten Appetit! · 5 Alltag und Familie · 6 Zeit mit Freunden · *Plattform 2* · 7 Arbeitsalltag · 8 Fit und gesund · 9 Meine Wohnung · *Plattform 3* · 10 Studium und Beruf · 11 Die Jacke gefällt mir! · 12 Ab in den Urlaub! · *Plattform 4*

Mỗi Kapitel đã xác minh: tên các mục, Sprachhandlungen, Grammatik, chủ đề Wortschatz, Aussprache, Strategie.

## 4. Tài liệu đã tạo trong `docs/`

`docs/curriculum/a1/`: README · a1-curriculum-overview · netzwerk-neu-a1-mapping · a1-learning-roadmap · a1-grammar-syllabus · a1-vocabulary-syllabus · a1-lesson-content-spec · a1-assessment-spec · a1-self-study-guide · phase-1-report. Cập nhật mục lục `docs/README.md`.

## 5. Nội dung đã tạo trong `content/`

| Đường dẫn | Nội dung |
|---|---|
| `content/_schemas/*.schema.json` (7 file) | Schema cho course, unit, lesson, grammar topic, vocabulary row, CEFR, kiểu dùng chung. Dùng được cho mọi cấp độ; không tạo dữ liệu cho cấp độ khác |
| `content/a1/course.yaml` | Lộ trình A1 đầy đủ (Einstieg, 12 Kapitel, 4 Plattform, Abschlusstest) kèm trạng thái |
| `content/a1/cefr-a1.yaml` | 20 mã can-do A1 |
| `content/a1/units/00-einstieg/` | Nhập môn: 4 bài |
| `content/a1/units/01-guten-tag/` | Kapitel 1: 5 bài + Kurz und klar – Test |
| `content/a1/grammar/` | 6 chủ điểm ngữ pháp |
| `content/a1/vocabulary/` | `00-einstieg.csv`, `01-guten-tag.csv` |
| `content/README.md` | Cập nhật quy ước (cột CSV, schema, quy tắc bản quyền) |

**Thay đổi cấu trúc nhỏ:** thư mục mẫu `content/a1/units/01-begruessung/` (chỉ chứa `audio/.gitkeep`) được đổi tên thành `01-guten-tag/` cho khớp tên Kapitel 1 đã xác minh.

## 6. Thống kê

| Hạng mục | Số lượng |
|---|---|
| Unit | 2 (Einstieg, Kapitel 1) |
| Bài học | 9 (4 nhập môn + 5 Kapitel 1) + 1 bài tổng kết/kiểm tra |
| Chủ điểm ngữ pháp | 6 |
| Từ vựng | 151 (Einstieg 26, Kapitel 1 125) – trong đó 93 thuộc Lernwortschatz giáo trình, 30 có trong danh sách giáo trình, 28 bổ sung |
| Redemittel | 38 (mỗi mục có hội thoại mẫu) |
| Mục phát âm | 21 |
| Khối kỹ năng | 12 nghe · 10 đọc · 10 nói · 10 viết |
| Bài tập | 109 (95 trong bài học + 14 trong chủ điểm ngữ pháp), 294 câu hỏi, 10 dạng |
| Thời lượng | Einstieg ~220 phút · Kapitel 1 ~435 phút |

## 7. Kết quả kiểm tra chất lượng

| Kiểm tra | Kết quả |
|---|---|
| Hợp lệ theo schema (mọi YAML, mọi dòng CSV) | ✅ 0 lỗi, 0 cảnh báo |
| Tham chiếu chéo (unit/lesson/course, từ vựng new/review theo thứ tự, ngữ pháp, CEFR, prerequisites) | ✅ |
| Mỗi từ dạy mới đúng 1 lần; không ôn từ chưa học | ✅ |
| Danh từ có mạo từ + số nhiều, viết hoa; IPA có trong `[ ]` | ✅ |
| Bài tập: đáp án nằm trong lựa chọn, số chỗ trống khớp đáp án, tokens khớp câu, mỗi mục tiêu có bài tập, mọi câu có giải thích | ✅ |
| Soát toàn bộ câu tiếng Đức (trích ~1.300 chuỗi) | ✅ Đã sửa 1 câu không tự nhiên (bài nghe khách sạn) |
| Không sao chép nội dung giáo trình | ✅ Hội thoại, bài đọc, bài tập, đáp án tự viết; Film và audio gốc không dùng |
| Không có thay đổi ở `a2/`–`c2/`, `content/grammar/` | ✅ |

Validator hiện là script ngoài repo (Python, dùng PyYAML + jsonschema có sẵn trên máy); chưa đưa vào repo vì tooling của dự án chưa được khởi tạo.

## 8. Phần chưa hoàn thiện / chưa xác minh

1. **Kapitel 2–12, Plattform 1–4, Abschlusstest:** mới có đặc tả và phạm vi, chưa có nội dung bài học.
2. **Lernwortschatz Kapitel 1 chưa phủ hết:** khoảng 29 mục in đậm chưa có trong CSV – chủ yếu là từ trong yêu cầu bài tập (*sammeln, notieren, raten, ergänzen*…), các từ “di cư” ở trang mở đầu (*Kindergarten, Autobahn, Koffer…*) và một số từ chức năng (*ein/eine, kennen, machen, spielen, dann, zuerst, man, über*). Cần quyết định: bổ sung vào Kapitel 1 hay dạy ở Kapitel sau, nơi chúng được dùng chủ động (ví dụ *ein/eine* ở Kapitel 3).
3. **Kapitelwortschatz trang 7–53** chưa đọc; **Stoffverteilungsplan A1.2 trang 20** chưa đọc.
4. Mục „Der Weg zum Job“ (Kapitel 10): chủ điểm ngữ pháp cụ thể chưa xác minh (cột trống trong Stoffverteilungsplan).
5. **Audio:** mọi bài nghe ở trạng thái `pending-tts` – chưa có file âm thanh.
6. **Chưa có người bản ngữ duyệt** nội dung tiếng Đức. Nội dung đã được tự soát, nhưng nên có người bản ngữ hoặc giáo viên đọc lại trước khi phát hành rộng.
7. Mã CEFR chưa dùng ở đợt này (sẽ dùng ở các Kapitel sau): A1.H4, A1.L2, A1.S3, A1.SI5, A1.SP2.

## 9. Vấn đề cần bạn review

1. **Định dạng bài học:** hãy đọc thử `units/01-guten-tag/lesson-01.yaml` (hoặc học thử khi có giao diện) – độ dài, mức giải thích, số bài tập có phù hợp không? Cần chốt trước khi biên soạn 11 Kapitel còn lại.
2. **Vị trí thư mục ngữ pháp:** `content/a1/grammar/` (đề xuất hiện tại) hay `content/grammar/` dùng chung?
3. **Lernwortschatz còn thiếu của Kapitel 1** (mục 8.2): bổ sung ngay hay dời sang Kapitel sau?
4. **Ngưỡng đánh giá:** mỗi kỹ năng ≥ 60%, mục tiêu bài ≥ 70%, kết luận A1 cần đồng thời 4 điều kiện ([a1-assessment-spec.md](a1-assessment-spec.md)) – có phù hợp không?
5. **Tài liệu bổ sung:** nếu bạn có Kursbuch/Übungsbuch Netzwerk neu A1 (bản in hoặc PDF), việc đối chiếu sẽ chính xác hơn – đặc biệt các trang „kurz und klar“.
6. **Validator:** có muốn đưa script kiểm tra vào repo ngay (Python) hay chờ tooling TypeScript?

## 10. Đề xuất bước tiếp theo để hoàn thiện A1

1. Bạn học thử Einstieg + Kapitel 1 và góp ý định dạng.
2. Chốt các điểm ở §9.
3. Biên soạn tiếp theo khối: **Kapitel 2 → 3 → Plattform 1**, rồi kiểm tra; lặp lại cho Khối 2–4.
4. Biên soạn Abschlusstest A1 (2 phiên bản đề).
5. Tạo audio TTS cho các khối nghe khi ai-service/TTS sẵn sàng.
6. Nhờ người bản ngữ duyệt nội dung theo từng khối.

Phase 2 (A2) **chưa bắt đầu** và chỉ bắt đầu khi bạn đã trải nghiệm và đánh giá A1.

---

## Cập nhật đợt 2 – Khối 1 hoàn chỉnh (Kapitel 2, Kapitel 3, Plattform 1)

> Ngày: 2026-11-21 · Nhánh: `content/a1-phase1`

**Nghiên cứu thêm:** Kapitelwortschatz trang 7–16 (Kapitel 2–3). Phát hiện: Kapitelwortschatz không có mục riêng cho Plattform.

**Nội dung mới:**

| Phần | Bài | Ngữ pháp | Từ vựng | Bài tập |
|---|---|---|---|---|
| Kapitel 2 – Freunde, Kollegen und ich | 6 + Test | verben-praesens, ja-nein-frage, bestimmter-artikel, plural, haben-sein | 182 | 68 |
| Kapitel 3 – In Hamburg | 6 + Test | unbestimmter-artikel, negation-kein, imperativ-sie | 113 | 61 |
| Plattform 1 | 3 | – | 7 | 22 |

**Tổng sau đợt 2:** 5 unit · 24 bài học + 3 bài kiểm tra · 14 chủ điểm ngữ pháp · 453 từ · 277 bài tập (709 câu hỏi) · phủ đủ **20/20** mã CEFR A1 · validator **0 lỗi, 0 cảnh báo**.

**Điều chỉnh so với đợt 1:**
- Từ Kapitel 2, đưa **toàn bộ Lernwortschatz** (từ in đậm) vào danh sách học; các từ Lernwortschatz còn thiếu của Kapitel 1 được dạy ở Kapitel phù hợp (spielen, machen, kennen, Wort → Kapitel 2; ein/eine, dann, zuerst → Kapitel 3; bekannt → Plattform 1). Danh sách còn lại ghi trong a1-vocabulary-syllabus.md.
- Schema mở rộng (không phá vỡ dữ liệu cũ): `unit.kind` thêm `plattform`; `source` chấp nhận `plattform: 1–4` thay cho `kapitel`.
- Thư mục Plattform đặt tên `03-plattform-1` để đứng ngay sau Kapitel 3 mà vẫn giữ số thư mục trùng số Kapitel.
- Soát tiếng Đức: sửa 3 chỗ (tránh „Ich bin nicht Arzt“ khi chưa học kein; đổi „Platz“ → „Tennisplatz“ để tránh nhầm nghĩa; bỏ câu dịch dùng từ chưa học).

**Còn lại:** Kapitel 4–12, Plattform 2–4, Abschlusstest A1; audio TTS; người bản ngữ duyệt.
