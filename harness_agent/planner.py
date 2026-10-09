from llm_client import local_llm_call
import json

class HarnessPlanner:
    def __init__(self):
        self.task_history = []
        self.tools = ["code_analyze", "gen_exercise", "summary_note"]

    def think(self, user_goal: str) -> dict:
        prompt = f"""
你是Harness任务调度器，参考Pi Agent架构，你是编程学习助教智能体。
用户学习目标：{user_goal}
已经完成的任务记录：{self.task_history}
可用工具列表：
1. code_analyze：输入一段代码，分析代码逻辑、定位bug、给出修改建议
2. gen_exercise：输入编程语言和知识点，生成配套编程练习题
3. summary_note：汇总本次所有学习内容，生成markdown学习笔记

输出严格JSON，不要多余文字：
{{
    "next_action": "工具名 / finish",
    "action_input": "传给工具的参数",
    "reason": "简短说明选择动作的原因"
}}
信息足够完成用户目标时，next_action填finish。
"""
        resp = local_llm_call(prompt)
        return json.loads(resp)

    def record_completed(self, task_info: str):
        self.task_history.append(task_info)
