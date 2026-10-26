import os
from dotenv import load_dotenv
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "").strip()
GROQ_MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b").strip()
GROQ_TTS_MODEL = os.getenv(
    "GROQ_TTS_MODEL",
    "canopylabs/orpheus-v1-english",
).strip()
def require_api_key() -> str:
    """Return the key or raise a helpful configuration error."""
    if not GROQ_API_KEY:
        raise RuntimeError(
            "GROQ_API_KEY is missing. Add it to your local .env file."
        )
    return GROQ_API_KEY