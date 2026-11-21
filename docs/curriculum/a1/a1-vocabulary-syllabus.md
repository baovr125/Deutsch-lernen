# A1 Vocabulary Syllabus – Danh mục từ vựng A1

> Dữ liệu: `content/a1/vocabulary/<NN>-<slug>.csv`, schema [`vocabulary-row.schema.json`](../../../content/_schemas/vocabulary-row.schema.json). Cập nhật: 2026-11-21.

## 1. Nguyên tắc

1. **Phạm vi theo giáo trình:** từ vựng mỗi Kapitel được xác định từ *Kapitelwortschatz Netzwerk neu A1* (Klett). Nghĩa tiếng Việt, câu ví dụ, phiên âm IPA và ghi chú cách dùng là **tự biên soạn**.
2. **Danh từ luôn có mạo từ và số nhiều.** Cột `article` bắt buộc với `pos=noun`. Danh từ không có số nhiều ghi `—` và tag `sg-only`; chỉ dùng ở số nhiều thì tag `pl-only`.
3. **Mỗi từ được dạy mới đúng một lần** (`lesson` = bài dạy mới). Các bài sau đưa ID vào `vocabulary.review`. Validator báo lỗi nếu một từ bị dạy mới hai lần, hoặc được “ôn” trước khi được dạy.
4. **Từ nhiều nghĩa** có tag `mehrdeutig` và ghi rõ các nghĩa trong `meaning_vi`/`usage_vi` (ví dụ: *bitte, Frau, Punkt, Partner, Reiseführer*).
5. **Câu ví dụ trong phạm vi:** chỉ dùng từ và ngữ pháp đã học, trừ khi có bản dịch hoặc chú thích.
6. **Tên riêng (nước, ngôn ngữ)** dùng `pos=name`; tên nước có mạo từ ghi vào `article` và tag `mit-artikel`.

## 2. Phân loại nguồn (`source`)

| Giá trị | Ý nghĩa | Ưu tiên học |
|---|---|---|
| `nwn-lern` | Có trong Lernwortschatz (từ in đậm) của Kapitel tương ứng | **Bắt buộc** – học chủ động (nói, viết) |
| `nwn` | Có trong danh sách Kapitelwortschatz nhưng không in đậm | Hiểu khi gặp (đọc, nghe) |
| `supplement` | Bổ sung cho người Việt tự học (ví dụ: *Vietnam, Vietnamesisch, Handy, Freut mich!*) | Hữu ích; không thuộc đánh giá bắt buộc |

## 3. Định dạng CSV

```
id, unit, lesson, lemma, article, plural, pos, forms, ipa, meaning_vi,
example_de, example_vi, usage_vi, level, tags, source
```

- `pos`: noun · name · verb · adj · adv · pron · art · prep · conj · num · q-word · particle · interj · phrase
- `forms`: dạng cần nhớ của động từ ở thì hiện tại (ví dụ: `du sprichst, er spricht`); Partizip II được thêm khi học Perfekt (Kapitel 10).
- `ipa`: đặt trong `[ ]`, có dấu trọng âm `ˈ`.
- `tags`: phân cách bằng `;` – chủ đề (`begruessung`, `zahl`, `land`…) và đặc tính (`mehrdeutig`, `sg-only`, `mit-artikel`, `trennbar`, `unregelmaessig`).

## 4. Chủ đề từ vựng theo Kapitel

| Kapitel | Chủ đề (theo Stoffverteilungsplan) | Trạng thái | Số từ |
|---|---|---|---|
| Einstieg | Chữ cái, từ quốc tế, yêu cầu bài tập, câu giao tiếp sống còn | ✅ | 26 (11 nwn-lern, 1 nwn, 14 supplement) |
| 1 Guten Tag! | Chào hỏi, Tageszeiten, giới thiệu, Herkunft, Zahlen 0–20, Alphabet, E-Mail, Unverständnis, Länder und Sprachen | ✅ | 125 (82 nwn-lern, 29 nwn, 14 supplement) |
| 2 | Hobbys und Aktivitäten, Wochentage, Orte, Berufe, Zahlen ab 20, Formular | ⏳ | – |
| 3 | Orte in der Stadt, Richtungen, Verkehrsmittel, Wegbeschreibung, Events, Jahreszeiten, Monate | ⏳ | – |
| 4 | Lebensmittel, Geschäfte, Preise, Essen und Trinken | ⏳ | – |
| 5 | Aktivitäten am Tag, Uhrzeit, Familie, Tageszeiten, Termine, Höflichkeit, Entschuldigung | ⏳ | – |
| 6 | Freizeit, Ordinalzahlen, Monate, Einladung, Restaurant, Trinkgeld, Veranstaltungen | ⏳ | – |
| 7 | Tagesablauf und Arbeit, Büro, Medien, Briefe | ⏳ | – |
| 8 | Fitness, Gesundheit, Körper, beim Arzt | ⏳ | – |
| 9 | Zimmer, Möbel, Geräte, Wohnungsanzeigen, Farben | ⏳ | – |
| 10 | Studium, Berufe, Tagesablauf, Telefon | ⏳ | – |
| 11 | Kleidung, Geschäfte, Kaufhaus, Zeitangaben | ⏳ | – |
| 12 | Urlaub, Reisen, Stadturlaub, Wetter, Himmelsrichtungen | ⏳ | – |

**Tổng số từ A1 dự kiến:** chưa xác định chính xác – Kapitelwortschatz (53 trang, dạng ảnh) mới đọc trang 1–6. Sẽ đếm khi biên soạn từng Kapitel. Để tham chiếu: danh sách từ của kỳ thi Goethe A1 khoảng vài trăm mục; Netzwerk neu A1 có thể nhiều hơn vì gồm cả từ bị động.

## 5. Gợi ý hiển thị và ôn tập (cho frontend/SRS)

- **Màu theo giống:** der = xanh dương, die = đỏ, das = xanh lá (quy ước phổ biến trong lớp học tiếng Đức). Số nhiều luôn hiển thị kèm `die`.
- **Thẻ SRS** gồm: mặt trước (nghĩa tiếng Việt) → mặt sau (mạo từ + từ + số nhiều + IPA + audio). Với danh từ, tính là đúng **chỉ khi đúng cả mạo từ**.
- Từ `nwn-lern` vào hàng đợi SRS mặc định; `nwn`/`supplement` vào khi người học chọn.
