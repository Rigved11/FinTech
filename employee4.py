employees = [
    ("RAM", 40000),
    ("KRISHNA", 55000),
    ("RADHA", 30000)
]
tax_rate = 0.10
result = []

for name, salary in employees:
    tax = salary * tax_rate
    bonus = 5000 if salary > 50000 else 2500
    final_salary = salary - tax + bonus
    result.append((name, salary, tax, bonus, final_salary))

result.sort(key=lambda x: x[4], reverse=True)

print("Name    Salary   Tax   Bonus   Final")
print("************************************")

for r in result:
    print(r[0], r[1], r[2], r[3], r[4])
