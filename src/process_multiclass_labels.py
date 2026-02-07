import os
import pandas as pd
import shutil

# --- CONFIGURATION (FAST TRACK - CSV FIX) ---
DRIVE_ROOT = "/content/drive/MyDrive/duke_processed_images"

# Corrected Input Filenames based on Masud's report
ANNOTATION_PATH = os.path.join(DRIVE_ROOT, "Annotation_Boxes(Sheet1).csv")
CLINICAL_PATH = os.path.join(DRIVE_ROOT, "Clinical_and_Other_Features(Data).csv")

# Output Directory
LABELS_DIR = os.path.join(DRIVE_ROOT, "labels")

def process_labels_csv_fix():
    print(f"--- P5.T4: Generating Labels from CSVs in {DRIVE_ROOT} ---")
    
    # 1. Check Inputs
    if not os.path.exists(ANNOTATION_PATH):
        print(f"❌ Error: '{os.path.basename(ANNOTATION_PATH)}' not found.")
        print("   Please check the filename in your Drive folder.")
        return
    if not os.path.exists(CLINICAL_PATH):
        print(f"❌ Error: '{os.path.basename(CLINICAL_PATH)}' not found.")
        return

    # 2. Setup Output Folder
    if os.path.exists(LABELS_DIR):
        shutil.rmtree(LABELS_DIR)
    os.makedirs(LABELS_DIR, exist_ok=True)
    print(f"✔ Creating labels folder: {LABELS_DIR}")

    # 3. Load Data (Using read_csv now)
    print("Loading CSV files...")
    try:
        df_boxes = pd.read_csv(ANNOTATION_PATH)
        df_clinical = pd.read_csv(CLINICAL_PATH)
    except Exception as e:
        print(f"❌ CSV Read Error: {e}")
        return
    
    # Map Diagnosis (Patient ID -> Diagnosis)
    # Ensure column names match. Usually 'Patient ID' and 'Diagnosis'
    # Check if Diagnosis is missing or named differently
    if 'Diagnosis' not in df_clinical.columns:
        print(f"⚠ Warning: 'Diagnosis' column not found. Available: {df_clinical.columns}")
        # Try to find a similar column or default to 0
        patient_diagnosis = {}
    else:
        patient_diagnosis = dict(zip(df_clinical['Patient ID'], df_clinical['Diagnosis']))

    label_count = 0
    missing_images = 0
    
    # 4. Generate Labels
    for index, row in df_boxes.iterrows():
        patient_id = row['Patient ID']
        class_id = patient_diagnosis.get(patient_id, 0) # Default to 0 if unknown
        
        start_slice = int(row['Start Slice'])
        end_slice = int(row['End Slice'])
        
        # Coordinates
        x1, y1 = row['Start Column'], row['Start Row']
        x2, y2 = row['End Column'], row['End Row']
        
        # Assume 512x512 dimensions
        img_w, img_h = 512.0, 512.0
        
        # YOLO Calculation
        box_w = (x2 - x1) / img_w
        box_h = (y2 - y1) / img_h
        box_cx = (x1 + (x2 - x1)/2) / img_w
        box_cy = (y1 + (y2 - y1)/2) / img_h
        
        for slice_idx in range(start_slice, end_slice + 1):
            # Filename Match: Breast_MRI_001_045.png
            image_name = f"{patient_id}_{slice_idx:03d}.png"
            image_path = os.path.join(DRIVE_ROOT, image_name)
            
            # Check if image exists
            if os.path.exists(image_path):
                out_filename = f"{patient_id}_{slice_idx:03d}.txt"
                out_path = os.path.join(LABELS_DIR, out_filename)
                
                with open(out_path, "w") as f:
                    f.write(f"{class_id} {box_cx:.6f} {box_cy:.6f} {box_w:.6f} {box_h:.6f}\n")
                
                label_count += 1
            else:
                missing_images += 1

    print(f"✔ Generated {label_count} label files.")
    if missing_images > 0:
        print(f"⚠ Skipped {missing_images} labels (Image not found in folder).")

if __name__ == "__main__":
    process_labels_csv_fix()