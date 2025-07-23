from ultralytics import YOLO
import torch

# Check MPS availability
if torch.backends.mps.is_available():
    device = 'mps'
    print("Training with MPS (Apple GPU)")
else:
    device = 'cpu'
    print("MPS not available, fallback to CPU")

# Load the YOLO model
model = YOLO('yolov8n.pt')

# Start training
model.train(
    data='data.yaml', # Dataset profiles
    epochs=70,       # Training rounds
    imgsz=640,         # Input image size
    batch=16,          # Batch size
    device=device       # Use MPS or CPU
)

print('Training completed')