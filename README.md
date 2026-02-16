# AI backend system

A minimal, production-ready wrapper for LLM interactions. Builds prompts from templates, calls an OpenRouter-backed OpenAI client, handles retries with exponential backoff, logs structured metrics, and supports structured JSON output validation.

## Key Capabilities

- Centralized LLM client with latency and retry metrics.
- Config-driven API setup (OpenRouter-compatible OpenAI client).
- Exponential backoff retry logic for transient failures.
- Prompt templates with a lightweight registry and builder.
- Optional structured output mode with validation helpers.

## Project Structure

```
.
├── main.py                          # CLI entry point
├── llm_client.py                    # Core LLM request logic
├── config.py                        # Environment-based configuration
├── retry.py                         # Exponential backoff retry logic
├── logger.py                        # Structured logger
├── requirements.txt                 # Dependencies
└── prompt_library/
    ├── registry.py                  # Template registry
    ├── builder.py                   # Prompt builder
    ├── templates/                   # Prompt template definitions
    │   ├── qa_assistant_v1
    │   ├── summarization_v1
    │   └── extraction_v1
    └── structured/
        ├── structured_output.py     # Structured prompt scaffold
        ├── generator.py             # Structured response generation
        └── validator.py             # JSON schema validation
```

## How It Works

1. `main.py` lists or selects a prompt template from the registry.
2. The template is rendered with parameters via the builder.
3. `llm_client.py` sends the prompt using the OpenAI client configured for
   OpenRouter, capturing latency and retry counts.
4. Responses are extracted and returned in a consistent dict format.
5. Optional structured output mode validates JSON-like outputs against a
   schema string.

## Setup

1. Create and activate a virtual environment.
2. Install dependencies.
3. Configure API settings in `config.py`.

### Example (macOS/Linux)

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

Run the example entry point:

```bash
python main.py
```

## Configuration

Edit `config.py` to supply:

- OpenRouter API key (used by the OpenAI client).
- Base URL for the OpenRouter-compatible endpoint.

## Prompt Templates

Templates are registered via `TemplateRegistry.register` in `registry.py` and built using `build_prompt` from `builder.py`. Each template is a `PromptTemplate` model.

| Template ID        | Purpose                     |
| ------------------ | --------------------------- |
| `qa_assistant_v1`  | Question & answer assistant |
| `summarization_v1` | Text summarization          |
| `extraction_v1`    | Information extraction      |

To list all registered templates:

```python
from prompt_library.registry import registry
print(registry.list_templates())
```

---

## Key Modules

| Module          | Responsibility                                             |
| --------------- | ---------------------------------------------------------- |
| `llm_client.py` | `generate_response` entry point, `extract_response` parser |
| `retry.py`      | `retry_with_backoff` — wraps any callable with retry logic |
| `logger.py`     | Structured `logger` instance for consistent metric logging |
| `config.py`     | Reads API key and base URL from environment                |

---

## Dependencies

- openai
- python-dotenv

## Notes

- The client returns a structured dict with `response`, `latency`, `retries`,
  and `success` to keep downstream handling consistent.
- Template registry makes it easy to add new prompt types without changing
  client logic.

## License

MIT
