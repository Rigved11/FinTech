marks = []

# Take 6 student marks
for i in range(6):
    m = int(input("Enter mark: "))
    marks.append(m)

# Calculate total
total = 0
for mark in marks:
    total += mark

average = total / len(marks)

# Create new list for marks >= average
above_avg = []

for mark in marks:
    if mark >= average:
        above_avg.append(mark)

# Output
print("All Marks:", marks)
print("Class Average:", average)
print("Marks >= Average:", above_avg)
