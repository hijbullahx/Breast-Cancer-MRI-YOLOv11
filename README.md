# 🎗️ Breast Cancer Detection & Classification using YOLOv11 on MRI

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-v2.2-red)
![YOLOv11](https://img.shields.io/badge/YOLO-v11-green)
![Status](https://img.shields.io/badge/Status-Research_Phase-orange)

> **Thesis Project** by Hijbullah & Masud  
> **Target:** Automated detection of benign vs. malignant lesions in Breast MRI (DICOM).

---

## 📖 Table of Contents
1. [Project Overview](#-project-overview)
2. [Key Features](#-key-features)
3. [Dataset](#-dataset)
4. [Installation & Setup](#-installation--setup)
5. [Documentation](#-documentation)

---

## 🔍 Project Overview
Breast cancer is the leading cause of cancer-related mortality among women. Early detection via MRI is crucial but manual interpretation is error-prone. This project leverages **Ultralytics YOLOv11** to:
1.  **Localize** tumors in 3D MRI slices.
2.  **Classify** them as **Benign** or **Malignant**.
3.  **Accelerate** diagnosis using GPU-optimized inference.

## 🌟 Key Features
* **DICOM Preprocessing:** Automatic conversion of medical images to deep-learning-ready formats.
* **Real-Time Detection:** Sub-50ms inference speed using YOLOv11.
* **Reproducible Pipeline:** Deterministic training with fixed seeds.

## 📊 Dataset
We use the **Duke Breast Cancer MRI Dataset** hosted on TCIA.
* **Source:** [The Cancer Imaging Archive (TCIA)](https://www.cancerimagingarchive.net/collection/duke-breast-cancer-mri/)
* **Format:** DICOM
* **Pre-processing:** Handled via Google Colab.

## ⚙️ Installation & Setup
This project is designed to run on **Google Colab** (for training) and **VS Code** (for development).

## 🚀 Training
To train the model on the MRI dataset, run the following command:

```bash
python src/train.py --epochs 50 --batch 16

```bash
# Clone the repository
git clone [https://github.com/hijbullahx/Breast-Cancer-MRI-YOLOv11.git](https://github.com/hijbullahx/Breast-Cancer-MRI-YOLOv11.git)

# Install dependencies
pip install -r requirements.txt