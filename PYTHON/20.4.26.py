import pandas as pd

# Load your dataset (replace 'your_dataset.csv' with your actual file path)
df = pd.read_csv('fraud_data.csv')

# Print the first 5 rows
print("--- First 5 Rows ---")
print(df.head())

# Print the shape of the dataset (rows, columns)
print("\n--- Shape of Dataset ---")
print(df.shape)

# Identify numerical and categorical columns
numerical_cols = df.select_dtypes(include=['number']).columns
categorical_cols = df.select_dtypes(include=['object', 'category']).columns

print(f"\nNumber of numerical columns: {len(numerical_cols)}")
print(f"Number of categorical columns: {len(categorical_cols)}")

# Print count of missing values in each column
print("\n--- Missing Values Count ---")
print(df.isnull().sum())