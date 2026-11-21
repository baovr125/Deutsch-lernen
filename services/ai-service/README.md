# ai-service

Service độc lập chứa **toàn bộ tính năng AI**. Quyết định: [ADR-0001](../../docs/adr/0001-hybrid-architecture.md), [ADR-0003](../../docs/adr/0003-ai-service-boundary.md).

## Cấu trúc

```text
src/
├── config/            # schema biến môi trường
├── platform/          # http, queue, observability, errors (phần dùng chung lấy từ packages/service-kit)
├── api/
│   ├── public/        # /api/v1/ai/* qua gateway — tutor chat, roleplay (SSE), xác thực JWT qua JWKS
│   └── internal/      # /internal/v1/* — chỉ cho service nội bộ
├── consumers/         # xử lý job BullMQ: ai.writing-eval.requested, ai.pronunciation.requested…
├── tasks/             # MỖI TÍNH NĂNG AI LÀ MỘT TASK: input/output schema + prompt + model profile
│   ├── tutor-chat/  roleplay/  writing-eval/  grammar-explain/  vocab-assist/  pronunciation-feedback/
├── providers/
│   ├── ports/         # LlmProvider, EmbeddingProvider, SpeechProvider
│   ├── anthropic/     # Claude — LLM
│   ├── voyage/        # embedding
│   ├── azure-speech/  # STT, TTS, chấm phát âm
│   └── mock/          # dùng cho test
├── gateway/           # router task → model, retry, fallback, timeout, theo dõi token và chi phí
├── prompt-registry/   # nạp và render prompt có version từ prompts/
├── rag/               # chunking, retriever, vector store (pgvector)
├── guardrails/        # moderation, lọc PII, chống prompt injection, validate output
├── persistence/       # repository cho DB ai
├── telemetry/         # Langfuse, usage log
└── database/migrations/
prompts/               # prompt là dữ liệu, có version — xem prompts/README.md
config/                # models.yaml: task → provider / model / fallback
evals/                 # bộ đánh giá chất lượng — xem evals/README.md
test/
```

## Sở hữu dữ liệu (DB `ai`)

conversations, messages, ai_results (kèm `task`, `promptVersion`, `model`, tokens, chi phí), usage, embeddings.

## Quy tắc

1. Chỉ `providers/` được import SDK của provider.
2. Model do `config/models.yaml` quyết định. Mặc định `claude-opus-5-5`.
3. Không truy cập DB của core. Cần ngữ cảnh người học thì gọi `GET core:/internal/v1/learners/:id/context`.
4. Đổi prompt hoặc model thì phải chạy eval.
