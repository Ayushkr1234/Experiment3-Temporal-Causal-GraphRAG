import pandas as pd

mitre = pd.read_excel("data/MitreEnterprise.xlsx")

print("First 5 rows:")
print(mitre.head())

print("\nColumns:")
print(list(mitre.columns))