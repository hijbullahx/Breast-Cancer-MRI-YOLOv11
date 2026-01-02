import os

def generate_dummy_labels():
    train_img_dir = "data/yolo_dataset/images/train"
    train_lbl_dir = "data/yolo_dataset/labels/train"
    
    print(f"Generating labels for all images in {train_img_dir}...")
    
    if not os.path.exists(train_lbl_dir):
        os.makedirs(train_lbl_dir)

    images = [f for f in os.listdir(train_img_dir) if f.endswith(".png")]
    for img_name in images:
        txt_name = img_name.replace(".png", ".txt")
        txt_path = os.path.join(train_lbl_dir, txt_name)
        
        # Write dummy label (Class 0, Center Box)
        with open(txt_path, "w") as f:
            f.write("0 0.5 0.5 0.2 0.2")
            
    print(f"✔ Generated {len(images)} dummy labels for testing.")

if __name__ == "__main__":
    generate_dummy_labels()