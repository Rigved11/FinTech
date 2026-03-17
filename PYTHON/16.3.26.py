import numpy as np
from sklearn.linear_model import LogisticRegression

X = np.array([[1],[2],[3],[4],[5]])
y = np.array([0,0,0,1,1])

model = LogisticRegression()

model.fit(X, y)

pred = model.predict(X)

print(pred)

print("Predictions:", pred)
print("Coefficient:", model.coef_)
print("Intercept:", model.intercept_)