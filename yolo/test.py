from ultralytics import YOLO

a1=YOLO('YOLOv8 test/runs/detect/train/weights/best.pt')

a1('test set/1.mp4', show=True, save=True)
#show=Ture显示检测结果
