from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
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
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Train
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict
pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, pred)
print("Accuracy:", accuracy)

# New prediction
new_pred = model.predict([[5]])
print("Prediction for 5 hours:", new_pred)