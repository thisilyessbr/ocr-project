import requests
import json

def extract_fields(raw_text):

    prompt = f"""You are a document extraction assistant.
Given this raw OCR text, extract the following fields and respond
ONLY with valid JSON, no other words:

document_type, date, sender, total_amount, key_line_items (array)

OCR text:
{raw_text}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.1",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()
    ai_output = result["response"]

    cleaned = ai_output.replace("```json", "").replace("```", "").strip()

    try:
       return json.loads(cleaned)
    except json.JSONDecodeError:
        print("Model didn't return clean JSON, raw output was:")
        print(ai_output)
        return None





