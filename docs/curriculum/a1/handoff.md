# Ghi chú bàn giao – nội dung A1 (để phiên làm việc sau tiếp tục)

> ⚠️ **Đã lỗi thời (2026-11-21):** nội dung A1 đã chuyển sang **Content Standard v2** (`content/a1/modules/`, `content/a1/grammar/`). Các đường dẫn/định dạng cũ (`units/`, `vocabulary/*.csv`, `g-a1-*.yaml`, `validate_content.py`) không còn tồn tại. Chuẩn hiện hành: [docs/content/content-standard.md](../../content/content-standard.md). Tài liệu này giữ lại để tham khảo lịch sử và phạm vi sư phạm.


> Cập nhật lần cuối: 2026-11-21 · Nhánh git: `content/a1-phase1` (chưa push lên GitHub, chưa mở PR)

## 1. Trạng thái

| Phần | Trạng thái | Thư mục |
|---|---|---|
| Einstieg | ✅ | `content/a1/units/00-einstieg` |
| Kapitel 1–3 | ✅ | `units/01-guten-tag`, `02-freunde-kollegen-und-ich`, `03-in-hamburg` |
| Plattform 1 | ✅ | `units/03-plattform-1` |
| **Kapitel 4 – Guten Appetit!** | ✅ | `units/04-guten-appetit` |
| **Kapitel 5 – Alltag und Familie** | ✅ | `units/05-alltag-und-familie` |
| **Kapitel 6 – Zeit mit Freunden** | ✅ | `units/06-zeit-mit-freunden` |
| **Plattform 2** (Kết thúc A1.1) | ✅ | `units/06-plattform-2` |
| **Kapitel 7 – Arbeitsalltag** | ⏳ **TIẾP THEO** (Bắt đầu A1.2) | `units/07-arbeitsalltag` |
| Kapitel 8–12, Plattform 3–4 | ⏳ chưa làm | |
| Abschlusstest A1 (`a1-final`) | ⏳ chưa làm – đặc tả ở `a1-assessment-spec.md §6` | |
| Audio TTS | ⏳ mọi khối nghe `pending-tts` | |

## 2. Cách làm (đã thống nhất, giữ nguyên)

- Quy trình và định dạng: `docs/curriculum/a1/a1-lesson-content-spec.md` (§7 quy trình biên soạn một Kapitel).
- Phạm vi mỗi Kapitel: `docs/curriculum/a1/netzwerk-neu-a1-mapping.md §4` (đã có đủ 12 Kapitel từ Stoffverteilungsplan).
- Từ vựng: đọc **Kapitelwortschatz** của Kapitel → đưa **toàn bộ từ in đậm** (Lernwortschatz) vào CSV, trừ từ chỉ dùng trong đề bài (ghi vào `not_covered_vi` của unit). Nghĩa/ví dụ/IPA tự viết.
- Mỗi Kapitel: 1 bài/1 mục của giáo trình (gộp mục nhỏ nếu cần) + `review.yaml`. Mỗi bài ≥ 5 dạng bài tập, mọi câu có `explanation_vi`, mọi objective có bài tập.
- Ngữ pháp: một file `content/a1/grammar/g-a1-<id>.yaml` cho mỗi chủ điểm; ID dự kiến ở `a1-grammar-syllabus.md`.
- Trong YAML **không dùng `""` kiểu CSV** – dùng “ ” hoặc „ “ cho ngoặc kép bên trong chuỗi.
- Tên Plattform: `NN-plattform-X` với NN = số Kapitel ngay trước (03-plattform-1, 06-plattform-2…).
- Sau mỗi Kapitel: chạy validator (0 lỗi) → soát câu tiếng Đức bằng `extract_de.py` → cập nhật `course.yaml` (dir + status: ready) → cập nhật roadmap/syllabus/mapping/report → commit.
- Không làm A2+. Không sao chép văn bản giáo trình.

## 3. Việc đang dở (cập nhật sau mỗi bước)

**Kapitel 4 – Guten Appetit!** (ĐÃ HOÀN THÀNH ✅)
- [x] Đọc Kapitelwortschatz Kapitel 4 (trang 17-21)
- [x] `vocabulary/04-guten-appetit.csv` (140 từ vựng)
- [x] Ngữ pháp: `g-a1-akkusativ`, `g-a1-moechten-moegen`, `g-a1-satzpositionen`
- [x] Bài học: l01 Guten Appetit! · l02 Kommt ihr? · l03 Einkaufen im Supermarkt · l04 Die Grillparty · l05 Frühstück, Mittagessen, Abendessen · l06 Wörter lernen + Berufe rund ums Essen · review
- [x] unit.yaml, course.yaml, tài liệu, validator 0 lỗi

