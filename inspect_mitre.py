import pandas as pd

df = pd.read_excel("data/MitreEnterprise.xlsx")

print(df[["Tactic ID", "Tactic Name"]].head(20))