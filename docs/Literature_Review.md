# Literature Review: YOLO and Deep Learning in Breast MRI

**Summary of Related Works**

## 1. Paper: "Deep Learning for Breast MRI" (2021)
* **Method:** Used 2D CNN (ResNet) to classify slices.
* **Limitation:** Did not use object detection (YOLO), only classification. Slow inference time.
* **Relevance:** Shows that Deep Learning works on MRI, but we can improve speed.

## 2. Paper: "YOLOv5 for Breast Tumor Detection in Mammograms" (2023)
* **Method:** Applied YOLOv5 to X-ray images (Mammography).
* **Result:** Achieved 89% mAP.
* **Gap:** This was done on X-rays, not MRI. MRI is 3D and more complex.
* **Our Contribution:** We will apply a newer model (YOLOv11) to the more complex MRI dataset.

## 3. Paper: "Automated Breast Cancer Detection using Faster R-CNN" (2022)
* **Method:** Used Faster R-CNN on MRI.
* **Result:** High accuracy (90%) but very slow (0.5 seconds per image).
* **Gap:** Not suitable for real-time applications.
* **Our Contribution:** YOLOv11 is much faster (<0.05 seconds) with similar accuracy.

## Conclusion
Most existing work focuses on Mammography or uses slow models like Faster R-CNN on MRI. There is a clear gap for a **real-time, high-accuracy detector like YOLOv11 on MRI data**.