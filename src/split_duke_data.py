import os
import shutil
import random
from pathlib import Path

# --- CONFIGURATION ---
DRIVE_ROOT = "/content/drive/MyDrive/duke_processed_images"
SOURCE_IMAGES = DRIVE_ROOT
SOURCE_LABELS = os.path.join(DRIVE_ROOT, "labels")

# Destination (Clean YOLO Structure)
DEST_ROOT = "/content/drive/MyDrive/duke_yolo_final"

def split_dataset():
    print(f"--- P5.T5: Organizing Data into YOLO Structure ---")
    
    # 1. Identify Valid Pairs (Image + Label)
    if not os.path.exists(SOURCE_LABELS):
        print("❌ Error: Labels folder not found. Did previous step finish?")
        return

    label_files = [f for f in os.listdir(SOURCE_LABELS) if f.endswith(".txt")]
    valid_pairs = []

    print(f"Scanning {len(label_files)} label files for matching images...")
    
    for lbl in label_files:
        base_name = lbl.replace(".txt", "")
        # Check for PNG match
        img_name = base_name + ".png"
        img_path = os.path.join(SOURCE_IMAGES, img_name)
        
        if os.path.exists(img_path):
            valid_pairs.append((img_name, lbl))
    
    print(f"✔ Found {len(valid_pairs)} valid Image-Label pairs.")
    
    if len(valid_pairs) == 0:
        print("❌ No valid pairs found. Check your filenames.")
        return

    # 2. Shuffle and Split (80/20)
    random.seed(42)
    random.shuffle(valid_pairs)
    
    split_idx = int(len(valid_pairs) * 0.8)
    train_set = valid_pairs[:split_idx]
    val_set = valid_pairs[split_idx:]
    
    print(f"Training items: {len(train_set)}")
    print(f"Validation items: {len(val_set)}")

    # 3. Move Files
    # Create structure: images/train, labels/train, etc.
    for split, pairs in [("train", train_set), ("val", val_set)]:
        img_dest = os.path.join(DEST_ROOT, "images", split)
        lbl_dest = os.path.join(DEST_ROOT, "labels", split)
        
        os.makedirs(img_dest, exist_ok=True)
        os.makedirs(lbl_dest, exist_ok=True)
        
        print(f"Populating {split} folders...")
        for img, lbl in pairs:
            # Copy Image
            shutil.copy(os.path.join(SOURCE_IMAGES, img), os.path.join(img_dest, img))
            # Copy Label
            shutil.copy(os.path.join(SOURCE_LABELS, lbl), os.path.join(lbl_dest, lbl))

    print(f"✔ Dataset Split Complete!")
    print(f"Location: {DEST_ROOT}")

if __name__ == "__main__":
    split_dataset()