import numpy as np

data = np.array([10, 20, 30, 40, 50])

mean = np.mean(data)
std = np.std(data)

normalized = (data - mean) / std

print("Mean:", mean)
print("Standard Deviation:", std)
print("Normalized Data:", normalized)

import numpy as np

data = np.array([10, 20, 30, 40, 50])

mean = np.mean(data)
std = np.std(data)

normalized = (data - mean) / std

print("Mean:", mean)
print("Standard Deviation:", std)
print("Normalized Data:", normalized)

import numpy as np

# Generate 20 random integers between 1 and 100
data = np.random.randint(1, 101, 20)

print("Original Data:\n", data)

# Basic Statistics
mean = np.mean(data)
std = np.std(data)
min_val = np.min(data)
max_val = np.max(data)

print("\nMean:", mean)
print("Standard Deviation:", std)
print("Minimum:", min_val)
print("Maximum:", max_val)

# Normalization (Z-score)
normalized = (data - mean) / std

print("\nNormalized Data:\n", normalized)

print("\nMean of Normalized Data (should be ~0):", np.mean(normalized))


# Manual Standard Deviation

mean_manual = sum(data) / len(data)

variance = sum((x - mean_manual) ** 2 for x in data) / len(data)

std_manual = variance ** 0.5

print("\nManual Standard Deviation:", std_manual)
print("Numpy Standard Deviation:", std)