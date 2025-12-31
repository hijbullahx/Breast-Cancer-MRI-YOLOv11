from ultralytics import YOLO
import os
import cv2
import matplotlib.pyplot as plt

def run_inference(image_path, model_path):
    print(f"--- Running Inference on {image_path} ---")
    
    if not os.path.exists(model_path):
        print("❌ Error: Model not found. Did you run training?")
        return
    if not os.path.exists(image_path):
        print("❌ Error: Image not found.")
        return

    # 1. Load Model
    model = YOLO(model_path)

    # 2. Predict
    # conf=0.01 means "show me ANYTHING even if you are not sure"
    results = model.predict(source=image_path, conf=0.01, save=True, verbose=True)
    
    # 3. Show Result
    # Ultralytics saves images to 'runs/detect/predict...'
    # We will just plot the first result array directly
    result = results[0]
    
    # Plotting
    plt.figure(figsize=(8, 8))
    plt.imshow(result.plot()) # .plot() draws the box on the image
    plt.axis('off')
    plt.title("Model Prediction")
    plt.show()
    
    print("✔ Inference Complete.")

if __name__ == "__main__":
    # In Colab, we pick a random image from our validation set
    # Update this path if yours is different
    val_dir = "data/yolo_dataset/images/val"
    best_model = "runs/detect/tumor_detector_v1/weights/best.pt"
    
    if os.path.exists(val_dir):
        # Pick the first image found
        sample_img = os.path.join(val_dir, os.listdir(val_dir)[0])
        run_inference(sample_img, best_model)
    else:
        print("Please check your dataset paths.")