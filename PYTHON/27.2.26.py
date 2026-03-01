import numpy as np

# ==============================
# DATASET (You can modify noise here)
# ==============================

X = np.array([1, 2, 3, 4, 5])

# Slightly noisy data
y = np.array([2.1, 3.9, 6.2, 8.1, 10.2])

# Try stronger noise (uncomment to test)
# y = np.array([2.5, 3.0, 6.8, 7.0, 11.0])

# ==============================
# INITIAL PARAMETERS
# ==============================

m = 0
b = 0
lr = 0.01
epochs = 200
n = len(X)

# ==============================
# TRAINING LOOP
# ==============================

for i in range(epochs):
    y_pred = m * X + b
    
    # Mean Squared Error
    cost = (1/n) * np.sum((y - y_pred)**2)
    
    # Gradients
    dm = (-2/n) * np.sum(X * (y - y_pred))
    db = (-2/n) * np.sum(y - y_pred)
    
    # Update parameters
    m = m - lr * dm
    b = b - lr * db

# ==============================
# FINAL RESULTS
# ==============================

final_predictions = m * X + b
final_cost = (1/n) * np.sum((y - final_predictions)**2)

print("Final m:", round(m, 4))
print("Final b:", round(b, 4))
print("Final Cost (MSE):", round(final_cost, 6))

print("\nActual vs Predicted")
print("----------------------")
for actual, pred in zip(y, final_predictions):
    print(f"Actual: {actual:.2f}  |  Predicted: {pred:.2f}")