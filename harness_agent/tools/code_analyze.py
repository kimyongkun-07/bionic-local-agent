def code_analyze(code_text: str):
    """分析代码，找bug、解释逻辑"""
    # 原型，交给本地大模型做解析，这里是工具入口
    return {
        "original_code": code_text,
        "analysis": "【调用本地大模型】分析代码结构，查找语法/逻辑错误，解释每一行作用，给出优化方案。"
    }
