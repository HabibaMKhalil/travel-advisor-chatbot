import requests
import json

url = "http://localhost:11434/api/generate"

payload = {
    "model": "phi:latest",
    "prompt": "Is France safe for tourists? Answer briefly.",
    "stream": False
}

response = requests.post(url, json=payload)

print("Status:", response.status_code)
print("Raw response:")
print(response.text)

if response.status_code == 200:
    data = response.json()
    print("\nMODEL ANSWER:")
    print(data.get("response", "No response"))
