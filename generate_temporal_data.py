import pandas as pd

df = pd.read_csv(
    "rgcn_triples.csv"
)

df["timestamp"] = range(
    len(df)
)

df.to_csv(
    "temporal_triples.csv",
    index=False
)

print(df.head())