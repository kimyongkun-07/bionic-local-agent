# Bionic Local Agent
华南农业大学AI协会二面项目，基于Bionic实现本地大模型对话Agent，附带YOLO实时目标检测模块

## 项目简介
本地部署开源大模型，离线运行，无需调用云端API。
技术栈：Python + LM Studio(Bionic) + Ultralytics YOLOv8

## 功能
1. 本地加载Bionic大模型，离线文本问答，支持多轮对话记忆
2. YOLOv8 图像目标检测推理
3. Task5：轻量化Harness智能体 - 编程助教Agent
    - 前后端分离架构：调度器 + LLM调用工具
    - 基于本地Bionic大模型，实现工具调用、任务规划
    - 增加循环次数限制，防止死循环
    - CLI交互，可对代码进行分析、查错、给出修改建议
    - 包含两个拓展子Harness：C语言代码Harness、论文阅读Harness
        - C语言Harness：C代码解析、语法纠错、代码优化、生成测试用例
        - 论文Harness：学术论文摘要提取、要点梳理、文献总结、研究思路拆解
## 项目目录结构
bionic-local-agent/
├── harness_agent/          # Task5 Harness 智能体（编程助教）
│   ├── backend/            # 后端模块：模型 API 调用
│   │   ├── **init**.py
│   │   └── llm_client.py
│   ├── tools/              # 工具集
│   │   ├── **init**.py
│   │   ├── code_tool.py    # 通用代码分析工具
│   │   ├── c_harness.py    # C 语言 Harness 子模块
│   │   └── paper_harness.py # 论文阅读 Harness 子模块
│   ├── main.py             # 项目入口，智能体调度主程序
│   └── task5_harness_shturl.txt  # Task5 工程日志
├── task2/                  # Task2 本地大模型单轮对话
├── task3/                  # Task3 流式 CLI 对话程序
├── task4_yolo/             # Task4 YOLOv8 目标检测
├── README.md
└── requirements.txt        # 项目依赖
## 环境依赖
ultralytics
requests
安装依赖命令：
```bash
pip install ultralytics requests
```
## 使用说明
1. 打开 LM Studio，加载 Bionic 模型，启动本地 API 服务（默认 `http://127.0.0.1:1234/v1`）
2. 进入对应任务文件夹，运行主程序
   # Task5 轻量化Harness智能体（包含C语言、论文Harness）
   cd harness_agent
   python main.py
## 任务清单
- Task1：本地大模型环境部署
- Task2：Python 调用本地大模型 API，实现单轮对话
- Task3：流式输出对话 CLI 程序
- Task4：YOLOv8 目标检测推理
- Task5：轻量化 Harness 智能体（编程助教 Agent）
  - 子模块 1：C 语言 Harness，针对 C 代码做静态分析、排错、优化
  - 子模块 2：论文 Harness，论文内容解析、提炼核心观点
## 项目亮点
 1.完全离线，本地大模型推理，不依赖互联网大模型接口
 2.模块化前后端分离设计，代码解耦，便于扩展新工具
 3.智能体增加循环上限约束，规避工具调用死循环问题
 4.CLI 控制台交互，轻量化，无需前端网页
 5.双拓展 Harness：C 语言代码处理 + 学术论文阅读分析
 6.配套完整工程日志，每一个任务有独立记录
