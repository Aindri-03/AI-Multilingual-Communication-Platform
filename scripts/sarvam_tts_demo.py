import requests

API_KEY = "sk_ev0gigod_ycBU9An1TrplmfMuFxJTACth"

url = "https://api.sarvam.ai/text-to-speech"

headers = {
    "api-subscription-key": API_KEY,
    "Content-Type": "application/json"
}

payload = {
    "text": "Namaste, this is a test.",
    "target_language_code": "hi-IN"
}

response = requests.post(
    url,
    headers=headers,
    json=payload
)

print(response.status_code)
print(response.text)