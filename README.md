docker push manojg914822/gen_ai:tagname
# Groq Language Translator
A Streamlit app that translates text with the Groq API and optionally
generates speech using Groq's supported text-to-speech models.
## Features- Source and target language selection- Translation through Groq chat completions- Optional speech generation for supported output voices- Streamlit interface- Docker support- GitHub Actions CI
## Requirements- Python 3.11+- Groq API key- Docker Desktop (optional)
## Local setup (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Create `.env` in the project root:
GROQ_API_KEY=your_key
GROQ_MODEL=openai/gpt-oss-120b
GROQ_TTS_MODEL=canopylabs/orpheus-v1-english
Run:
python -m streamlit run src/app.py
## Docker
docker build -t groq-language-translator .
docker run --rm -p 8501:8501 --env-file .env groq-language-translator
## Security
Never commit `.env` or paste API keys into source code.
## TTS limitation
Speech output depends on the languages and voices supported by the selected
Groq TTS model. Translation text may work for a language whose speech output
is not supported by the configured voice. Check Groq's current API docs.