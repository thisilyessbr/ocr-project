# OCR Invoice Extraction Pipeline

A Python-based Optical Character Recognition (OCR) system designed to extract structured data from invoice images using pytesseract and AI-powered field extraction.

## 📋 Project Overview

This project automates the process of reading invoices from images and extracting key business information such as:
- Document type
- Date
- Sender information  
- Total amount
- Key line items (products/services)

## 🚀 Features

- **OCR Processing**: Uses pytesseract for text extraction from images
- **Image Preprocessing**: OpenCV-based preprocessing to improve OCR accuracy
- **AI-powered Extraction**: LLM-based field extraction for structured output
- **JSON Output**: Clean, parseable JSON responses from AI model

## 📁 Project Structure

```
ocr-project/
├── main.py              # Main entry point - runs full OCR pipeline
├── extract.py           # AI-based field extraction using LLM
├── ocr_test.py          # Simple OCR test script
├── preprocess.py        # Image preprocessing with OpenCV
├── invoice-sample.jpg   # Sample invoice image for testing
└── README.md            # This file
```

## 🛠️ Dependencies

### Python Packages
```bash
pip install pytesseract pillow requests opencv-python
```

### System Requirements
- Tesseract OCR installed on your system
  ```bash
  # Windows (from Scoop)
  scoop install tesseract
  
  # Or download from https://github.com/tesseract-ocr/tesseract/releases
  ```
- OpenCV for image processing
- LLM service running locally (e.g., llama.cpp with Ollama)

## 🏃 Running the Project

### Basic Usage

Run the main pipeline:
```bash
python main.py
```

This will:
1. Load the sample invoice image (`invoice-sample.jpg`)
2. Extract raw text using OCR
3. Send the text to an LLM for field extraction
4. Output both raw and structured JSON data

### Test Script

Run a simple OCR test:
```bash
python ocr_test.py
```

## 🤖 LLM Configuration

The `extract.py` module connects to a local LLM service via Ollama. Make sure you have:

1. **Ollama installed**: https://ollama.ai
2. **LLM model downloaded**:
   ```bash
   ollama pull llama3.1
   ```
3. **Service running on localhost:11434**

## 📊 Example Output

```
--- Raw OCR text ---
INVOICE #12345
Date: 2026-07-01
From: ABC Company
To: XYZ Corp
Items:
  - Software License: $100.00
  - Support Package: $50.00
Total Amount: $150.00

--- Structured output ---
{"document_type": "invoice", "date": "2026-07-01", "sender": "ABC Company", ...}
```

## 📝 Notes

- The sample invoice (`invoice-sample.jpg`) should be placed in the project directory
- LLM response is cleaned to extract valid JSON (removes markdown code blocks)
- Error handling is included for cases where the AI model doesn't return clean JSON

## 🔧 Customization

Modify the `prompt` variable in `extract.py` to customize which fields you want to extract or change the extraction schema.

---

Built with Python, pytesseract, Ollama/LLM, and OpenCV.