from sklearn.linear_model import LogisticRegression
import pandas as pd

# Dataset
data = {
    "hours": [1,2,3,4,5,6],
    "result": [0,0,0,1,1,1]
}

df = pd.DataFrame(data)
X = df[["hours"]]
y = df["result"]

# Model
model = LogisticRegression()
model.fit(X, y)

# Predictions
pred = model.predict(X)
prob = model.predict_proba(X)

print("Predictions:", pred)
print("Probabilities:\n", prob)

# Comparison
print("\nActual:", list(y))
print("Predicted:", list(pred))
