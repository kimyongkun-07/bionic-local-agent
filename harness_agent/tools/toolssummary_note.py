def summary_note(all_data):
    text = "# 编程学习笔记\n\n"
    for item in all_data:
        text += f"## {item['type']}\n{item['content']}\n\n"
    text += "\n## 学习小结\n本次学习完成知识点练习与代码分析。"
    return text
