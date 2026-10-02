from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="dummy_key"
)

response = client.chat.completions.create(
    model="Qwen2.5 7B Instruct",
    messages=[{"role": "user", "content": "介绍一下你自己"}]
)
print(response.choices[0].message.content)
