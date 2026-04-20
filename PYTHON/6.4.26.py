import pandas as pd

df = pd.read_csv("student_exam_data_messy.csv")

print(df.head())
print(df.info())

print("Missing values:\n", df.isnull().sum())

print("Gender values:", df["gender"].unique())
print("Branch values:", df["branch"].unique())