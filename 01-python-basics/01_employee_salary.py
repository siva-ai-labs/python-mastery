
# 01_employee_salary.py

employee_name = input("Employee name: ")
gross_salary = float(input("Monthly gross salary (SEK): "))
tax_percentage = float(input("Estimated tax percentage: "))

tax_amount = gross_salary * tax_percentage / 100
net_salary = gross_salary - tax_amount

print("\n--- Salary Summary ---")
print(f"Employee: {employee_name}")
print(f"Gross Salary: {gross_salary:,.2f} SEK")
print(f"Estimated Tax: {tax_amount:,.2f} SEK")
print(f"Net Salary: {net_salary:,.2f} SEK")
