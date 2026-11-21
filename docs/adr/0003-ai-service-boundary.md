# ADR-0003: Ranh giới AI service và trừu tượng hóa provider

- **Trạng thái:** Đã chấp nhận
- **Ngày:** 2026-11-21

## Bối cảnh

Hệ thống cần đổi được LLM provider, model, prompt, embedding model và speech provider mà không ảnh hưởng nghiệp vụ. Chất lượng AI (nhất là giải thích ngữ pháp) ảnh hưởng trực tiếp đến người học, và chi phí AI phải kiểm soát được.

## Quyết định

### Phân chia trách nhiệm

| | `ai-service` | `core-service/modules/ai-bridge` |
|---|---|---|
| Biết về | Model, prompt, token, embedding, giọng nói, hội thoại AI | Người học, gói dịch vụ, quota, bài làm |
| Sở hữu dữ liệu | conversations, ai_results, usage/cost, embeddings | Trạng thái Attempt, quota |
| Không biết về | Bảng của core, quy tắc chấm điểm nghiệp vụ | Provider nào đang được dùng |

### Bảy quy tắc

1. **Gọi theo task:** mọi tính năng AI là một task trong `src/tasks/<task>` với input/output khai báo bằng zod. Không có code nào ngoài `src/providers/` được import SDK của provider.
2. **Model do config quyết định:** `config/models.yaml` ánh xạ task → provider, model, fallback và tham số. Mặc định dùng `claude-opus-5-5` cho mọi task. Việc chuyển một task sang model rẻ hơn chỉ được làm sau khi đo bằng eval.
3. **Provider tách theo năng lực:** `LlmProvider`, `EmbeddingProvider`, `SpeechProvider` được định nghĩa trong `src/providers/ports`. Có `mock/` dùng cho test.
4. **Prompt là dữ liệu có version:** `prompts/<task>/<name>.v<N>.md`. Không sửa version đã phát hành mà tạo version mới.
5. **Truy vết được:** mỗi kết quả AI lưu kèm `task`, `promptVersion`, `model`, số token và chi phí.
6. **Eval là cổng chất lượng:** đổi prompt hoặc model thì phải chạy `evals/` và không được tụt dưới ngưỡng.
7. **Guardrails:** input của người học được coi là dữ liệu (chống prompt injection). Lọc PII trước khi gửi ra ngoài. Output phải qua validate schema. Quota theo người dùng.

### Lựa chọn provider ban đầu

| Năng lực | Provider | Ghi chú |
|---|---|---|
| LLM | Anthropic Claude (SDK chính thức `@anthropic-ai/sdk`) | Structured output, streaming, prompt caching, Batch API cho việc offline. Xử lý `stop_reason: "refusal"` |
| Embedding | Voyage AI (multilingual) | Anthropic không có endpoint embedding. Lưu tên model cạnh vector; đổi model thì phải re-index |
| Speech | Azure AI Speech (STT, TTS, Pronunciation Assessment `de-DE`) | LLM chỉ diễn giải kết quả chấm phát âm |

### Thứ tự triển khai tính năng (Phase 4)

writing-eval → grammar-explain (RAG trên `content/grammar` đã duyệt) → tutor-chat (SSE) → vocab-assist (sinh sẵn qua Batch API) → roleplay (text) → pronunciation-feedback (Phase 5).

Learning recommendation **bắt đầu bằng luật** trong core. LLM chỉ dùng để diễn đạt lời khuyên.

## Hệ quả

- Đổi provider chỉ cần thêm adapter và sửa config. Nghiệp vụ không đổi.
- Phải duy trì bộ eval có dữ liệu gán nhãn. Đây là chi phí liên tục nhưng bắt buộc.
