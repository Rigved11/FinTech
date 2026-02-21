import numpy as np

# -------------------------
# 1D NumPy Array
# -------------------------
arr1 = np.array([10, 20, 30, 40])

print("1D Array:", arr1)
print("Shape:", arr1.shape)
print("Size:", arr1.size)
print("Dimensions:", arr1.ndim)

print("\n-------------------------")

# -------------------------
# 2D NumPy Array
# -------------------------
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])

print("2D Array:\n", arr2)
print("Shape:", arr2.shape)
print("Size:", arr2.size)
print("Dimensions:", arr2.ndim)

print("\n-------------------------")

# -------------------------
# Zeros Matrix (3x3)
# -------------------------
zeros_matrix = np.zeros((3, 3))
print("3x3 Zeros Matrix:\n", zeros_matrix)

print("\n-------------------------")

# -------------------------
# Ones Matrix (2x4)
# -------------------------
ones_matrix = np.ones((2, 4))
print("2x4 Ones Matrix:\n", ones_matrix)

print("\n-------------------------")

# -------------------------
# Arange 1 to 10
# -------------------------
range_array = np.arange(1, 11)
print("Array from 1 to 10:", range_array)

print("\n-------------------------")

# -------------------------
# Challenge: 3x3 Matrix using arange + reshape
# -------------------------
matrix_3x3 = np.arange(1, 10).reshape(3, 3)
print("3x3 Matrix (1 to 9):\n", matrix_3x3)

print("\n-------------------------")

# Properties of 3x3 matrix
print("Shape:", matrix_3x3.shape)
print("Size:", matrix_3x3.size)
print("Dimensions:", matrix_3x3.ndim)
