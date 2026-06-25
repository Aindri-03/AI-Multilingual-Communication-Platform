from sarvamai import SarvamAI

client = SarvamAI(
    api_subscription_key="sk_09nr8orj_Rxmx396rV9Dfz31A4ak8kRFP"
)

def speech_to_text(audio_file):
    response = client.speech_to_text.transcribe(
        file=open(audio_file, "rb"),
        model="saaras:v3",
        mode="transcribe"
    )

    return response.transcript