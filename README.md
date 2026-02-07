# Breast Cancer Detection using YOLOv11

## 📌 Project Overview
This project implements an automated pipeline to detect breast cancer tumors in MRI scans using the **YOLOv11** object detection model. The system is trained on the **Duke Breast Cancer MRI Dataset** (922 patients).

## 📊 Performance (Phase 5 Results)
* **mAP@50:** 0.917 (91.7% Accuracy)
* **Precision:** 0.98
* **Recall:** 0.81

## 📂 Repository Structure
* `src/`: Data processing and training scripts.
* `configs/`: YOLOv11 configuration files.
* `notebooks/`: Colab notebooks for execution.

## 🚀 How to Run
1.  **Setup:** Clone the repo and install dependencies (`pip install ultralytics`).
2.  **Data:** Place Duke MRI dataset in Google Drive.
3.  **Train:** Run `src/train.py`.
4.  **Inference:** Run `src/refined_inference.py` to visualize results.

## 📈 Key Features
* **Automatic Preprocessing:** Converts DICOM/NIfTI to PNG.
* **Intelligent Labeling:** Maps clinical data to image slices.
* **Professional Visualization:** Non-overlapping Ground Truth vs. AI labels.

## 👥 Contributors
* **Hijbullah**
* **Masud** 