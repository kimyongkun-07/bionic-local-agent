from llm_client import local_llm_call
from tools import gen_exercise

def main():
    print("===== Harness 编程助教智能体 =====")
    user_query = input("请输入你的学习需求：")

    max_tool_calls = 3
    call_count = 0
    history = []

    system_prompt = """
你是编程学习调度智能体。根据用户需求选择工具，只输出JSON，不要多余文字。
可选工具：
1. gen_exercise：生成练习题，参数 language、topic
任务终止条件：达到最大调用次数，或者需求完成输出 {"action":"finish"}
"""
    while call_count < max_tool_calls:
        # 拼接系统提示词 + 用户和历史对话
        prompt = f"{system_prompt}\n用户需求：{user_query}\n历史记录：{history}"
        resp = local_llm_call(prompt)
        print(f"\n【Harness调度思考】{resp}")

        import json
        try:
            data = json.loads(resp)
        except Exception as e:
            print("模型输出解析失败，结束任务")
            break

        next_action = data.get("action")
        action_input = data.get("params", {})

        if next_action == "finish":
            print("任务完成，准备生成笔记")
            break
        elif next_action == "gen_exercise":
            res = gen_exercise(action_input)
            history.append({"action": next_action, "params": action_input, "result": res})
            call_count += 1
            print(f"工具调用成功，次数：{call_count}/{max_tool_calls}")
        else:
            print("未知动作，退出调度")
            break

    # 生成学习笔记
    print("\n达到最大工具调用次数，任务结束，生成学习笔记")
    print("\n=====学习笔记=====")
    if len(history) > 0:
        last_input = history[-1]["params"]
        lang = last_input["language"]
        topic = last_input["topic"]
        note_prompt = f"""
请根据知识点：{topic}，编程语言：{lang}
写一份学习笔记，包含两点：
1.知识点简要讲解
2.一道编程练习题，含题目、输入输出、参考答案
"""
        note = local_llm_call(note_prompt)
        print(note)
    else:
        print("本次没有调用工具")

if __name__ == "__main__":
    main()
