import pandas as pd

df = pd.read_csv("transactions.csv")

df["timestamp"] = pd.to_datetime(df["timestamp"])

df = df.sort_values(by=["account_id", "timestamp"])

print("Unique accounts:", df["account_id"].nunique())
print(df["account_id"].value_counts())

df["rolling_sum"] = df.groupby("account_id")["amount"] \
    .rolling(window=3, min_periods=1) \
    .sum() \
    .reset_index(0, drop=True)

print(df.head(10))
df = df.set_index("timestamp")

df["rolling_24hr"] = df.groupby("account_id")["amount"] \
    .rolling("24H") \
    .sum() \
    .reset_index(0, drop=True)

print(df.head(10))
df["txn_count_24hr"] = df.groupby("account_id")["amount"] \
    .rolling("24H") \
    .count() \
    .reset_index(0, drop=True)

df["flag"] = (df["rolling_24hr"] > 20000) & (df["txn_count_24hr"] >= 3)

print(df[df["flag"] == True])

print("Suspicious accounts:",
      df[df["flag"]]["account_id"].nunique())