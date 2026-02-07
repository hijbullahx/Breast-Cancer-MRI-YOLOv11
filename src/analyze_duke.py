import os
import pandas as pd

# Configuration
DATA_ROOT = "data/duke_raw"
CSV_PATH = os.path.join(DATA_ROOT, "metadata.csv")

def analyze_dataset_structure():
    print("--- P5.T2: Duke Dataset Analysis ---")
    
    # 1. Inspect Metadata CSV
    if os.path.exists(CSV_PATH):
        print(f"\nLoading {CSV_PATH}...")
        df = pd.read_csv(CSV_PATH)
        print("✔ Metadata Loaded Successfully.")
        print(f"Total Rows: {len(df)}")
        print("\n--- Columns ---")
        print(df.columns.tolist())
        print("\n--- First 5 Rows ---")
        print(df.head())
        
        # Check class balance if 'Diagnosis' or 'Class' exists
        # (We will know the exact column name after you run this)
    else:
        print("❌ Metadata CSV not found!")

    # 2. Inspect One Patient's Folder Structure
    # Let's pick a random patient folder found in the root
    subdirs = [d for d in os.listdir(DATA_ROOT) if os.path.isdir(os.path.join(DATA_ROOT, d))]
    
    if subdirs:
        sample_patient = subdirs[0] # Pick the first one
        patient_path = os.path.join(DATA_ROOT, sample_patient)
        
        print(f"\n--- Structure of Patient: {sample_patient} ---")
        # List sequences (sub-folders inside the patient)
        sequences = os.listdir(patient_path)
        for seq in sequences:
            seq_path = os.path.join(patient_path, seq)
            if os.path.isdir(seq_path):
                num_slices = len(os.listdir(seq_path))
                print(f"  📂 Sequence: {seq} ({num_slices} slices)")
            else:
                print(f"  📄 File: {seq}")
    else:
        print("❌ No patient folders found in data root.")

if __name__ == "__main__":
    analyze_dataset_structure()