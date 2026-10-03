from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="dummy_key"
)

messages = []
print("【流式对话程序】输入exit退出\n")
while True:
    user_input = input("你：")
    if user_input == "exit":
        break
    messages.append({"role":"user", "content":user_input})
    stream = client.chat.completions.create(
        model="Qwen2.5 7B Instruct",
        messages=messages,
        temperature=0.7,
        stream=True
    )
    print("AI：", end="", flush=True)
    full_ans = ""
    for chunk in stream:
        if chunk.choices and chunk.choices[0].delta.content:
            text = chunk.choices[0].delta.content
            print(text, end="", flush=True)
            full_ans += text
    print("\n")
    messages.append({"role":"assistant", "content":full_ans})
