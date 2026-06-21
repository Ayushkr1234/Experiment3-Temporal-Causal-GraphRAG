import pandas as pd

df = pd.read_excel("data/attackmitre.xlsx")

print(df.iloc[0]["APT Group Name"])
print()
print(df.iloc[0]["Software Techniques"])