**Kapitel 5 – Alltag und Familie** (ĐÃ HOÀN THÀNH ✅)
- [x] Đọc Kapitelwortschatz Kapitel 5
- [x] Soạn `vocabulary/05-alltag-und-familie.csv` (110 từ vựng duy nhất)
- [x] Ngữ pháp: `g-a1-zeitangaben-wann`, `g-a1-possessivartikel`, `g-a1-modalverben`
- [x] Bài học: l01 Mein Alltag · l02 Wie spät ist es? · l03 Meine Familie und Possessivartikel · l04 Familienalltag und Termine · l05 Die Verabredung – Modalverben im Satz · l06 Termine vereinbaren und Pünktlichkeit · review Kurz und klar – Test Kapitel 5
- [x] unit.yaml, cập nhật course.yaml, validator 0 lỗi, 0 cảnh báo (703 từ vựng, 387 bài tập, 933 items)

**Kapitel 6 – Zeit mit Freunden** (ĐÃ HOÀN THÀNH ✅)
- [x] Soạn `vocabulary/06-zeit-mit-freunden.csv` (110 từ vựng duy nhất)
- [x] Ngữ pháp: `g-a1-trennbare-verben`, `g-a1-ordinalzahlen`, `g-a1-fuer-akkusativ`, `g-a1-personalpronomen-akkusativ`, `g-a1-praeteritum-haben-sein`
- [x] Bài học: l01 Freizeitaktivitäten · l02 Eine Geburtstagsparty · l03 Geschenke und Einladungen · l04 Im Restaurant · l05 Wie war das Wochenende? · l06 Veranstaltungen und Kneipenkultur · review Kurz und klar – Test Kapitel 6
- [x] unit.yaml, validator 0 lỗi

**Plattform 2 – Ôn tập 2 (Kapitel 4–6) & Luyện thi A1** (ĐÃ HOÀN THÀNH ✅ - Kết thúc A1.1)
- [x] `vocabulary/06-plattform-2.csv` (6 từ vựng bổ trợ văn hóa D-A-CH)
- [x] Bài học: l01 Wiederholen und trainieren · l02 Landeskunde: Essen und Feste in D-A-CH · l03 Prüfungstraining: Lesen Teil 1, Schreiben Teil 1, Sprechen Teil 2
- [x] unit.yaml, cập nhật course.yaml, validator 0 lỗi, 0 cảnh báo (9 units, 45 lessons, 6 reviews, 25 grammar topics, 819 từ vựng, 468 bài tập, 1103 items)

**Kapitel 7 – Arbeitsalltag** (VIỆC TIẾP THEO ⏳ - Mở đầu A1.2)
- [ ] Đọc Kapitelwortschatz Kapitel 7
- [ ] Soạn `vocabulary/07-arbeitsalltag.csv`
- [ ] Ngữ pháp K07: Modalverben im Beruf / Dativ / Präpositionen mit Dativ
- [ ] Soạn 6 bài học + 1 bài review cho Kapitel 7
- [ ] unit.yaml, cập nhật course.yaml, validator 0 lỗi

## 4. Tài liệu nguồn (tải lại nếu cần – không lưu trong repo vì bản quyền)

- Stoffverteilungsplan A1.1: https://www.klett-sprachen.de/downloads/31495/netzwerk-neu-a1-1-stoffverteilungsplan/pdf
- Stoffverteilungsplan A1.2: https://www.klett-sprachen.de/downloads/31496/netzwerk-neu-a1-2-stoffverteilungsplan/pdf
- Kapitelwortschatz A1 (53 trang, ảnh scan): https://www.klett-sprachen.de/downloads/22483/netzwerk-neu-a1-kapitelwortschatz-kapitel-1-12/pdf
  - Trang đã đọc: 1–16 (Kapitel 1–3). Kapitel 4 bắt đầu ở trang 17.
- PDF là ảnh scan: dùng `scripts/content-tools/render_pdf.py` để chuyển trang thành PNG rồi đọc ảnh.

## 5. Câu hỏi còn chờ người dùng trả lời

1. Push nhánh `content/a1-phase1` và mở Pull Request?
2. Vị trí thư mục ngữ pháp: giữ `content/a1/grammar/` (đang dùng) hay chuyển sang `content/grammar/`?
3. Ngưỡng đánh giá (mỗi kỹ năng ≥ 60%, mục tiêu bài ≥ 70%) có phù hợp không?
4. Có tài liệu Kursbuch/Übungsbuch để đối chiếu không?
