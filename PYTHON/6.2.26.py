positive_count=0
negative_count=0
zero_count=0

for i in range(5):
    num=int(input("Enter numbers{i+1}:"))
    if num>0:
        positive_count+=1
    elif num <0:
        negative_count+=1
    else:
        zero_count +=1

print("results:")
print(f"positive count:{positive_count}")
print(f"negative count:{negative_count}")
print(f"zeros:{zero_count}")

#workout2

marks = []
for i in range(3):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)

# Calculate average
average = sum(marks) / len(marks)

# Print grade
print(f"Average: {average:.2f}")
if average >= 75:
    print("Distinction")
elif average >= 40:
    print("Pass")
else:
    print("Fail")