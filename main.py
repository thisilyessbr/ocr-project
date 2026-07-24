import pytesseract
from PIL import Image
from extract import extract_fields


def run_pipeline(image_path):
    img = Image.open(image_path)
    raw_text = pytesseract.image_to_string(img)

    print("--- Raw OCR text ---")
    print(raw_text)

    structured = extract_fields(raw_text)

    print("--- Structured output ---")
    print(structured)

if __name__ == "__main__":
  run_pipeline("invoice-sample.jpg")