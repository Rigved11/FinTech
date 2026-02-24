import numpy as np

X = np.array([1, 2, 3, 4])
y = np.array([2, 4, 6, 8])

m = 0
b = 0

n = len(X)

y_pred = m * X + b

dm = (-2/n) * np.sum(X * (y - y_pred))
db = (-2/n) * np.sum(y - y_pred)

print("dm:", dm)
print("db:", db)