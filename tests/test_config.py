import pytest


def test_default_model_is_not_empty():
    from src.config import GROQ_MODEL

    assert isinstance(GROQ_MODEL, str)
    assert GROQ_MODEL.strip()


def test_tts_rejects_blank_text():
    from src.speech import text_to_speech

    with pytest.raises(ValueError, match="There is no text to speak"):
        text_to_speech("   ", "English")


def test_tts_rejects_unsupported_language():
    from src.speech import text_to_speech

    with pytest.raises(ValueError, match="English output only"):
        text_to_speech("hello", "Kannada")