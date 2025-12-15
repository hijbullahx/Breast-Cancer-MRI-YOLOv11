import os
import shutil

# 1. Configuration
LABEL_DIR = "data/processed/labels"
IMAGE_DIR = "data/processed/images"

# Create labels folder
if os.path.exists(LABEL_DIR):
    shutil.rmtree(LABEL_DIR)
os.makedirs(LABEL_DIR, exist_ok=True)

def create_sample_label():
    """
    Creates a dummy label for Slice #65 (assuming it's the middle slice).
    YOLO Format: class x_center y_center width height
    We will label a 'fake' tumor in the center of the image.
    """
    # Sample file name (Must match the image name exactly, but end with .txt)
    # Note: Our images are named like '1-001.png', '1-002.png'... 
    # Let's find the actual name of the 65th file to be safe.
    
    sorted_images = sorted(os.listdir(IMAGE_DIR))
    if len(sorted_images) < 65:
        print("⚠ Not enough images to label slice 65.")
        return

    target_image = sorted_images[64] # Index 64 is the 65th image
    label_filename = target_image.replace(".png", ".txt")
    label_path = os.path.join(LABEL_DIR, label_filename)
    
    # Dummy Coordinates: Class 0 (Tumor), Center (0.5, 0.5), Size (20% of image)
    # Format: class x y w h
    dummy_annotation = "0 0.5 0.5 0.2 0.2"
    
    with open(label_path, "w") as f:
        f.write(dummy_annotation)
    
    print(f"✔ Created label file: {label_path}")
    print(f"Content: {dummy_annotation}")

if __name__ == "__main__":
    create_sample_label()