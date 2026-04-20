import pandas as pd

df = pd.read_csv("transactions.csv")

df["timestamp"] = pd.to_datetime(df["timestamp"])

df = df.sort_values(by=["account_id", "timestamp"])

print("Unique accounts:", df["account_id"].nunique())
print(df["account_id"].value_counts())