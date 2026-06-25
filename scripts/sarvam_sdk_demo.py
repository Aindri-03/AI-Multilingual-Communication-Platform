from sarvamai import SarvamAI
import base64

client = SarvamAI(
    api_subscription_key="sk_09nr8orj_Rxmx396rV9Dfz31A4ak8kRFP"
)

response = client.text_to_speech.convert(
    model="bulbul:v3",
    text="Namaste, this is a test.",
    target_language_code="hi-IN",
    speaker="shubh"
)

audio_base64 = response.audios[0]

audio_bytes = base64.b64decode(audio_base64)

with open("sarvam_output.wav", "wb") as f:
    f.write(audio_bytes)

print("Audio saved successfully!")