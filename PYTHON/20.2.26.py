
import numpy as np

X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

m = 0
b = 0

y_pred = m * X + b

error = y - y_pred
mse = np.mean(error ** 2)

print("Predictions:", y_pred)
print("MSE:", mse)


import numpy as np

X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

m_values = [0, 1, 2, 3]
b = 0

for m in m_values:
    y_pred = m * X + b
    error = y - y_pred
    mse = np.mean(error ** 2)

    print(f"\nm = {m}")
    print("Predictions:", y_pred)
    print("MSE:", mse)


    m = 2
b = 0
y_pred = m * X + b

print("Predictions when m = 2:", y_pred)

X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 5, 7, 9, 11])   # Slightly changed