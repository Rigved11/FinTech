import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load encoded dataset
df = pd.read_csv("student_exam_data.csv")

# Apply encoding again (if not saved)
df = pd.get_dummies(df, columns=["gender", "branch"], drop_first=True)

# Separate features and target
X = df.drop("pass", axis=1)   # assuming 'pass' is target column
y = df["pass"]

# Train-test split (70-30)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

print("Model trained successfully!")