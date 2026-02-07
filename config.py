import os
from dotenv import load_dotenv

load_dotenv()

def get_openrouter_key():
    key = os.getenv("OPENROUTER_API_KEY")
    if not key:
        raise ValueError("OPENROUTER_API_KEY not found in environment variables")
    return key

def get_base_url():
    return os.getenv("OPENROUTER_BASE_URL")