import pandas as pd

df = pd.read_csv("student_exam_data_messy.csv")

df["study_hours"].fillna(df["study_hours"].mean(), inplace=True)
df["prev_score"].fillna(df["prev_score"].mean(), inplace=True)

print(df.isnull().sum())