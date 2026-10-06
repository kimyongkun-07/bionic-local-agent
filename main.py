# -*- coding: utf-8 -*-
# 模块名称：main.py
# 功能：项目入口主文件
# 职责：仅调度前端CLI和后端模型接口，业务逻辑拆分到其他模块
from frontend.cli_ui import show_menu, user_input_prompt, display_result
from backend.llm_api import get_llm_response

def main():
    while True:
        select = show_menu()
        if select == "0":
            print("程序退出")
            break
        elif select == "1":
            prompt = user_input_prompt()
            res = get_llm_response(prompt)
            display_result(res)
        elif select == "2":
            file_path = input("请输入代码文件路径：")
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    code_content = f.read()
                prompt = f"分析下面这段代码，找出bug并给出解释：\n{code_content}"
                res = get_llm_response(prompt)
                display_result(res)
            except Exception as e:
                print("读取文件失败：", e)
        else:
            print("无效选项，请重新选择")

if __name__ == "__main__":
    main()
