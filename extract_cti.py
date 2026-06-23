import google.generativeai as genai
import json

import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")

with open("reports/report1.txt", "r", encoding="utf-8") as f:
    report = f.read()

prompt = f"""
You are a cybersecurity threat intelligence analyst.

Extract CTI knowledge from the given report.

Return only valid JSON.

Extract:
1. Threat actors
2. Malware
3. Tools
4. Vulnerabilities
5. ATT&CK tactics
6. ATT&CK techniques
7. Targets
8. Temporal expressions
9. Entity-relation triples
10. Evidence sentence
11. Confidence score

Input CTI text:
{report}
"""

response = model.generate_content(prompt)

print(response.text)

json_text = response.text.strip()

if json_text.startswith("```json"):
    json_text = json_text[len("```json"):]

if json_text.endswith("```"):
    json_text = json_text[:-3]

json_text = json_text.strip()

with open(
    "output/Extracted_data_1.json",
    "w",
    encoding="utf-8"
) as f:
    f.write(json_text)

print("JSON saved successfully")