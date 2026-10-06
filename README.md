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
