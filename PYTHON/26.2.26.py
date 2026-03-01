


import numpy as np

X = np.array([1, 2, 3, 4])
y = np.array([2, 4, 6, 8])

m = 0
b = 0
lr = 0.01
epochs = 100
n = len(X)

for i in range(epochs):
    y_pred = m * X + b
    
    # Cost (MSE)
    cost = (1/n) * np.sum((y - y_pred)**2)
    
    # Gradients
    dm = (-2/n) * np.sum(X * (y - y_pred))
    db = (-2/n) * np.sum(y - y_pred)

    # Update
    m = m - lr * dm
    b = b - lr * db
    
    # Print every 10 iterations
    if i % 10 == 0:
        print(f"Epoch {i}: Cost = {cost:.4f}")

print("\nFinal m:", m)
print("Final b:", b)