# 工程日志：Issue #1 缺陷修复
## 任务目标
修复项目主程序src/main.py仅返回占位文本的缺陷，补齐上下文窗口、模型参数传递功能，让项目README描述与实际代码功能匹配。

## 问题分析
1. 主程序仅打印硬编码占位文字，没有调用本地Bionic大模型API；
2. 模型调用代码放在examples目录，没有接入主入口；
3. temperature等参数仅打印，未传入模型；缺少对话上下文传递，无法多轮对话；
4. 项目文档README和代码实现不一致。

## 实现步骤
1. 重构backend/llm_api.py，接口接收完整messages对话列表，支持temperature、max_tokens参数；
2. 修改src/main.py，增加chat_history对话历史数组，每一轮将全部对话上下文传给模型；
3. 增加路径兼容代码，解决backend模块导入报错；
4. 本地CLI测试，验证多轮对话记忆生效；
5. Git提交、解决README合并冲突，推送代码至GitHub；
6. 在GitHub评论提交修复说明，关闭Issue。

## 测试结果
运行`python src/main.py`，可以连续对话，模型能够记住上文，temperature、max_tokens参数生效，不再输出占位文本。

## 总结
完成Issue全部需求，主程序实现本地Bionic模型多轮对话，编程助教功能完整。
