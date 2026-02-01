import os
import pandas as pd
import pydicom
import cv2
import numpy as np
import shutil

# Configuration
RAW_ROOT = "data/duke_raw"
CSV_PATH = os.path.join(RAW_ROOT, "metadata.csv")
PROCESSED_DIR = "data/duke_processed/images"

# Keywords we want in the 'Series Description' column
TARGET_KEYWORDS = ["1st pass", "ax dyn 1st", "ax dyn pre"]

if os.path.exists(PROCESSED_DIR):
    shutil.rmtree(PROCESSED_DIR)
os.makedirs(PROCESSED_DIR, exist_ok=True)

def normalize_mri(pixel_array):
    pixel_array = pixel_array.astype(float)
    min_val = np.min(pixel_array)
    max_val = np.max(pixel_array)
    if max_val - min_val == 0:
        return np.zeros(pixel_array.shape, dtype=np.uint8)
    scaled = (pixel_array - min_val) / (max_val - min_val) * 255.0
    return scaled.astype(np.uint8)

def process_via_csv():
    print("--- Processing Duke Data using Metadata CSV ---")
    
    if not os.path.exists(CSV_PATH):
        print("❌ Metadata CSV not found.")
        return

    df = pd.read_csv(CSV_PATH)
    
    # 1. Filter the CSV for our target sequences
    # We create a regex pattern to find ANY of our keywords
    pattern = '|'.join(TARGET_KEYWORDS)
    # Case insensitive search
    filtered_df = df[df['Series Description'].str.contains(pattern, case=False, na=False)]
    
    print(f"Found {len(filtered_df)} DICOM series matching keywords: {TARGET_KEYWORDS}")
    
    total_converted = 0
    
    # 2. Iterate through valid rows
    for index, row in filtered_df.iterrows():
        # The CSV has paths like: .\Duke-Breast-Cancer-MRI\Breast_MRI_001\...
        # We need to fix this to match our Colab path: data/duke_raw/Breast_MRI_001...
        
        csv_path = row['File Location']
        patient_id = row['Subject ID']
        
        # Clean up path
        # Remove '.\Duke-Breast-Cancer-MRI' prefix
        rel_path = csv_path.replace(".\\Duke-Breast-Cancer-MRI", "").replace("./Duke-Breast-Cancer-MRI", "")
        # Remove leading slash/backslash if present
        rel_path = rel_path.lstrip("\\").lstrip("/")
        # Fix slashes
        rel_path = rel_path.replace("\\", "/")
        
        # Construct full path
        full_dir_path = os.path.join(RAW_ROOT, rel_path)
        
        if not os.path.exists(full_dir_path):
            # Try to match the patient ID folder directly if structure differs
            # print(f"Warning: Path not found {full_dir_path}, attempting fallback...")
            continue
            
        # Process all DICOMs in this folder
        if os.path.isdir(full_dir_path):
            files = sorted([f for f in os.listdir(full_dir_path) if f.endswith('.dcm')])
            
            for i, f_name in enumerate(files):
                dcm_path = os.path.join(full_dir_path, f_name)
                try:
                    ds = pydicom.dcmread(dcm_path)
                    img = normalize_mri(ds.pixel_array)
                    
                    # Save: PatientID_SliceNum.png
                    out_name = f"{patient_id}_{i:03d}.png"
                    cv2.imwrite(os.path.join(PROCESSED_DIR, out_name), img)
                    total_converted += 1
                except Exception as e:
                    pass

    print(f"✔ Processing Complete.")
    print(f"Total Images Saved: {total_converted}")

if __name__ == "__main__":
    process_via_csv()