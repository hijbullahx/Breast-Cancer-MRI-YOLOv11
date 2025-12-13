import os
import pydicom
import matplotlib.pyplot as plt
import sys

# Install package if not exists (Only for Colab/Local execution, not for file saving)
try:
    import tcia_utils
except ImportError:
    os.system('pip install tcia-utils')
    from tcia_utils import nbi

# 1. Setup
# This Series Instance UID belongs to a specific scan of Patient 001 from the Duke Dataset
# We use this to test if we can grab data from the internet.
series_uid = "1.3.6.1.4.1.14519.5.2.1.6279.6001.179049373636438705059720603192" 
download_path = "data/raw/Patient_001"

# 2. Download Data (Using TCIA API)
print("Downloading DICOM sample...")
try:
    # downloadSeries returns the number of files downloaded or list of files
    data = nbi.downloadSeries(seriesInstanceUID=series_uid, downloadPath=download_path)
    print(f"✔ Download Complete. Files saved to: {download_path}")
except Exception as e:
    print(f"Error downloading: {e}")

# 3. Visualize the first DICOM image
try:
    # Find the first .dcm file
    found = False
    for root, dirs, files in os.walk(download_path):
        for file in files:
            if file.endswith(".dcm"):
                dcm_path = os.path.join(root, file)
                ds = pydicom.dcmread(dcm_path)
                
                # Plot
                plt.figure(figsize=(6,6))
                plt.imshow(ds.pixel_array, cmap=plt.cm.gray)
                plt.title(f"Patient 001 - MRI Slice")
                plt.axis('off')
                plt.show()
                print("✔ Visualization Successful: Image displayed.")
                found = True
                break 
        if found: break
    
    if not found:
        print("⚠ No .dcm files found. Download might have failed.")

except Exception as e:
    print(f"Visualization Error: {e}")