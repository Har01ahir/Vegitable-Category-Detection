# Onion Category Detection

Onion Category Detection is a simple image classification project that detects and categorizes different types of onions using deep learning.  

## Repository Structure
- `model/` – Contains the trained model files
- `data/` – Dataset of onion images (if included)
- `predict.py` – Script to make predictions on new onion images
- `train.py` – Script to train the model (if dataset is available)

## Features
- Classifies different types of onions
- Easy-to-use prediction script for new images
- Lightweight and suitable for beginners in image classification

## Installation
- Create a virtual environment and activate it (optional but recommended):

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate```bash

### Install dependencies:

pip install -r requirements.txt

**Make sure Python 3.8 or higher is installed**

## Usage

- Predict on a new onion image:

python predict.py --image path_to_image.jpg```
