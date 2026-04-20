import pandas as pd

df = pd.read_csv("student_exam_data_messy.csv")

df_encoded = pd.get_dummies(df, columns=["gender", "branch"], drop_first=True)

print(df_encoded.head())
print("Total columns:", len(df_encoded.columns))