import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.arange(-5,6)

print("Values:", x)
print("Sigmoid:", sigmoid(x))