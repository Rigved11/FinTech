import numpy as np

# Hours studied by students
hours = np.array([1, 2, 3, 4, 5, 6])

# Exam result (0 = Fail, 1 = Pass)
result = np.array([0, 0, 0, 1, 1, 1])

print("Hours studied:", hours)
print("Exam result:", result)

# Total students
total_students = len(hours)
print("Total students:", total_students)

# Students who passed
passed = np.sum(result)
print("Students passed:", passed)

# Pass percentage
pass_percentage = (passed / total_students) * 100
print("Pass Percentage:", pass_percentage,"%")

# Students who studied more than 3 hours
print("Students who studied >3 hours:", hours[hours > 3])