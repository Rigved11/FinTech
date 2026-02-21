numbers = []

# Taking 5 integers as input
for i in range(5):
    n = int(input("Enter number: "))
    numbers.append(n)

# Assume first element is both largest and smallest
largest = numbers[0]
smallest = numbers[0]

# Find largest and smallest manually
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

# Calculate range
range_value = largest - smallest

print("Numbers:", numbers)
print("Largest:", largest)
print("Smallest:", smallest)
print("Range:", range_value)
