numbers = []

for i in range(5):
    n = int(input("Enter number: "))
    numbers.append(n)

print("Numbers:", numbers)

# Total
total = sum(numbers)
print("Total:", total)

# Average
average = total / len(numbers)
print("Average:", average)

# Count Positive Numbers
positive_count = 0
for num in numbers:
    if num > 0:
        positive_count += 1

print("Count of positive numbers:", positive_count)
