from sarvamai import SarvamAI

client = SarvamAI(
    api_subscription_key="sk_09nr8orj_Rxmx396rV9Dfz31A4ak8kRFP"
)

response = client.speech_to_text.transcribe(
    file=open("sarvam_output.wav", "rb"),
    model="saaras:v3",
    mode="transcribe"
)
print(response.transcript)
print(response.language_code)