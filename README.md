# AI-ML-DAY-2

# 🍕 Food Classification using YOLOv8 (Pretrained)

This project focuses on building a **production-grade food image classifier** using the **YOLOv8 classification head (`yolov8n-cls.pt`)**, fine-tuned on a subset of the **Food-101 dataset**.

Currently, we are using **5 classes**:
- `pizza`
- `grilled_chicken`
- `sushi`
- `ice_cream`
- `hamburger`

The classifier is designed to be **fast**, **lightweight**, and **highly accurate**, suitable for real-time applications.

---

## ✅ Features

- YOLOv8 Classification Head (Pretrained on ImageNet)
- Albumentations for advanced image augmentation
- Cosine Annealing LR Scheduler
- Clean configuration class
- Logging system for tracking training

---

## 🧠 Model & Dataset

- **Model**: `yolov8n-cls.pt` (YOLOv8 nano)
- **Dataset**: Food-101 (only 5 selected classes used for now)

Folder structure (in progress):


## 📌 Current Status

🟡 **Work in progress**

- [x] Initial config and setup
- [x] Preprocessing + augmentation pipeline
- [x] Dataset structure
- [ ] Model training loop (coming soon)
- [ ] Evaluation + metrics
- [ ] Model saving and inference

📓 Notebook
All code is inside:
Food_Classification_YOLOv8_Module12.ipynb

🚀 To Do (Tomorrow’s Plan)
Implement the FoodDataset class with Albumentations

Add the training + validation loop

Save and test the fine-tuned model

Maybe test with yolov8s-cls.pt for better accuracy
