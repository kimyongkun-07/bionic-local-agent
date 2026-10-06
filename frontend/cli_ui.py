# -*- coding: utf-8 -*-
# 模块名称：cli_ui.py
# 功能：前端CLI交互模块
# 职责：仅负责控制台输入、输出展示，不调用模型API
from backend.llm_api import get_llm_response

def show_menu():
    print("===== 编程助教CLI =====")
    print("1. 输入代码提问")
    print("2. 读取本地代码文件分析")
    print("0. 退出程序")
    return input("请选择功能：")

def user_input_prompt():
    prompt = input("\n请输入你的问题/代码：")
    return prompt

def display_result(text):
    print("\n【模型回复】")
    print(text)
