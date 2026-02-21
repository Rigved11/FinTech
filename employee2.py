employees = [
    ("Rahul", 40000),
    ("Anita", 55000),
    ("John", 30000)
]

tax_rate= 0.10

def calculate_tax(salary):
    return salary * tax_rate if tax_rate > 0 else 0

def calculate_bonus(salary):
    return 5000 if salary > 50000 else 2500

final_salary_list = []

for name, salary in employees:
    tax = calculate_tax(salary)
    bonus = calculate_bonus(salary)
    final_salary = salary - tax + bonus

    final_salary_list.append({
        "name": name,
        "base_salary": salary,
        "tax": tax,
        "bonus": bonus,
        "final_salary": final_salary
    })

print("EMPLOYEE SALARY REPORT")
print("**********************")

for e in final_salary_list:
    print("Welcome")
    print("Name:", e["name"])
    print("Base Salary:", e["base_salary"])
    print("Tax:", e["tax"])
    print("Bonus:", e["bonus"])
    print("Final Salary:", e["final_salary"])
    print("Thank You")