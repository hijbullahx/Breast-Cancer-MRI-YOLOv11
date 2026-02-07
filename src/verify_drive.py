import os
from google.colab import drive

# --- CORRECTED CONFIGURATION ---
# Using your exact path:
DRIVE_ROOT = "/content/drive/MyDrive/duke_processed_images"

def check_manual_folder():
    print(f"--- P5.T1: Inspecting {DRIVE_ROOT} ---")

    # 1. Mount Drive
    if not os.path.exists('/content/drive'):
        print("Mounting Google Drive...")
        drive.mount('/content/drive')

    # 2. Verify Folder Exists
    if not os.path.exists(DRIVE_ROOT):
        print(f"❌ Error: Folder not found at {DRIVE_ROOT}")
        print("   Please check the spelling carefully in your Google Drive.")
        return

    print(f"✔ Found folder: {DRIVE_ROOT}")

    # 3. What is inside?
    contents = os.listdir(DRIVE_ROOT)
    print(f"Total items in root: {len(contents)}")
    print(f"First 5 items: {contents[:5]}")

    # 4. Deep Check (Are they Patient Folders or Images?)
    # We check the first item to see what it is
    first_item = os.path.join(DRIVE_ROOT, contents[0])
    
    if os.path.isdir(first_item):
        print("\nType: 📂 FOLDERS detected (Likely Raw Data)")
        # Check inside the first folder
        sub_contents = os.listdir(first_item)
        print(f"Inside {contents[0]}: {sub_contents[:3]}")
        if any(f.endswith('.dcm') for f in sub_contents):
            print("✔ .dcm files found (Needs Conversion)")
        else:
            print("⚠ No .dcm files in the first folder. Checking deeper...")
            
    elif first_item.endswith('.png') or first_item.endswith('.jpg'):
        print("\nType: 🖼 IMAGES detected (Already Processed)")
        print("✔ We can skip DICOM conversion!")
        
    elif first_item.endswith('.zip'):
        print("\nType: 📦 ZIP file detected. Do you need to unzip it?")

    # 5. Check for Metadata
    if "metadata.csv" in contents:
        print("\n✔ Found 'metadata.csv'")
    else:
        print("\n⚠ 'metadata.csv' NOT found in root.")

if __name__ == "__main__":
    check_manual_folder()