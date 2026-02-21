import numpy as np

# -----------------------------
# Starter Code (Element-wise operations)
# -----------------------------
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print("a + b =", a + b)
print("a * b =", a * b)
print("2 * a =", 2 * a)
print("a squared =", a ** 2)

print("\n-----------------------------")

# -----------------------------
# Basic NumPy Computations
# -----------------------------
arr = np.array([1, 2, 3, 4, 5])

print("Array:", arr)
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))

print("\n-----------------------------")

# -----------------------------
# Create array of 10 numbers
# -----------------------------
arr10 = np.arange(1, 11)
print("Original array:", arr10)

# Add 5 to every element
print("Add 5:", arr10 + 5)

# Multiply every element by 3
print("Multiply by 3:", arr10 * 3)

print("\n-----------------------------")

# -----------------------------
# Sum using Python loop
# -----------------------------
total_loop = 0
for num in arr10:
    total_loop += num

print("Sum using loop:", total_loop)

# -----------------------------
# Sum using NumPy
# -----------------------------
print("Sum using np.sum():", np.sum(arr10))

print("\n-----------------------------")

# -----------------------------
# Challenge: Manual Variance
# Formula: Var = sum((x - mean)^2) / n
# -----------------------------
mean_value = np.mean(arr10)

variance = np.sum((arr10 - mean_value) ** 2) / len(arr10)

print("Manual Variance:", variance)
