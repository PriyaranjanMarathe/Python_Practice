import cv2
import numpy as np
from PIL import Image
import pytesseract

# Set the path to the Tesseract executable (update accordingly)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open the image using Pillow
image_path = r'C:\Users\marat\OneDrive\Documents\CareerPlanning\learning\ocr\Bard_Generated_Image.jpeg'
image = Image.open(image_path)

# Preprocess the image (optional)
# You can add steps like grayscale conversion, noise reduction, etc.

# Extract text using Tesseract
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)
