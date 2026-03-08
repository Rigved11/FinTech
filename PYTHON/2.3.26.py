import numpy as np

# 3 samples, 2 features
X = np.array([[1, 2],
              [2, 1],
              [3, 4]])

y = np.array([5, 6, 9])

# Initialize weights
W = np.zeros(2)
b = 0

print("Shape of X:", X.shape)
print("Shape of W:", W.shape)

y_pred = X @ W + b
print("Predictions:", y_pred)