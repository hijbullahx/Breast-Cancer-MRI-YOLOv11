from ultralytics import YOLO
import os

def run_sanity_check():
    print("--- Starting Sanity Check Training ---")
    
    # 1. Load the Custom Model Architecture
    # (Ensure custom_yolov11.yaml exists from previous step)
    try:
        model = YOLO("custom_yolov11.yaml") 
    except Exception as e:
        print(f"Error loading model: {e}")
        return

    # 2. Train for 3 Epochs (Fast test)
    # We use yolo_config.yaml which we created in P3.T2
    try:
        results = model.train(
            data="yolo_config.yaml",
            epochs=3,           # Only 3 loops
            imgsz=224,          # Small image size for speed
            batch=8,            # Small batch
            name="sanity_check",
            verbose=True
        )
        print("✔ Dry Run Complete! System is ready for full training.")
        
    except Exception as e:
        print(f"❌ Training Failed: {e}")

if __name__ == "__main__":
    run_sanity_check()