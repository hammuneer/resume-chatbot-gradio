# Resume Chatbot

An AI-powered chatbot, built with [Gradio](https://www.gradio.app/) and the OpenAI API, that answers
career-related questions about **Hamza Munir** grounded in his resume.

The assistant's system prompt is built at runtime by extracting text from a resume PDF, so
answers stay in sync with the source document instead of being hand-copied into the code.

## How it works

```
User message
     │
     ▼
resume_chatbot.chatbot.chat
     │  builds system prompt from data/resume.pdf (cached after first extraction)
     ▼
OpenAI Chat Completions (gpt-4o-mini, streamed)
     │
     ▼
Gradio ChatInterface (streamed token-by-token)
```

- `src/resume_chatbot/utils.py` — extracts text from the resume PDF.
- `src/resume_chatbot/prompts.py` — builds the system prompt from that text (cached with `lru_cache`).
- `src/resume_chatbot/chatbot.py` — streams a chat completion from the OpenAI API.
- `src/resume_chatbot/app.py` — wires the chat function into a Gradio `ChatInterface`.

## Getting started

### Prerequisites

- Python 3.10+
- An [OpenAI API key](https://platform.openai.com/api-keys)

### Installation

```bash
git clone https://github.com/hammuneer/resume-chatbot-gradio.git
cd resume-chatbot-gradio
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
```

### Configuration

```bash
cp .env.example .env
# then edit .env and set OPENAI_API_KEY
```

### Run

```bash
resume-chatbot
# or: python -m resume_chatbot.app
```

Gradio will print a local URL to open in your browser.

## Project structure

```
.
├── src/resume_chatbot/   # application package
│   ├── app.py             # Gradio entry point
│   ├── chatbot.py         # streaming chat completion
│   ├── prompts.py         # system prompt construction
│   └── utils.py           # PDF text extraction
├── data/resume.pdf        # source of truth for the assistant's knowledge
├── tests/                 # pytest suite
├── pyproject.toml
└── requirements.txt
```

## Testing

```bash
pytest
```

## License

See [LICENSE](LICENSE).
