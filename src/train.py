from ultralytics import YOLO
import os
import argparse

def train_model(epochs=50, img_size=224, batch_size=16):
    print(f"--- Starting Full Training (Epochs: {epochs}) ---")
    
    # 1. Load the Custom Model
    model_path = "custom_yolov11.yaml" # Defined in P3.T3
    if not os.path.exists(model_path):
        # Fallback if running from root dir
        model_path = "configs/custom_yolov11.yaml"
    
    try:
        model = YOLO(model_path)
    except Exception as e:
        print(f"❌ Error loading model config: {e}")
        return

    # 2. Configure Training
    # data config path
    data_config = "yolo_config.yaml"
    if not os.path.exists(data_config):
        data_config = "configs/data.yaml"

    try:
        results = model.train(
            data=data_config,
            epochs=epochs,
            imgsz=img_size,
            batch=batch_size,
            name="tumor_detector_v1",
            patience=10,        # Stop if no improvement for 10 epochs
            save=True,          # Save checkpoints
            device=0,           # Use GPU (index 0)
            verbose=True,
            exist_ok=True       # Overwrite existing project folder if needed
        )
        print("✔ Training Finished.")
        print(f"Best Model Saved at: runs/detect/tumor_detector_v1/weights/best.pt")
        
    except Exception as e:
        print(f"❌ Training Crashed: {e}")

if __name__ == "__main__":
    # Allow running from command line with arguments
    # Example: python src/train.py --epochs 100
    parser = argparse.ArgumentParser()
    parser.add_argument("--epochs", type=int, default=50, help="Number of training epochs")
    parser.add_argument("--batch", type=int, default=16, help="Batch size")
    args = parser.parse_args()
    
    train_model(epochs=args.epochs, batch_size=args.batch)