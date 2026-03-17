import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

hours = np.array([1,2,3,4,5])

W = 1.2
b = -4

z = W*hours + b
prob = sigmoid(z)

print("Probabilities:", prob)

predicted = (prob >= 0.5).astype(int)

actual = np.array([0,0,0,1,1])

correct = np.sum(predicted == actual)

print("Predicted:", predicted)
print("Actual:", actual)
print("Correct Predictions:", correct)