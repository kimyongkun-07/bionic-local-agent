from utils import load_config

def main():
    # 加载配置文件
    config = load_config("../config/config.yaml")
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
