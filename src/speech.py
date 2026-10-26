import os
import tempfile

from groq import Groq

from .config import GROQ_TTS_MODEL, require_api_key

SUPPORTED_TTS_LANGUAGES = {"English"}


def text_to_speech(text: str, language: str) -> bytes:
    cleaned_text = text.strip()
    if not cleaned_text:
        raise ValueError("There is no text to speak.")
    if language not in SUPPORTED_TTS_LANGUAGES:
        raise ValueError(
            "Groq TTS in this example supports English output only. "
            "The translation text is still available."
        )

    client = Groq(api_key=require_api_key())
    result = client.audio.speech.create(
        model=GROQ_TTS_MODEL,
        voice="troy",
        input=cleaned_text[:4000],
        response_format="wav",
    )

    if hasattr(result, "write_to_file"):
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_file:
            temp_path = temp_file.name
        try:
            result.write_to_file(temp_path)
            with open(temp_path, "rb") as audio_file:
                audio_bytes = audio_file.read()
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)
        return audio_bytes

    if hasattr(result, "read"):
        audio_bytes = result.read()
        if isinstance(audio_bytes, (bytes, bytearray)):
            return bytes(audio_bytes)

    raise TypeError("Unsupported audio response from Groq API.")