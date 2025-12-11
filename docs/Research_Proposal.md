# Thesis Proposal: Breast Cancer Detection and Classification using YOLOv11 from MRI Images

**Authors:** Hijbullah & Masud  
**Date:** December 2025  

## 1. Problem Statement
Manual interpretation of Breast MRI scans (DICOM) is time-consuming and prone to human error. We need an automated system to assist doctors. We will use **YOLOv11** because it is faster and more accurate than older models for detecting objects in real-time.

## 2. Research Objectives
1.  **Dataset:** Create a clean dataset from the DUKE Breast Cancer MRI collection.
2.  **Model:** Adapt YOLOv11 to detect tumors and classify them (Benign vs. Malignant).
3.  **Target:** Achieve >85% accuracy (mAP).
4.  **Hardware:** Optimize the model to run efficiently on a standard GPU (Tesla T4).

## 3. Methodology
* **Input:** MRI Images (DICOM format).
* **Process:** Convert to images -> Train YOLOv11 -> Validate Results.
* **Output:** Bounding boxes around tumors with classification labels.

## 4. Expected Outcomes
* A working Python code pipeline.
* A complete Thesis Paper.
* Performance metrics (Accuracy, Precision, Recall graphs).