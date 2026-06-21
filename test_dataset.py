import pandas as pd

attack = pd.read_excel("data/attackmitre.xlsx")

print("First 5 rows:")
print(attack.head())

print("\nColumns:")
print(list(attack.columns))