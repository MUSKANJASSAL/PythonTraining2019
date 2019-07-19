import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

image = cv2.imread("data.png", 1)
print(image) # Numpy Array

print("=============")

text = pytesseract.image_to_string(image)
print(text)

# Scan an Image : eg: Blood Report Sample
# Extract Textual Data analyze it with datasets available
# Perform supervised Learning with Regression


# https://gtts.readthedocs.io/en/latest/module.html#examples
# https://pypi.org/project/SpeechRecognition/