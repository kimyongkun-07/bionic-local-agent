from planner import HarnessPlanner
from tools.code_analyze import code_analyze
from tools.gen_exercise import gen_exercise
from tools.summary_note import summary_note

def main():
    planner = HarnessPlanner()
    print("===== Harness编程学习助教智能体（Pi Agent架构） =====")
    goal = input("请输入你的编程学习目标：")
    collect_data = []

    while True:
        action = planner.think(goal)
        print(f"\n【Harness调度思考】{action}")
        act_name = action["next_action"]
        act_param = action["action_input"]

        if act_name == "finish":
            print(" 学习任务完成，正在生成学习笔记！")
            note = summary_note(collect_data)
            print("\n=====学习笔记=====")
            print(note)
            break
        elif act_name == "code_analyze":
            res = code_analyze(act_param)
            collect_data.append({"type":"代码分析","content":res["analysis"]})
            planner.record_completed(f"已完成代码分析任务，输入代码：{act_param[:30]}...")
        elif act_name == "gen_exercise":
            res = gen_exercise(act_param)
            collect_data.append({"type":"编程习题","content":res["exercise"]})
            planner.record_completed(f"已生成{act_param}的编程练习题")
        else:
            print("未知工具，任务终止")
            break

if __name__ == "__main__":
    main()
