import streamlit as st

from src.speech import text_to_speech
from src.translator import translate_text

st.set_page_config(page_title="Groq Language Translator", page_icon="🌐")
st.title("Groq Language Translator")
st.write("Translate text and listen to supported speech output.")

languages = [
    "English",
    "Kannada",
    "Hindi",
    "Tamil",
    "Telugu",
    "Spanish",
    "French",
    "German",
    "Japanese",
    "Arabic",
]

source_language = st.selectbox("Source language", ["Auto"] + languages, index=0)
target_language = st.selectbox("Target language", languages, index=1)
input_text = st.text_area("Text to translate", height=160)

if st.button("Translate", type="primary"):
    if not input_text.strip():
        st.warning("Please enter text first.")
    else:
        try:
            with st.spinner("Translating with Groq..."):
                translated = translate_text(input_text, source_language, target_language)
                st.session_state["translated"] = translated
            st.session_state["target_language"] = target_language
        except Exception as exc:
            st.error(f"Translation failed: {exc}")

if st.session_state.get("translated"):
    st.subheader("Translation")
    st.text_area(
        "Translated text",
        value=st.session_state["translated"],
        height=160,
        key="translated_text_display",
    )
    if st.button("Generate audio"):
        try:
            with st.spinner("Generating audio..."):
                audio = text_to_speech(
                    st.session_state["translated"],
                    st.session_state.get("target_language", target_language),
                )
            st.audio(audio, format="audio/wav")
        except Exception as exc:
            st.warning(str(exc))