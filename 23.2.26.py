import numpy as np

X = np.array([1, 2, 3, 4])
y = np.array([2, 4, 6, 8])

m = 1
b = 0

y_pred = m * X + b
cost = np.mean((y - y_pred) ** 2)

print("Cost:", cost)