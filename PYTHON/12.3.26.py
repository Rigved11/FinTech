import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

X = np.array([1,2,3,4])

W = 1
b = -3

z = W * X + b

prob = sigmoid(z)

print("Probabilities:", prob)

# Convert probability to class
predicted_class = (prob >= 0.5).astype(int)

print("Predicted class:", predicted_class)