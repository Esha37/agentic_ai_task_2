import requests

url = "http://localhost:11434/api/generate"

data = {
    "model": "gemma3:4b",
    "prompt": "Give me 3 simple ideas for an AI project.",
    "stream": False
}

response = requests.post(url, json=data )

print("Status code:", response.status_code)

result = response.json()

print("\nGemma response:\n")
print(result["response"])
