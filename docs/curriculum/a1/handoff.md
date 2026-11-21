# Ghi chú bàn giao – nội dung A1 (để phiên làm việc sau tiếp tục)

> Cập nhật lần cuối: 2026-11-21 · Nhánh git: `content/a1-phase1` (chưa push lên GitHub, chưa mở PR)

## 1. Trạng thái

| Phần | Trạng thái | Thư mục |
|---|---|---|
| Einstieg | ✅ | `content/a1/units/00-einstieg` |
| Kapitel 1–3 | ✅ | `units/01-guten-tag`, `02-freunde-kollegen-und-ich`, `03-in-hamburg` |
| Plattform 1 | ✅ | `units/03-plattform-1` |
| **Kapitel 4 – Guten Appetit!** | ⏳ **ĐANG LÀM** – xem §3 | `units/04-guten-appetit` |
| Kapitel 5 – Alltag und Familie | ⏳ chưa làm | `units/05-alltag-und-familie` |
| Kapitel 6 – Zeit mit Freunden | ⏳ chưa làm | `units/06-zeit-mit-freunden` |
| Plattform 2 | ⏳ chưa làm | `units/06-plattform-2` |
| Kapitel 7–12, Plattform 3–4 | ⏳ chưa làm | |
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

**Kapitel 4 – Guten Appetit!**
- [ ] Đọc Kapitelwortschatz Kapitel 4 (bắt đầu ở trang 17 của PDF Kapitelwortschatz)
- [ ] `vocabulary/04-guten-appetit.csv`
- [ ] Ngữ pháp: `g-a1-akkusativ`, `g-a1-moechten-moegen`, `g-a1-satzpositionen`
- [ ] Bài học: l01 Guten Appetit! (Lebensmittel, Geschäfte) · l02 Kommt ihr? (Akkusativ, Umlaute) · l03 Einkaufen im Supermarkt (Preise) · l04 Die Grillparty (möchten, Beim Essen) · l05 Frühstück, Mittagessen, Abendessen (mögen, Positionen im Satz) · l06 Wörter lernen + Berufe rund ums Essen (Strategie) · review
- [ ] unit.yaml, course.yaml, tài liệu, commit

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
