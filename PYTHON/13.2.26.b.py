numbers = []

size = int(input("How many numbers? "))

# Input numbers
for i in range(size):
    n = int(input("Enter number: "))
    numbers.append(n)

# Calculate sum manually
total = 0
for num in numbers:
    total += num

average = total / len(numbers)

# Create new list with numbers greater than average
above_avg = []

for num in numbers:
    if num > average:
        above_avg.append(num)

print("Original List:", numbers)
print("Average:", average)
print("Numbers greater than average:", above_avg)
