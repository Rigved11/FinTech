import numpy as np

X = np.array([[1, 2],
              [2, 1],
              [3, 4]])

y = np.array([5, 6, 9])

W = np.zeros(2)
b = 0
n = len(X)

y_pred = X @ W + b

dW = (-2/n) * (X.T @ (y - y_pred))
db = (-2/n) * np.sum(y - y_pred)

print("dW:", dW)
print("db:", db)