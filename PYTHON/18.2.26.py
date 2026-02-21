import numpy as np

# -----------------------------
# Starter Code
# -----------------------------
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

print("\nElement-wise multiplication (A * B):")
print(A * B)

print("\nMatrix multiplication (A @ B):")
print(A @ B)

print("\n-----------------------------")

# -----------------------------
# Transpose of Matrix A
# -----------------------------
print("Transpose of A:")
print(A.T)

print("\n-----------------------------")

# -----------------------------
# Create 3x2 matrix and reshape to 2x3
# -----------------------------
M = np.array([[1, 2],
              [3, 4],
              [5, 6]])

print("Original 3x2 Matrix:\n", M)
print("Shape:", M.shape)

reshaped_M = M.reshape(2, 3)

print("\nReshaped to 2x3:\n", reshaped_M)
print("New Shape:", reshaped_M.shape)

print("\n-----------------------------")

# -----------------------------
# Dot Product (Vectors)
# -----------------------------
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

# Manual dot product
manual_dot = 0
for i in range(len(v1)):
    manual_dot += v1[i] * v2[i]

print("Manual Dot Product:", manual_dot)

# Using NumPy
print("np.dot():", np.dot(v1, v2))

print("\n-----------------------------")

# -----------------------------
# Challenge: X (3x2) and w (2x1)
# -----------------------------
X = np.array([[1, 2],
              [3, 4],
              [5, 6]])

w = np.array([[2],
              [3]])

print("Matrix X:\n", X)
print("Vector w:\n", w)

result = X @ w

print("\nX @ w =\n", result)
