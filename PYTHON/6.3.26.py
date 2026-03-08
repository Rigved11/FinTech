import numpy as np

X = np.array([[1,2],
              [2,3],
              [3,4],
              [4,5],
              [5,6]])

y = np.array([3,5,7,9,11])

X_train = X[:4]
y_train = y[:4]

X_test = X[4:]
y_test = y[4:]

W = np.zeros(2)
b = 0
lr = 0.01
epochs = 200
n = len(X_train)

for i in range(epochs):

    y_pred = X_train @ W + b

    dW = (-2/n) * (X_train.T @ (y_train - y_pred))
    db = (-2/n) * np.sum(y_train - y_pred)

    W -= lr * dW
    b -= lr * db

# Prediction
test_pred = X_test @ W + b

print("Test prediction:", test_pred)
print("Actual:", y_test)