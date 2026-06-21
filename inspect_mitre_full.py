import pandas as pd

df = pd.read_excel("data/MitreEnterprise.xlsx")

print("Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nLast 20 rows:")
print(df.tail(20))