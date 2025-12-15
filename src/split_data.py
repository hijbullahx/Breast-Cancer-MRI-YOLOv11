import os
import shutil
import random

# 1. Configuration
SOURCE_IMAGES = "data/processed/images"
SOURCE_LABELS = "data/processed/labels"
BASE_DIR = "data/yolo_dataset"

# Define standard YOLO folders
DIRS = [
    f"{BASE_DIR}/images/train",
    f"{BASE_DIR}/images/val",
    f"{BASE_DIR}/labels/train",
    f"{BASE_DIR}/labels/val"
]

# 2. Cleanup and Create Folders
if os.path.exists(BASE_DIR):
    shutil.rmtree(BASE_DIR)

for d in DIRS:
    os.makedirs(d, exist_ok=True)
    print(f"Created folder: {d}")

def split_and_organize(split_ratio=0.8):
    # Get all image files
    images = [f for f in os.listdir(SOURCE_IMAGES) if f.endswith(".png")]
    # Shuffle for randomness
    random.seed(42)
    random.shuffle(images)
    
    # Calculate split index
    split_idx = int(len(images) * split_ratio)
    train_files = images[:split_idx]
    val_files = images[split_idx:]
    
    print(f"Total Images: {len(images)}")
    print(f"Training: {len(train_files)} | Validation: {len(val_files)}")
    
    # Helper function to move files
    def move_files(file_list, split_name):
        for img_name in file_list:
            # Source paths
            src_img = os.path.join(SOURCE_IMAGES, img_name)
            txt_name = img_name.replace(".png", ".txt")
            src_lbl = os.path.join(SOURCE_LABELS, txt_name)
            
            # Destination paths
            dst_img = os.path.join(BASE_DIR, "images", split_name, img_name)
            dst_lbl = os.path.join(BASE_DIR, "labels", split_name, txt_name)
            
            # Copy Image
            shutil.copy(src_img, dst_img)
            
            # Copy Label (only if it exists - remember we only made ONE label earlier)
            if os.path.exists(src_lbl):
                shutil.copy(src_lbl, dst_lbl)
                
    # Execute Move
    print("Moving Training files...")
    move_files(train_files, "train")
    
    print("Moving Validation files...")
    move_files(val_files, "val")
    
    print("✔ Dataset organized successfully for YOLOv11.")

if __name__ == "__main__":
    split_and_organize()