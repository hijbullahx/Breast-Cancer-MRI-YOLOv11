# Breast Cancer Detection using YOLOv11

![YOLOv11](https://img.shields.io/badge/YOLOv11-Object_Detection-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Research_Complete-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

## 📌 Project Overview

This project implements an automated AI pipeline to detect breast cancer tumors in MRI scans. Utilizing the state-of-the-art **YOLOv11** architecture, the system was trained on the **Duke Breast Cancer MRI Dataset** to identify invasive breast cancer with high precision.

The model acts as a diagnostic assistant, providing a "second opinion" overlay that highlights potential tumor regions in MRI slices, aiming to reduce false negatives in clinical settings.

---

## 📊 Research Results

The model was trained on **1,007 MRI slices** and achieved performance metrics suitable for academic publication.

### **Performance Metrics**
| Metric | Score | Interpretation |
| :--- | :--- | :--- |
| **mAP@50** | **0.917** | **Excellent:** The model correctly identifies tumors 91.7% of the time. |
| **Precision** | **0.981** | **High Confidence:** When the AI predicts a tumor, it is 98% likely to be correct. |
| **Recall** | **0.812** | **Sensitivity:** The AI detects 81.2% of all tumors present in the test set. |

### **Confusion Matrix Analysis**
* **True Positives (171):** Tumors correctly detected.
* **False Positives (31):** Healthy tissue incorrectly flagged as tumor (Low False Alarm rate).
* **False Negatives (23):** Tumors missed by the model.

---

## 📂 Repository Structure

```text
├── src/
│   ├── process_labels.py       # Converts clinical annotations to YOLO format
│   ├── split_duke_data.py      # Splits dataset into Train (80%) and Val (20%)
│   ├── refined_inference.py    # Generates professional visualization (Green/Red boxes)
│   └── visualize_results.py    # Debugging tool for model predictions
├── configs/
│   └── duke.yaml               # YOLOv11 Dataset Configuration
├── notebooks/                  # Google Colab experiments & training logs
└── models/                     # Trained weights (best.pt)
```

---

## 🚀 Installation & Usage

### 1. Prerequisites

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/hijbullahx/Breast-Cancer-MRI-YOLOv11.git
cd Breast-Cancer-MRI-YOLOv11
pip install ultralytics opencv-python matplotlib pandas seaborn
```

### 2. Data Setup

1. Download the **Duke Breast Cancer MRI Dataset**.
2. Organize it into Google Drive or local storage.
3. Update `configs/duke.yaml` with your specific data path.

### 3. Training

To retrain the model from scratch using the YOLO command line interface:

```bash
yolo task=detect mode=train model=yolo11n.pt data=configs/duke.yaml epochs=50 imgsz=512
```

### 4. Inference (Visualization)

To run the model on a new MRI scan and generate the "Ground Truth vs. AI" comparison:

```bash
python src/refined_inference.py
```

## 👥 Authors

* **Md. Taher Bin Omar Hijbullah**
* **Masud Rana**