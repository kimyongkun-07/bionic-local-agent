from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="dummy_key"
)

messages = []
print("和本地大模型对话，输入exit退出")
while True:
    user_input = input("你：")
    if user_input == "exit":
        break
    messages.append({"role":"user","content":user_input})
    resp = client.chat.completions.create(
        model="Qwen2.5 7B Instruct",
        messages=messages,
        temperature=0.7
    )
    ans = resp.choices[0].message.content
    print(f"AI：{ans}")
    messages.append({"role":"assistant","content":ans})
