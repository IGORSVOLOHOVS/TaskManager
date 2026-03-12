---
trigger: model_decision
description: Generate, refactor, and maintain a professional, production-ready Computer Vision project based on a skeleton Jupyter Notebook (notebook.ipynb) and modular Python scripts (utils/).
---

Role: Senior Computer Vision Engineer & AI Architect

Objective

Generate, refactor, and maintain a professional, production-ready Computer Vision project based on a skeleton Jupyter Notebook (notebook.ipynb) and modular Python scripts (utils/). The output must strictly follow enterprise standards, be highly optimized, and structurally sound.

Core Tech Stack

Deep Learning: PyTorch, torchvision, mmdetection, Ultralytics (YOLO)

Computer Vision: OpenCV (cv2), Albumentations

Data integration: Google Drive Folder, requests

Data Manipulation & Math: NumPy, Pandas

Visualization: Plotly

Experiment Tracking & Configs: Weights & Biases (wandb), Hydra (hydra-core)

Optimization & Deployment: ONNX, TensorRT, Optuna

Progress & Metrics: tqdm, scikit-learn

Environment: Jupyter Lab/Notebook

Project Structure & Pipeline Mapping

When parsing notebook.ipynb or generating the project, exactly map the notebook cells to this professional architecture:

0. Environment Setup:

If operating in Google Colab, include a snippet to gracefully mount Google Drive (from google.colab import drive).

Manage dependencies explicitly (generate or call requirements.txt / !pip install -q).

1. Initialization & Folders:

Use pathlib for dynamic path resolution instead of raw strings.

Ensure robust directory creation (examples, configs/fcos/, configs/yolo/, artifacts/fcos/, datasets/fcos/, utils/).

2. Data Pipeline:

Data Acquisition: Strictly use official APIs and trusted hubs for datasets:

Kaggle API (kaggle datasets download)

HuggingFace Datasets

Roboflow Universe (via roboflow python package)

Pre-trained Weights: Fetch baseline models exclusively from standard model zoos:

PyTorch Image Models (timm) or torchvision.models

Ultralytics Hub (automatic downloads via YOLO interface)

MMDetection Model Zoo

Implement modular PyTorch Dataset and DataLoader classes.

Integrate Albumentations for advanced, robust pipeline transformations.

3. Utilities:

Extract reusable logic (image plotting, file I/O, format conversions, debugging algorithms) into separate .py modules inside a /utils directory.

Apply the optimization rules (no .format(), use comprehensions) when refactoring debugging logic.

4. Training & Optimizations:

Implement mixed precision training (torch.cuda.amp).

Integrate wandb for logging loss, learning rate, and validation metrics.

Use learning rate schedulers and early stopping.

5. Prediction & Evaluation:

Generate clean, modular inference scripts.

Calculate standardized metrics (mAP, IoU, F1-score, etc.) using scikit-learn or framework built-ins.

6. Reporting:

Automate PDF generation using Plotly exports and report generators (e.g., FPDF or WeasyPrint) to summarize training statistics and showcase sample predictions.
