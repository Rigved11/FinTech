import numpy as np

X = np.array([1, 2, 3, 4])
y = np.array([2, 4, 6, 8])

m = 0
b = 0
lr = 0.01
n = len(X)

# Step 1
y_pred = m * X + b
cost = (1/n) * np.sum((y - y_pred)**2)
dm = (-2/n) * np.sum(X * (y - y_pred))
db = (-2/n) * np.sum(y - y_pred)
m = m - lr * dm
b = b - lr * db
print("Step 1 → m:", m, "b:", b, "cost:", cost)

# Step 2
y_pred = m * X + b
cost = (1/n) * np.sum((y - y_pred)**2)
dm = (-2/n) * np.sum(X * (y - y_pred))
db = (-2/n) * np.sum(y - y_pred)
m = m - lr * dm
b = b - lr * db
print("Step 2 → m:", m, "b:", b, "cost:", cost)

# Repeat same block 3 more times...
y_pred = m * X + b
cost = (1/n) * np.sum((y - y_pred)**2)
dm = (-2/n) * np.sum(X * (y - y_pred))
db = (-2/n) * np.sum(y - y_pred)
m = m - lr * dm
b = b - lr * db
print("Step 3 → m:", m, "b:", b, "cost:", cost)
y_pred = m * X + b
cost = (1/n) * np.sum((y - y_pred)**2)
dm = (-2/n) * np.sum(X * (y - y_pred))
db = (-2/n) * np.sum(y - y_pred)
m = m - lr * dm
b = b - lr * db
print("Step 4 → m:", m, "b:", b, "cost:", cost)
y_pred = m * X + b
cost = (1/n) * np.sum((y - y_pred)**2)
dm = (-2/n) * np.sum(X * (y - y_pred))
db = (-2/n) * np.sum(y - y_pred)
m = m - lr * dm
b = b - lr * db
print("Step 5 → m:", m, "b:", b, "cost:", cost)