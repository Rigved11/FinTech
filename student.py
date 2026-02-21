students = [
    ("ram", 75),
    ("krishna", 90),
    ("kalki", 40),
    ("parshuram", 65)
]


def add_grace_marks(marks):
    return marks + 5


def grade_student(marks):
    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "Fail"

graded_students = list(map(
    lambda x: (x[0], add_grace_marks(x[1]), grade_student(add_grace_marks(x[1]))),
    students
))
graded_students.sort(key=lambda x: x[1], reverse=True)

print("Student Marks Report:")
for name, marks, grade in graded_students:
    print(f"{name}: Marks={marks}, Grade={grade}")