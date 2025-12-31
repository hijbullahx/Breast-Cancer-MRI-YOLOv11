import os
import matplotlib.pyplot as plt
import cv2
import random

# 1. Configuration
TRAIN_DIR = "data/yolo_dataset/images/train"
VAL_DIR = "data/yolo_dataset/images/val"

def inspect_dataset():
    print("--- Dataset Health Check ---")
    
    # Count files
    if not os.path.exists(TRAIN_DIR) or not os.path.exists(VAL_DIR):
         print("❌ Error: Dataset folders not found!")
         return

    n_train = len(os.listdir(TRAIN_DIR))
    n_val = len(os.listdir(VAL_DIR))
    
    print(f"Training Images: {n_train}")
    print(f"Validation Images: {n_val}")
    print(f"Total Dataset Size: {n_train + n_val}")
    
    # Sanity Check
    if n_train == 0 or n_val == 0:
        print("❌ CRITICAL ERROR: Dataset is empty!")
        return
    
    # Visualize Samples
    print("\nGenerating visual sample...")
    try:
        fig, axes = plt.subplots(1, 4, figsize=(15, 5))
        
        # Pick 4 random images from Train
        sample_files = random.sample(os.listdir(TRAIN_DIR), 4)
        
        for i, file_name in enumerate(sample_files):
            img_path = os.path.join(TRAIN_DIR, file_name)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            
            axes[i].imshow(img, cmap='gray')
            axes[i].set_title(file_name[:15] + "...") # Shorten name
            axes[i].axis('off')
        
        plt.suptitle("Augmented Training Samples")
        plt.tight_layout()
        plt.show()
        print("✔ Dataset Health Check: PASSED")
    except Exception as e:
        print(f"Visualization Error: {e}")

if __name__ == "__main__":
    inspect_dataset()