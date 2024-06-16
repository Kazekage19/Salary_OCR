from ultralytics import YOLO
model = YOLO("yolov8s.pt")
results = model.train(data='config.yaml', epochs=50) 
