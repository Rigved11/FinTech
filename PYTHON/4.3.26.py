import numpy as np

X = np.array([[1, 2],
              [2, 1],
              [3, 4]])

y = np.array([5, 6, 9])

W = np.zeros(2)
b = 0
lr = 0.01
epochs = 200
n = len(X)

for i in range(epochs):

    y_pred = X @ W + b

    cost = np.mean((y - y_pred)**2)

    dW = (-2/n) * (X.T @ (y - y_pred))
    db = (-2/n) * np.sum(y - y_pred)

    W = W - lr * dW
    b = b - lr * db

    if i % 20 == 0:
        print(f"Epoch {i}, Cost {cost}")

print("Final W:", W)
print("Final b:", b)