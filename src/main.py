import os
from utils import load_config

def main():
    # 获取当前main.py文件所在目录
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # 拼接配置文件完整路径
    config_path = os.path.join(base_dir, "../config/config.yaml")
    config = load_config(config_path)

    print("===== Bionic Local Agent 本地对话程序 =====")
    print(f"模型温度：{config['model']['temperature']}")
    print("输入问题进行对话，输入 exit 退出程序\n")

    while True:
        user_input = input("你：")
        if user_input.strip() == "exit":
            print("程序退出")
            break
        # 这里后续接入Bionic模型生成回答
        print("Agent：【模型回答占位，后续接入Bionic】\n")


if __name__ == "__main__":
    main()

