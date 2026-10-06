import sys
from pathlib import Path
# 把项目根目录加入python搜索路径
sys.path.append(str(Path(__file__).parent.parent))

from backend.llm_api import call_bionic

from backend.llm_api import call_bionic

def main():
    print("===== 本地Bionic编程助教 =====")
    print("输入问题和代码，输入 exit 退出程序\n")
    while True:
        user_text = input(">>> ")
        user_text = user_text.strip()
        if user_text.lower() == "exit":
            print("程序退出")
            break
        # 调用本地Bionic模型API
        try:
            reply = call_bionic(user_text)
            print(f"\n模型回复：\n{reply}\n")
        except Exception as e:
            print(f"请求出错：{e}")
            print("请检查LM Studio是否启动、模型是否加载、API服务是否打开\n")

if __name__ == "__main__":
    main()
