import json

with open(
    "output/Extracted_data_1.json",
    "r",
    encoding="utf-8"
) as f:
    data = json.load(f)

print("JSON loaded successfully")
print(data.keys())