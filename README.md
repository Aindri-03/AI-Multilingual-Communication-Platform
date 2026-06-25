# 🌍 AI Multilingual Communication Platform

An AI-powered multilingual communication platform that enables users to communicate across different languages using Speech-to-Text, Automatic Language Detection, Translation, and Text-to-Speech technologies.

---

## 📌 Project Overview

The AI Multilingual Communication Platform helps users communicate effortlessly by converting spoken language into text, automatically detecting the language, translating it into another language, and converting the translated text back into speech.

This project combines Natural Language Processing (NLP), Speech Recognition, Machine Translation, and Text-to-Speech technologies to create a complete multilingual communication system.

---

# ✨ Features

- 🎤 Speech-to-Text Conversion
- 🌍 Automatic Language Detection
- 🔄 Real-time Language Translation
- 🔊 Text-to-Speech Audio Output
- 📥 Download Translated Audio
- 🖥️ Interactive Streamlit Interface
- ⚡ FastAPI Backend Services
- 🌐 Supports Multiple Indian Languages

---

# 🏗️ System Architecture

```
                 User
                   │
                   ▼
        Streamlit Frontend
                   │
                   ▼
            FastAPI Backend
                   │
   ┌───────────────┼───────────────┐
   │               │               │
   ▼               ▼               ▼
Speech-to-Text  Language      Translation
                Detection
                   │
                   ▼
           Text-to-Speech
                   │
                   ▼
            Audio + Text Output
```

---

# 🛠️ Technologies Used

## Frontend

- Streamlit

## Backend

- FastAPI

## Programming Language

- Python 3.12

## AI & NLP Libraries

- deep-translator
- SpeechRecognition
- langdetect
- gTTS / Sarvam AI TTS
- streamlit-mic-recorder

## APIs

- Google Translator
- Sarvam AI API

---

# 📂 Project Structure

```
AI-Multilingual-Communication-Platform
│
├── backend/
│   ├── language_service.py
│   ├── speech_service.py
│   ├── translation_service.py
│   └── tts_service.py
│
├── frontend/
│   └── app.py
│
├── scripts/
├── outputs/
├── tests/
├── app.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Aindri-03/AI-Multilingual-Communication-Platform.git
```

Move inside the project

```bash
cd AI-Multilingual-Communication-Platform
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 🔄 Workflow

1. User records speech.
2. Speech is converted into text.
3. Language is detected automatically.
4. Text is translated into the selected language.
5. Translated text is displayed.
6. Text is converted into speech.
7. User can listen or download the audio.

---

# 🚀 Future Scope

- Support 100+ languages
- Real-time conversation mode
- Video subtitle translation
- Offline translation
- AI voice cloning
- Speaker identification
- Mobile application
- Cloud deployment

---

# 👩‍💻 Contributors

**Aindri Pal**

B.Tech Computer Science and Engineering

KIIT University

---

# 📄 License

This project is licensed under the MIT License.