employees = [("Parshuram", 50000),("Ram", 60000),("Krishna", 40000)]

tax_rate = 0.1

def calculate_tax(salary):
    return  salary * tax_rate

def calculate_bonus(salary):
    return salary * 0.05

final_salaries = list(map(lambda emp:{
    "name": emp[0],
    "base_salary": emp[1],
    "tax": calculate_tax(emp[1]),
    "bonus":calculate_bonus(emp[1]),
    "final_salary":emp[1]-calculate_tax(emp[1]) +calculate_bonus(emp[1])                      
     },employees))


print("Employee Salary Report:")
for name, salary in employees:
    print(f"{name}: ₹{salary:.2f}")

for e in final_salaries:
    print("Welcome")
    print("Name:", e["name"])
    print("Base Salary:", e["base_salary"])
    print("Tax:", e["tax"])
    print("Bonus:", e["bonus"])
    print("Final Salary:", e["final_salary"])
    print("Thank You Guys")