import csv


class Employee:
    employees = []

    def __init__(self, name=None, salary=0.0):
        self.name = name
        self.salary = salary

    @classmethod
    def load_from_csv(cls, file_path):
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                name, salary = row[0], float(row[1])
                cls.employees.append(Employee(name, salary))

    @classmethod
    def get_max_salary_employee(cls):
        if not cls.employees:
            return None
        return max(cls.employees, key=lambda emp: emp.salary)

    @classmethod
    def get_min_salary_employee(cls):
        if not cls.employees:
            return None
        return min(cls.employees, key=lambda emp: emp.salary)
