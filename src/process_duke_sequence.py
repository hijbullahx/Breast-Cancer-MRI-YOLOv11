import os
import pydicom
import cv2
import numpy as np
import shutil

# Configuration
RAW_ROOT = "data/duke_raw"
PROCESSED_DIR = "data/duke_processed/images"
# Keywords to find the right folder (Case insensitive)
TARGET_SEQ_KEYWORDS = ["1st pass", "1st_pass", "ax dyn 1st", "ax dyn pre"] 

# Create output
if os.path.exists(PROCESSED_DIR):
    shutil.rmtree(PROCESSED_DIR)
os.makedirs(PROCESSED_DIR, exist_ok=True)

def normalize_mri(pixel_array):
    """Normalize 16-bit DICOM to 8-bit grayscale"""
    pixel_array = pixel_array.astype(float)
    min_val = np.min(pixel_array)
    max_val = np.max(pixel_array)
    if max_val - min_val == 0:
        return np.zeros(pixel_array.shape, dtype=np.uint8)
    scaled = (pixel_array - min_val) / (max_val - min_val) * 255.0
    return scaled.astype(np.uint8)

def process_duke_data():
    print(f"--- Processing Duke Dataset (Target Keywords: {TARGET_SEQ_KEYWORDS}) ---")
    
    patients = [d for d in os.listdir(RAW_ROOT) if os.path.isdir(os.path.join(RAW_ROOT, d))]
    print(f"Found {len(patients)} patient folders.")
    
    total_converted = 0
    
    for patient_id in patients:
        patient_path = os.path.join(RAW_ROOT, patient_id)
        
        # 1. Find the correct sequence folder
        target_folder = None
        
        # Get all subfolders (sequences)
        subdirs = [d for d in os.listdir(patient_path) if os.path.isdir(os.path.join(patient_path, d))]
        
        for seq_name in subdirs:
            # Check if keyword is in the folder name
            if any(k in seq_name.lower() for k in TARGET_SEQ_KEYWORDS):
                target_folder = os.path.join(patient_path, seq_name)
                break
        
        # Fallback: If no keyword match, grab the folder with the MOST images (usually the main volume)
        if not target_folder and subdirs:
            full_paths = [os.path.join(patient_path, s) for s in subdirs]
            target_folder = max(full_paths, key=lambda x: len(os.listdir(x)))
            # print(f"  ⚠ No keyword match for {patient_id}. Using largest folder.")

        if target_folder and os.path.isdir(target_folder):
            # 2. Convert DICOMs in that folder
            dicom_files = [f for f in os.listdir(target_folder) if f.endswith(".dcm")]
            
            # Sort by filename to keep slice order (important for 3D context later)
            dicom_files.sort()
            
            for i, dcm_file in enumerate(dicom_files):
                try:
                    ds = pydicom.dcmread(os.path.join(target_folder, dcm_file))
                    img = normalize_mri(ds.pixel_array)
                    
                    # Save Name: PatientID_SliceNum.png
                    # Example: Breast_MRI_001_045.png
                    out_name = f"{patient_id}_{i:03d}.png"
                    cv2.imwrite(os.path.join(PROCESSED_DIR, out_name), img)
                    total_converted += 1
                except Exception as e:
                    pass # Skip bad files

    print(f"✔ Processing Complete.")
    print(f"Total Images Saved: {total_converted}")
    print(f"Location: {PROCESSED_DIR}")

if __name__ == "__main__":
    process_duke_data()