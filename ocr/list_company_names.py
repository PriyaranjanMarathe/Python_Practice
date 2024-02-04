import cv2
import numpy as np
from PIL import Image
import pytesseract

# Set the path to the Tesseract executable (update accordingly)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open the image using Pillow
image_path = r'C:\Users\marat\OneDrive\Documents\CareerPlanning\learning\ocr\dish_network_200_vendors.jpg'
image = Image.open(image_path)

# Use pytesseract to extract text
text = pytesseract.image_to_string(image)

# Convert Pillow image to OpenCV format
opencv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

# Load the pre-trained Haarcascades classifier for logo detection
logo_cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

# Convert the image to grayscale for logo detection
gray = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2GRAY)

# Perform logo detection
logos = logo_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Extract and print company names from text and logos
text_company_names = [name.strip() for name in text.split('\n') if name.strip()]
logo_company_names = ['Company Logo' for _ in range(len(logos))]
all_company_names = text_company_names + logo_company_names

print(all_company_names)
