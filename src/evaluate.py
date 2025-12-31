from ultralytics import YOLO
import os
import argparse

def evaluate_model(model_path):
    print(f"--- Starting Evaluation for: {model_path} ---")
    
    if not os.path.exists(model_path):
        print(f"❌ Error: Model file not found at {model_path}")
        print("   (Did you finish training in Phase 4 yet?)")
        return

    # 1. Load the Trained Model
    try:
        model = YOLO(model_path)
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        return

    # 2. Run Validation
    # This uses the 'val' split defined in data.yaml
    try:
        # data config path
        data_config = "yolo_config.yaml"
        if not os.path.exists(data_config):
            data_config = "configs/data.yaml"

        metrics = model.val(
            data=data_config,
            split='val',
            name="evaluation_run",
            verbose=True
        )
        
        print("\n✔ Evaluation Complete.")
        print(f"mAP@50: {metrics.box.map50:.4f}")
        print(f"mAP@50-95: {metrics.box.map:.4f}")
        print("Detailed plots saved in: runs/detect/evaluation_run")
        
    except Exception as e:
        print(f"❌ Evaluation Failed: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # Default points to where training usually saves the best model
    parser.add_argument("--model", type=str, default="runs/detect/tumor_detector_v1/weights/best.pt", help="Path to .pt model file")
    args = parser.parse_args()
    
    evaluate_model(args.model)