import pytesseract
from PIL import Image

image_path = "invoice-sample.jpg"
img = Image.open(image_path)

text  = pytesseract.image_to_string(img)
print(text)