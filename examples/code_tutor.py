import requests

# API配置
API_URL = "http://127.0.0.1:1234/v1/chat/completions"
MODEL_NAME = "bionic"

def call_llm(prompt):
    headers = {"Content-Type": "application/json"}
    data = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": "你是编程助教，面向大一学生，分析Python/C代码，找出bug，解释逻辑，最后总结知识点。"},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }
    resp = requests.post(API_URL, headers=headers, json=data)
    return resp.json()["choices"][0]["message"]["content"]

def save_note(text):
    with open("code_note.md", "w", encoding="utf-8") as f:
        f.write(text)
    print("\n✅ 笔记已保存到 code_note.md")

def read_code_file(filepath):
    """读取本地代码文件"""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"读取文件失败：{e}"

def main():
    while True:
        print("\n===== 本地编程助教（Bionic）=====")
        print("1: 手动粘贴代码 / 查bug")
        print("2: 生成编程练习题")
        print("3: 读取本地代码文件分析")
        print("0: 退出")
        select = input("请选择功能(1/2/3/0):")
        if select == "0":
            print("程序结束")
            break
        elif select == "1":
            code = input("粘贴你的代码：\n")
            res = call_llm(code)
            print("\n=====AI辅导结果=====\n", res)
            save_note(res)
        elif select == "2":
            msg = input("输入要求（例如：Python简单if练习题）：\n")
            res = call_llm(msg)
            print("\n=====AI辅导结果=====\n", res)
            save_note(res)
        elif select == "3":
            path = input("输入examples内代码文件名（如temp_test.py）：\n")
            code = read_code_file(path)
            prompt = f"分析下面代码，找bug并讲解：\n{code}"
            res = call_llm(prompt)
            print("\n=====AI辅导结果=====\n", res)
            save_note(res)
        else:
            print("输入错误，请重新选择")

if __name__ == "__main__":
    main()
