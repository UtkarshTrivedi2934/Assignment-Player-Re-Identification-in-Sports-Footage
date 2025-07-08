#Import All the Required Libraries
from ultralytics import YOLO

# After replacing with your trained model:
model = YOLO("model/best.pt")  # Your fine-tuned YOLOv11 model
results = model.track(source="input_video/15sec_input_720p.mp4", save=True, persist=True)
