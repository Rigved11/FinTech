import pandas as pd

# Load data
df = pd.read_csv("student_exam_data.csv")

# Preview
print(df.head())

# Info
print(df.info())

# Statistics
print(df.describe())

# Shape
print("Rows and Columns:", df.shape)

# Rename columns
df.columns = ["study_hours", "prev_score", "result"]

# Class balance
print(df["result"].value_counts())