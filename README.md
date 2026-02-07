# LLM Wrapper

Minimal wrapper around an LLM client with retry and logging helpers.

Features:

- Simple client interface.
- Config-driven defaults.
- Retry with backoff.
- Structured logging.

Project Structure:

- `config.py`: configuration values.
- `llm_client.py`: LLM client wrapper.
- `retry.py`: retry utilities.
- `logger.py`: logging setup.
- `main.py`: example entry point.

Setup:

1. Create and activate a virtual environment.
2. Install dependencies (if any).

Requirements:

- openai
- python-dotenv

Example (macOS/Linux):

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Usage:
Run the example entry point:

```bash
python main.py
```

Notes:

- Update `config.py` with your API keys and model settings.
- If there is no `requirements.txt`, install the packages you use manually.
