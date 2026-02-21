numbers = []

# Take 8 integers as input
for i in range(8):
    n = int(input("Enter number: "))
    numbers.append(n)

# Initialize values
total = 0
maximum = numbers[0]
minimum = numbers[0]
even_count = 0
odd_count = 0

# Loop through list
for num in numbers:
    # Sum
    total += num

    # Max
    if num > maximum:
        maximum = num

    # Min
    if num < minimum:
        minimum = num

    # Even / Odd count
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Average
average = total / len(numbers)

# Output
print("Numbers:", numbers)
print("Sum:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Even count:", even_count)
print("Odd count:", odd_count)
