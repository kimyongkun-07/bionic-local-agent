# -*- coding: utf-8 -*-
# 模块名称：llm_api.py
# 功能：后端模块，封装LM Studio本地Bionic模型API调用
# 职责：仅负责发送请求、接收模型返回，不处理交互界面
import requests

API_URL = "http://127.0.0.1:1234/v1/chat/completions"

def get_llm_response(prompt: str, stream: bool = False):
    payload = {
        "model": "bionic",
        "messages": [{"role": "user", "content": prompt}],
        "stream": stream
    }
    resp = requests.post(API_URL, json=payload, stream=stream)
    if not stream:
        return resp.json()["choices"][0]["message"]["content"]
    return resp
