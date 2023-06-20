import cv2
import numpy as np

# Load image
img = cv2.imread(r"C:\Users\hardi\Face_detection\Onion_type_detection\OnionData\0.jpg")

# Load YOLO output file in text format
with open(r"C:\Users\hardi\Face_detection\Onion_type_detection\OnionData\0.txt", 'r') as f:
    lines = f.readlines()

# Loop through lines and extract bounding box information
for line in lines:
    # Parse line and extract class, confidence, and bounding box coordinates
    class_id, x, y, w, h = map(float, line.strip().split())

    # Convert relative coordinates to absolute coordinates
    x = int((x - w / 2) * img.shape[1])
    y = int((y - h / 2) * img.shape[0])
    w = int(w * img.shape[1])
    h = int(h * img.shape[0])

    # Define bounding box color based on class ID
    color = (0, 255, 0)  # Default color is green
    if class_id == 1:  # Change color for a specific class ID (here, class 1)
        color = (0, 0, 255)  # Red color for class 1

    # Draw bounding box on the image
    thickness = 2  # Thickness of the bounding box lines
    cv2.rectangle(img, (x, y), (x+w, y+h), color, thickness)

# Show image with bounding boxes
cv2.imshow('Image with bounding boxes', img)
cv2.imwrite(r"C:\Users\hardi\Face_detection\Onion_type_detection\OnionData\Image.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
