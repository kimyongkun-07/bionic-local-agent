# Bionic Local Agent
华南农业大学AI协会二面项目，基于Bionic实现本地大模型对话Agent，附带YOLO实时目标检测模块

## 项目简介
本地部署开源大模型，离线运行，无需云端API。
技术栈：Python + LM Studio(Bionic) + Ultralytics YOLOv8

## 功能
1. 本地加载Bionic大模型，离线文本问答，支持多轮对话记忆
2. 可配置模型参数（temperature、上下文窗口大小）
3. 命令行交互式对话界面 + 流式逐字输出
4. YOLOv8摄像头实时目标检测，识别画面物体，输出检测框与置信度

## 任务说明
### Task1：项目初始化
搭建项目目录结构，创建Git仓库，规范工程文件，编写工程日志。

### Task2：本地LLM多轮对话
Python调用LM Studio本地Bionic模型API，实现带上下文记忆的多轮对话。

### Task3：流式对话输出
实现大模型逐字流式返回，模拟ChatGPT打字效果。

### Task4：YOLOv8实时目标检测
YOLOv8n预训练权重，调用本机摄像头，实时识别人、书本等目标，输出检测框和置信度。
>踩坑记录：原本计划微调coco8数据集，海外资源下载失败，改为直接使用预训练权重做推理。

## 环境依赖
- Python >=3.10
- ultralytics
- LM Studio（加载Bionic模型，开启本地API服务）

## 运行方式
1. 打开LM Studio，加载Bionic模型，启动本地API服务
2. 进入examples文件夹
3. 运行本地大模型对话：`python main.py`
4. 运行YOLO摄像头检测：`python task4_yolo_infer.py`

## 工程日志
每个任务独立配套工程日志，记录实验步骤、报错与解决方案，存放于examples目录。
