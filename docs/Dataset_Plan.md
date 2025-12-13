# Dataset Acquisition Plan

## 1. Source
**Duke Breast Cancer MRI Dataset** (The Cancer Imaging Archive).
* **URL:** https://www.cancerimagingarchive.net/collection/duke-breast-cancer-mri/
* **Format:** DICOM (3D Medical Images).
* **Size:** ~68 GB (We will download subsets).

## 2. Platform Strategy: Google Colab
* **Storage:** We will mount Google Drive to store processed data.
* **Compute:** Google Colab T4 GPU.
* **Download Method:** We will use the `tcia_utils` Python library or direct HTTP download commands in Colab.

## 3. Workflow
1.  Clone this GitHub repo into Colab.
2.  Download patient data using TCIA API.
3.  Convert DICOM to PNG.
4.  Train YOLOv11.