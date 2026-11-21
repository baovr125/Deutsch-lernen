# ADR-0001: Kiến trúc Hybrid, gồm Modular Monolith và AI Service tách riêng

- **Trạng thái:** Đã chấp nhận
- **Ngày:** 2026-11-21

## Bối cảnh

- Nền tảng học tiếng Đức A1–C2, đội nhỏ (1–3 developer) ở giai đoạn đầu.
- Mục tiêu: dễ bảo trì, dễ phát triển lâu dài, có thể mở rộng.
- Phần lớn tải là đọc nội dung (dễ cache). Điểm nghẽn thật nằm ở **nội dung** và **AI** (độ trễ tính bằng giây, chi phí theo token, chất lượng khó kiểm soát).
- Ranh giới domain chưa được kiểm chứng bằng người dùng thật.

## Các phương án đã cân nhắc

| | A. Modular Monolith | **B. Hybrid** | C. Microservices thô (4–5 service) |
|---|---|---|---|
| Thời gian đến MVP | Nhanh nhất | Thêm khoảng 1–2 tuần | Thêm khoảng 4–6 tuần |
| Chi phí hạ tầng | Thấp | Thấp–vừa | Cao (gateway, broker, observability đầy đủ) |
| Scale phần AI riêng | Một phần (qua worker) | Có | Có |
| Deploy AI độc lập | Không | Có | Có |
| Rủi ro chia sai ranh giới | Thấp | Thấp | Cao |
| Phù hợp đội 1–3 người | Rất phù hợp | Phù hợp | Kém |

Microservices chia nhỏ theo từng nghiệp vụ đã bị loại vì: phải dùng saga và chịu eventual consistency cho những luồng vốn chỉ cần một transaction, chi phí vận hành cao, và chia sai ranh giới thì rất tốn kém khi domain chưa ổn định.

## Quyết định

Chọn **phương án B**:

- **`core-service`** là Modular Monolith (NestJS) chứa identity, curriculum, vocabulary, practice, progress, media, content-admin và ai-bridge.
- **`ai-service`** là service độc lập chứa mọi tính năng AI.

AI được tách vì nó khác phần còn lại ở cả 4 mặt:
- **Tải:** request chậm và đột biến.
- **Công nghệ:** có thể cần Python cho speech hoặc NLP sau này.
- **Rủi ro:** phụ thuộc provider bên ngoài.
- **Chu kỳ thay đổi:** prompt và model đổi liên tục.

## Hệ quả

**Tích cực**
- AI lỗi hoặc chậm thì luồng học chính không bị ảnh hưởng.
- Deploy và scale AI độc lập. Đổi provider hoặc model không động đến core.
- Có kinh nghiệm giao tiếp giữa service (contract, queue, JWT/JWKS) ở quy mô nhỏ, kiểm soát được.

**Chi phí phải chấp nhận**
- Phải duy trì contract trong `packages/contracts`, xử lý idempotent và retry cho các job giữa service.
- Cần correlation ID và tracing giữa 2 service ngay từ Phase 1.

**Việc cần làm**
- ADR-0002 (stack), ADR-0003 (ranh giới AI), ADR-0004 (giao tiếp giữa service).

## Điều kiện tách thêm service

Chỉ tách thêm khi có dấu hiệu **đo được**:

| Ứng viên | Điều kiện |
|---|---|
| `notification-service` | Có email, push và lịch nhắc phức tạp |
| `analytics-service` | Query thống kê làm chậm DB chính |
| `identity-service` | Có thêm sản phẩm hoặc app khác dùng chung tài khoản |
| Tách nhỏ `core-service` | Có đội riêng phụ trách một mảng, hoặc một module cần scale khác hẳn |

Điều kiện để việc tách dễ dàng: trong core, mỗi bảng chỉ thuộc một module và module chỉ giao tiếp qua public API hoặc event.
