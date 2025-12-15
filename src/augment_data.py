import os
import cv2

# 1. Configuration
TRAIN_IMG_DIR = "data/yolo_dataset/images/train"

def augment_data():
    print(f"Starting Augmentation on: {TRAIN_IMG_DIR}")
    
    # Get list of existing images (only .png)
    images = [f for f in os.listdir(TRAIN_IMG_DIR) if f.endswith(".png")]
    initial_count = len(images)
    print(f"Initial Image Count: {initial_count}")
    
    new_images_count = 0
    for img_name in images:
        img_path = os.path.join(TRAIN_IMG_DIR, img_name)
        img = cv2.imread(img_path)
        
        if img is None:
            continue
            
        # 1. Horizontal Flip (Mirror)
        h_flip = cv2.flip(img, 1)
        h_name = f"aug_h_{img_name}"
        cv2.imwrite(os.path.join(TRAIN_IMG_DIR, h_name), h_flip)
        
        # 2. Vertical Flip
        v_flip = cv2.flip(img, 0)
        v_name = f"aug_v_{img_name}"
        cv2.imwrite(os.path.join(TRAIN_IMG_DIR, v_name), v_flip)
        
        new_images_count += 2 
        
    final_count = len(os.listdir(TRAIN_IMG_DIR))
    print(f"✔ Augmentation Complete.")
    print(f"Added {new_images_count} new images.")
    print(f"Total images in Train: {final_count}")

if __name__ == "__main__":
    augment_data()