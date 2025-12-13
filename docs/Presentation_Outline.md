# Thesis Presentation Outline

## Slide 1: Title Slide
* **Title:** Breast Cancer Detection and Classification using YOLOv11 from MRI Images.
* **Authors:** Hijbullah & Masud.
* **Supervisor:** [Supervisor Name].

## Slide 2: Introduction
* **Statistic:** Breast cancer is the #1 cancer in women.
* **Problem:** MRI analysis is slow and hard for doctors.
* **Solution:** AI (YOLOv11) can help detect tumors faster.

## Slide 3: Literature Review
* **Existing Methods:** CNNs, Faster R-CNN (Slow).
* **Research Gap:** Lack of real-time detection on 3D MRI data.
* **Why YOLOv11?** It is the state-of-the-art for speed and accuracy (2024/2025).

## Slide 4: Methodology (The Pipeline)
* **Dataset:** Duke Breast Cancer MRI (TCIA).
* **Preprocessing:** DICOM -> PNG -> Normalization.
* **Model:** YOLOv11 (Custom Head for Benign/Malignant).
* **Training:** Transfer Learning on NVIDIA T4 GPU.

## Slide 5: Expected Results
* **Metric:** mAP@50 > 0.85.
* **Speed:** < 50ms per image.
* **Visuals:** Bounding boxes around tumors.

## Slide 6: Timeline (Gantt Chart)
* **Phase 1:** Setup (Completed).
* **Phase 2:** Data Collection (Next).
* **Phase 3:** Model Training.
* **Phase 4:** Evaluation & Writing.