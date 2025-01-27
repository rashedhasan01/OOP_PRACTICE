"""
Read a CSV file and find the max and minimum salaries.
"""
from Employee import Employee

if __name__ == "__main__":
    csv_file_path = "salarysheet.csv"
    Employee.load_from_csv(csv_file_path)
    max_salary_employee = Employee.get_max_salary_employee()
    if max_salary_employee:
        print(f"Max Salary: {max_salary_employee.name}, {max_salary_employee.salary}")
    min_salary_employee = Employee.get_min_salary_employee()
    if min_salary_employee:
        print(f"Min Salary: {min_salary_employee.name}, {min_salary_employee.salary}")

