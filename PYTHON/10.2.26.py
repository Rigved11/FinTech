marks = [78, 85, 90, 66, 72]
print(sum(marks))
print(max(marks))
print(min(marks))
print(len(marks))

average = sum(marks) / len(marks)
print(f"Average: {average:.2f}")
diff = max(marks) - min(marks)
print(f"Difference: {diff}")
print(average >= 60)