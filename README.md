# Deepfake Detection System

## Overview
This project is an end-to-end deepfake detection system built using deep learning techniques.
It focuses on identifying manipulated (deepfake) media by training and evaluating a neural network model on real-world datasets.

The project was developed to gain practical experience in computer vision, model training, and evaluation beyond academic coursework.

---

## Key Features
- Deepfake detection using a trained deep learning model
- Dataset preprocessing and reduction for efficient training
- Model evaluation on unseen samples
- Modular and script-based implementation

---

## Tech Stack
- Python
- TensorFlow / Keras
- OpenCV
- NumPy
- Matplotlib

---

## Project Structure
deepfake_detection.py # Model training logic
reduce_dataset.py # Dataset preprocessing and reduction
test_deepfake.py # Model testing and inference
local.py # Helper and utility functions
deepfake_detector_model.h5 # Trained model


---

## How It Works
1. The dataset is cleaned and reduced to balance classes and improve training efficiency.
2. A deep learning model is trained to learn distinguishing features between real and fake media.
3. The trained model is evaluated using test samples to measure performance.
4. The system predicts whether a given input is real or deepfake.

---

## Results
- Training Accuracy: ~87%
- Validation Accuracy: ~71%
- Test Accuracy: ~70%

The model demonstrates consistent learning behavior and reasonable generalization on unseen data.

---

## How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/deepfake-detection.git
cd deepfake-detection
