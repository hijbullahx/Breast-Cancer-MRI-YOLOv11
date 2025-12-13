import os
import pydicom
import matplotlib.pyplot as plt
from tcia_utils.nbia import downloadSeries

# 1. Setup
series_uid = "1.3.6.1.4.1.14519.5.2.1.6279.6001.179049373636438705059720603192"
download_path = "data/raw/Patient_001"

os.makedirs(download_path, exist_ok=True)

# 2. Download Data
series_data = [{"SeriesInstanceUID": series_uid}]

print("Downloading DICOM series from NBIA...")
try:
    downloadSeries(series_data, path=download_path)
    print("✔ Download complete")
except Exception as e:
    print(f"Error: {e}")

# 3. Visualization
dcm_files = []
for root, _, files in os.walk(download_path):
    for f in files:
        if f.lower().endswith(".dcm"):
            dcm_files.append(os.path.join(root, f))

print(f"Found {len(dcm_files)} DICOM files")

if dcm_files:
    ds = pydicom.dcmread(dcm_files[0])
    plt.imshow(ds.pixel_array, cmap="gray")
    plt.axis("off")
    plt.title("Sample MRI Slice")
    # In a script, plt.show() opens a window. In Colab, it prints the image.
    print("✔ Image loaded successfully (Run in Colab to see visual)")
else:
    print("❌ No DICOM files found.")