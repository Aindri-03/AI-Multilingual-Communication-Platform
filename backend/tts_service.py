from gtts import gTTS

def text_to_speech(text, language):

    tts = gTTS(
        text=text,
        lang=language
    )

    tts.save("output.mp3")

    return "output.mp3"