employees = [("Ram", 40000),("Radha", 50000), ("Krishna", 30000)]
print(employees)
tax_rate = 0.10

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

final_salary_list.sort(key=lambda x: x["final_salary"], reverse=True)

print("EMPLOYEE SALARY REPORT")
print("=" * 100)
print(f"{'Name':<15} {'Base Salary':<20} {'Tax':<15} {'Bonus':<15} {'Final Salary':<20}")
print("-" * 100)

for e in final_salary_list:
    print(f"{e['name']:<15} {e['base_salary']:<20.2f} {e['tax']:<15.2f} {e['bonus']:<15.2f} {e['final_salary']:<20.2f}")

print("=" *100)
