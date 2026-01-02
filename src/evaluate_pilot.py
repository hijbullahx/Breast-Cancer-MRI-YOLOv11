from ultralytics import YOLO
import os
import matplotlib.pyplot as plt
from IPython.display import Image, display

def evaluate_pilot_run():
    print("--- Running Pilot Evaluation (Training Set) ---")
    
    # 1. Load the Best Model from Phase 4
    model_path = "runs/detect/tumor_detector_v1/weights/best.pt"
    
    if not os.path.exists(model_path):
        print("❌ Error: 'best.pt' not found. Did Phase 4 finish?")
        return

    model = YOLO(model_path)

    # 2. Run Evaluation on TRAINING Data
    # We use split='train' because that's where our dummy label is!
    print("Calculating metrics on Training Data (to verify learning)...")
    
    # Check config path
    data_config = "yolo_config.yaml"
    if not os.path.exists(data_config):
        data_config = "configs/data.yaml"

    results = model.val(
        data=data_config,
        split='train',        # <--- THE MAGIC TRICK
        name="pilot_evaluation",
        verbose=True,
        plots=True
    )
    
    print("\n✔ Pilot Metrics (Train Split):")
    print(f"  Precision: {results.results_dict['metrics/precision(B)']:.4f}")
    print(f"  Recall:    {results.results_dict['metrics/recall(B)']:.4f}")
    print(f"  mAP@50:    {results.results_dict['metrics/mAP50(B)']:.4f}")
    
    # 3. Show the Confusion Matrix
    cm_path = "runs/detect/pilot_evaluation/confusion_matrix.png"
    if os.path.exists(cm_path):
        print("\n--- Confusion Matrix ---")
        display(Image(cm_path))
    else:
        print("Confusion matrix not found.")

if __name__ == "__main__":
    evaluate_pilot_run()