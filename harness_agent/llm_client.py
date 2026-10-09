import requests

def local_llm_call(prompt: str) -> dict:
    url = "http://127.0.0.1:1234/v1/chat/completions"
    payload = {
        "model": "local-model",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3
    }
    res = requests.post(url, json=payload)
    return res.json()["choices"][0]["message"]["content"]
