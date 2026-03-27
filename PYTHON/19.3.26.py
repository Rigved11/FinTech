from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pandas as pd

# Dataset
data = {
    "hours": [1,2,3,4,5,6,7,8],
    "result": [0,0,0,0,1,1,1,1]
}

df = pd.DataFrame(data)
X = df[["hours"]]
y = df["result"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Model training
model = LogisticRegression()
model.fit(X_train, y_train)

# Prediction
pred = model.predict(X_test)

print("Test Predictions:", pred)
print("Actual:", list(y_test))

