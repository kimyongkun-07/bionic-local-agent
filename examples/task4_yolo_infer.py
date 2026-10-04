from ultralytics import YOLO

# 加载本地提前下载好的 yolov8n.pt
model = YOLO("./yolov8n.pt")

# 调用摄像头实时检测，弹出画面窗口
model.predict(source=0, show=True)
