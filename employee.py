def calculate_salary(basic_salary, bonus, tax_rate):
    """
    Calculate employee salary with tax and bonus.

    Args:
        basic_salary (float): Basic salary of the employee.
        bonus (float): Bonus amount.
        tax_rate (float): Tax rate as a percentage.

    Returns:
        float: Net salary after tax and bonus.
    """

    gross_salary = basic_salary + bonus

    tax = (gross_salary * tax_rate) / 100

    map= gross_salary - tax

    return map

def main():
    
    basic_salary = float(input("Enter basic salary: "))
    bonus = float(input("Enter bonus amount: "))
    tax_rate = float(input("Enter tax rate (%): "))

   
    map = calculate_salary(basic_salary, bonus, tax_rate)

    
    print(f"Net Salary: ₹{map:.2f}")

if __name__ == "__main__":
    main()