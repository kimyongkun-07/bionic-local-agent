# Bionic Local Agent
华南农业大学AI协会二面项目，基于Bionic实现本地大模型对话Agent，附带YOLO实时目标检测模块

## 项目简介
本地部署开源大模型，离线运行，无需云端API。
技术栈：Python + LM Studio(Bionic) + Ultralytics YOLOv8
## 功能
1. 本地加载Bionic大模型，离线文本问答，支持多轮对话记忆
2. YOLOv8 图像目标检测推理
3. 【Task5】前后端分离CLI编程助教
    - frontend：CLI控制台交互，负责输入输出
    - backend：模型API调用层，封装LM Studio接口
    - main.py：项目入口，调度前后端，模块解耦
## 项目目录结构
bionic-local-agent/
├── backend/              # 后端模块：模型 API 调用
│   ├── **init**.py
│   ├── llm_api.py
│   └── README.md
├── frontend/             # 前端模块：CLI 控制台交互
│   ├── **init**.py
│   ├── cli_ui.py
│   └── README.md
├── config/
├── docs/
├── examples/
├── src/
├── main.py               # 项目入口
├── .gitignore
└── README.md
## 环境依赖
```bash
pip install requests ultralytics
启动方式
# 启动CLI编程助教
python main.py
前置条件：打开 LM Studio，加载 Bionic 模型，开启本地 API 服务器
## 任务清单
- [x] Task1：搭建本地大模型环境，基础对话
- [x] Task2：Python调用本地模型API，实现对话
- [x] Task3：流式输出对话
- [x] Task4：YOLOv8目标检测推理
- [x] Task5：项目重构，前后端分离CLI编程助教

## 工程日志
- engineering_log_task1.txt
- engineering_log_task2.txt
- engineering_log_task3.txt
- engineering_log_task4.txt
- engineering_log_task5.txt
