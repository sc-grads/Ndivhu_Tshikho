class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

employee_list = []

employee_list.append[Employee("John", 23, 50000)]

def get_all_employee_names():
    return [employee.name for employee in employee_list]

def get_employee_by_name(name):
    return [employee for employee in employee_list if employee.name == name]   

