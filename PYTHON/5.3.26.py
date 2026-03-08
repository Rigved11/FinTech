import numpy as np

X = np.array([[1000, 2],
              [2000, 1],
              [3000, 4]])

mean = np.mean(X, axis=0)
std = np.std(X, axis=0)

X_scaled = (X - mean) / std

print("Scaled X:")
print(X_scaled)