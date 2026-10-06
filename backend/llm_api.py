import requests

def call_bionic(prompt, temperature=0.7, max_tokens=512):
    url = "http://localhost:1234/v1/chat/completions"
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": "local-model",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": temperature,
        "max_tokens": max_tokens
    }
    resp = requests.post(url, headers=headers, json=payload)
    data = resp.json()
    return data["choices"][0]["message"]["content"]
