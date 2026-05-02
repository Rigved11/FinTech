import pandas as pd

# Load dataset
df = pd.read_csv("student_exam_data.csv")

# One-hot encoding
df_encoded = pd.get_dummies(df, columns=["gender", "branch"], drop_first=True)

# Print updated columns
print("Updated Columns:\n", df_encoded.columns)
print("\nSample Data:\n", df_encoded.head())