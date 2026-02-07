import os
import pandas as pd
import shutil

# --- CONFIGURATION (SINGLE CLASS: TUMOR DETECTION) ---
DRIVE_ROOT = "/content/drive/MyDrive/duke_processed_images"
ANNOTATION_PATH = os.path.join(DRIVE_ROOT, "Annotation_Boxes(Sheet1).csv")
LABELS_DIR = os.path.join(DRIVE_ROOT, "labels")

def process_labels_single_class():
    print(f"--- P5.T4: Generating Tumor Labels (Single Class) ---")
    
    # 1. Check Input
    if not os.path.exists(ANNOTATION_PATH):
        print(f"❌ Error: '{os.path.basename(ANNOTATION_PATH)}' not found.")
        return

    # 2. Setup Output Folder
    if os.path.exists(LABELS_DIR):
        shutil.rmtree(LABELS_DIR)
    os.makedirs(LABELS_DIR, exist_ok=True)
    print(f"✔ Creating labels folder: {LABELS_DIR}")

    # 3. Load Annotations
    print("Loading Annotation Data...")
    df_boxes = pd.read_csv(ANNOTATION_PATH)
    
    label_count = 0
    missing_images = 0
    
    # 4. Generate Labels
    for index, row in df_boxes.iterrows():
        patient_id = row['Patient ID']
        
        # Class 0 = Tumor (Since all are malignant)
        class_id = 0 
        
        start_slice = int(row['Start Slice'])
        end_slice = int(row['End Slice'])
        
        # Coordinates
        x1, y1 = row['Start Column'], row['Start Row']
        x2, y2 = row['End Column'], row['End Row']
        
        # Assume 512x512
        img_w, img_h = 512.0, 512.0
        
        # YOLO Calculation
        box_w = (x2 - x1) / img_w
        box_h = (y2 - y1) / img_h
        box_cx = (x1 + (x2 - x1)/2) / img_w
        box_cy = (y1 + (y2 - y1)/2) / img_h
        
        for slice_idx in range(start_slice, end_slice + 1):
            image_name = f"{patient_id}_{slice_idx:03d}.png"
            image_path = os.path.join(DRIVE_ROOT, image_name)
            
            if os.path.exists(image_path):
                out_filename = f"{patient_id}_{slice_idx:03d}.txt"
                out_path = os.path.join(LABELS_DIR, out_filename)
                
                with open(out_path, "w") as f:
                    f.write(f"{class_id} {box_cx:.6f} {box_cy:.6f} {box_w:.6f} {box_h:.6f}\n")
                
                label_count += 1
            else:
                missing_images += 1

    print(f"✔ Generated {label_count} label files.")
    print(f"✔ Class Defined: 0 = Tumor")
    if missing_images > 0:
        print(f"⚠ Skipped {missing_images} labels (Image not found in folder).")

if __name__ == "__main__":
    process_labels_single_class()