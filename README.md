# Breast Cancer Detection using YOLOv11

![Project Banner](https://img.shields.io/badge/YOLOv11-Object_Detection-blue) ![Python](https://img.shields.io/badge/Python-3.10%2B-green) ![Status](https://img.shields.io/badge/Status-Research_Complete-success)

## 📌 Project Overview
This project implements an automated AI pipeline to detect breast cancer tumors in MRI scans. Utilizing the **YOLOv11** architecture, the system was trained on the **Duke Breast Cancer MRI Dataset** (922 patients) to identify invasive breast cancer with high precision.

The model is designed to assist radiologists by providing a "second opinion" overlay, highlighting potential tumor regions in MRI slices.

## 📊 Final Performance Results
The model was trained on **1,007 MRI slices** and achieved research-grade performance, suitable for academic publication.

| Metric | Score | Interpretation |
| :--- | :--- | :--- |
| **mAP@50** | **0.917** | **Excellent:** The model correctly identifies tumors 91.7% of the time. |
| **Precision** | **0.981** | **High Confidence:** When the AI predicts a tumor, it is 98% likely to be correct. |
| **Recall** | **0.812** | **Sensitivity:** The AI detects 81.2% of all tumors present in the test set. |

### Confusion Matrix Analysis
* **True Positives (171):** Tumors correctly detected.
* **False Positives (31):** Healthy tissue incorrectly flagged as tumor (Low False Alarm rate).
* **False Negatives (23):** Tumors missed by the model.

## 📂 Repository Structure
```text
├── src/
│   ├── process_labels.py       # Converts Duke annotations to YOLO format
│   ├── split_duke_data.py      # Splits data into Train (80%) and Val (20%)
│   ├── refined_inference.py    # Generates non-overlapping visualization
│   └── visualize_results.py    # Debugging tool for model predictions
├── configs/
│   └── duke.yaml               # YOLOv11 Dataset Configuration
├── notebooks/                  # Google Colab experiments
└── README.md                   # Project Documentation