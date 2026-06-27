import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import streamlit as st
from backend.translation_service import translate_text
from backend.tts_service import text_to_speech
from backend.speech_service import speech_to_text
from backend.language_service import detect_language

try:
    from streamlit_mic_recorder import mic_recorder
    has_mic_recorder = True
except Exception:
    mic_recorder = None
    has_mic_recorder = False

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI Multilingual Communication Platform",
    page_icon="🌍",
    layout="centered"
)

# ---------------- SIDEBAR ----------------

st.sidebar.title("🌍 AI Translator")

st.sidebar.info("""
Features:
- Speech To Text
- Automatic Language Detection
- Multi-language Translation
- Text To Speech
- Audio Download
""")

# ---------------- TITLE ----------------

st.title("🌍 AI Multilingual Communication Platform")

st.write(
    "Speak or enter text and translate it into another language."
)

# ---------------- LANGUAGES ----------------

languages = {
    "English": "en",
    "Hindi": "hi",
    "Bengali": "bn",
    "Tamil": "ta",
    "Telugu": "te"
}

lang_names = {
    "en": "English",
    "hi": "Hindi",
    "bn": "Bengali",
    "ta": "Tamil",
    "te": "Telugu"
}

# ---------------- SESSION STATE ----------------

if "recognized_text" not in st.session_state:
    st.session_state.recognized_text = ""

if "source_lang" not in st.session_state:
    st.session_state.source_lang = "English"

if "target_lang" not in st.session_state:
    st.session_state.target_lang = "Hindi"

# ---------------- VOICE INPUT ----------------

st.subheader("🎤 Voice Input")

if has_mic_recorder:
    try:
        audio = mic_recorder(
            start_prompt="🎤 Start Recording",
            stop_prompt="⏹ Stop Recording",
            key="recorder"
        )
    except Exception as recorder_error:
        st.error("Voice recorder is unavailable right now.")
        st.write(f"Recorder error: {recorder_error}")
        audio = None
else:
    st.warning("Voice recording is unavailable. Please use text input below.")
    audio = None

if audio:

    st.success("🎤 Voice Recorded Successfully!")

    with open("recorded_audio.wav", "wb") as f:
        f.write(audio["bytes"])

    recognized_text = speech_to_text(
        "recorded_audio.wav"
    )

    st.session_state.recognized_text = recognized_text

    detected_lang = detect_language(
        recognized_text
    )

    language_name = lang_names.get(
        detected_lang,
        "English"
    )

    if language_name in languages:
        st.session_state.source_lang = language_name

    st.subheader("📝 Recognized Speech")
    st.info(recognized_text)

    st.success(
        f"Detected Language: {language_name}"
    )

# ---------------- LANGUAGE SELECTION ----------------

st.subheader("🌐 Translation Settings")

col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox(
        "Source Language",
        list(languages.keys()),
        index=list(languages.keys()).index(
            st.session_state.source_lang
        )
    )

with col2:
    target_lang = st.selectbox(
        "Target Language",
        list(languages.keys()),
        index=list(languages.keys()).index(
            st.session_state.target_lang
        )
    )

# Save latest selections

st.session_state.source_lang = source_lang
st.session_state.target_lang = target_lang

# ---------------- SWAP BUTTON ----------------

if st.button("🔄 Swap Languages"):

    temp = st.session_state.source_lang

    st.session_state.source_lang = (
        st.session_state.target_lang
    )

    st.session_state.target_lang = temp

    st.rerun()

# ---------------- TEXT INPUT ----------------

st.subheader("✍ Enter Text")

text = st.text_area(
    "Input Text",
    value=st.session_state.recognized_text,
    height=150,
    label_visibility="collapsed"
)

# ---------------- TRANSLATE ----------------

if st.button("Translate"):

    if not text.strip():

        st.warning(
            "Please enter some text."
        )

    elif source_lang == target_lang:

        st.error(
            "Source and Target Language cannot be the same."
        )

    else:

        result = translate_text(
            text,
            languages[source_lang],
            languages[target_lang]
        )

        st.success(
            "✅ Translation Complete!"
        )

        st.subheader(
            "🌍 Translated Text"
        )

        st.write(result)

        # ---------------- TEXT TO SPEECH ----------------

        audio_file = text_to_speech(
            result,
            languages[target_lang]
        )

        st.subheader(
            "🔊 Audio Output"
        )

        st.audio(audio_file)

        with open(audio_file, "rb") as file:

            st.download_button(
                label="⬇ Download Audio",
                data=file,
                file_name="translated_audio.wav",
                mime="audio/wav"
            )