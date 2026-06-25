import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Please speak...")
    audio = r.listen(source)

print("Audio captured!")

try:
    text = r.recognize_google(audio, language="en-IN")
    print("You said:", text)

except Exception as e:
    print(type(e))
    print(repr(e))