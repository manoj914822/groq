from groq import Groq
from .config import GROQ_MODEL, require_api_key
def translate_text(text: str, source_language: str, target_language: str) -> str:
    text = text.strip()
    if not text:
        raise ValueError("Enter some text to translate.")
    if len(text) > 8000:
        raise ValueError("Please keep the input under 8,000 characters.")
    client = Groq(api_key=require_api_key())
    response = client.chat.completions.create(
        model=GROQ_MODEL,
        temperature=0.2,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a careful translation assistant. Translate the "
                    "user's text into the requested target language. Preserve "
                    "meaning, names, numbers, tone, and formatting. Return "
                    "only the translation. If the source language is Auto, "
                    "identify it from the text."
                ),
            },
            {
                "role": "user",
                "content": (
                    f"Source language: {source_language}\n"
                    f"Target language: {target_language}\n\n"
                    f"Text to translate:\n{text}"
                ),
            },
        ],
    )
    result = response.choices[0].message.content
    if not result:
        raise RuntimeError("Groq returned an empty translation.")
    return result.strip()