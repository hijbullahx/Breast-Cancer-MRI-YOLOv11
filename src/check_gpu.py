import torch
import sys
import os

# 1. Install Ultralytics (Only needed in Colab/Local, not for file saving)
try:
    import ultralytics
except ImportError:
    os.system('pip install ultralytics')
    import ultralytics

from ultralytics import YOLO

def check_yolo_setup():
    print("--- YOLOv11 Setup Check ---")
    
    # Check Python & PyTorch
    print(f"Python: {sys.version.split()[0]}")
    print(f"PyTorch: {torch.__version__}")
    
    # Check Ultralytics
    print(f"Ultralytics Version: {ultralytics.__version__}")
    
    # Check GPU
    if torch.cuda.is_available():
        device_name = torch.cuda.get_device_name(0)
        print(f"✔ GPU Available: {device_name}")
        print("   (This is critical for Phase 4 Training)")
    else:
        print("⚠ GPU NOT Detected! Training will be very slow.")
        
    # Initialize a dummy model to test the library
    try:
        model = YOLO("yolo11n.pt") # Load 'nano' version (smallest)
        print("✔ YOLOv11n model loaded successfully.")
    except Exception as e:
        print(f"❌ Error loading YOLO model: {e}")

if __name__ == "__main__":
    check_yolo_setup()