def gen_exercise(knowledge: str):
    """根据知识点生成编程习题"""
    return {
        "knowledge_point": knowledge,
        "exercise": f"【练习题】围绕{knowledge}设计编程题目，包含题目描述、输入输出要求、参考答案。"
    }
