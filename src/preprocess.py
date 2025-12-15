import os
import cv2
import pydicom
import numpy as np
import shutil

# 1. Configuration
INPUT_DIR = "data/raw/Patient_001"
OUTPUT_DIR = "data/processed/images"

# Create output folder if it doesn't exist
if os.path.exists(OUTPUT_DIR):
    shutil.rmtree(OUTPUT_DIR) # Clean up old run
os.makedirs(OUTPUT_DIR, exist_ok=True)

def normalize_image(pixel_array):
    """
    Scales the MRI pixel intensity to 0-255 (8-bit) for YOLO.
    """
    pixel_array = pixel_array.astype(float)
    min_val = np.min(pixel_array)
    max_val = np.max(pixel_array)
    
    if max_val - min_val == 0:
        return np.zeros(pixel_array.shape, dtype=np.uint8)
        
    # Min-Max Scaling Formula
    scaled = (pixel_array - min_val) / (max_val - min_val) * 255.0
    return scaled.astype(np.uint8)

def process_dicom_to_png():
    print(f"Processing DICOM files from {INPUT_DIR}...")
    
    converted_count = 0
    for root, _, files in os.walk(INPUT_DIR):
        for file in files:
            if file.lower().endswith(".dcm"):
                dcm_path = os.path.join(root, file)
                
                try:
                    # Read DICOM
                    ds = pydicom.dcmread(dcm_path)
                    
                    # Normalize
                    img = normalize_image(ds.pixel_array)
                    
                    # Save as PNG
                    # Use the file name but change extension
                    filename = file.replace('.dcm', '.png')
                    save_path = os.path.join(OUTPUT_DIR, filename)
                    
                    cv2.imwrite(save_path, img)
                    converted_count += 1
                    
                except Exception as e:
                    print(f"Failed to convert {file}: {e}")
    
    print(f"✔ Successfully converted {converted_count} images to PNG.")
    print(f"Saved in: {OUTPUT_DIR}")

if __name__ == "__main__":
    process_dicom_to_png()