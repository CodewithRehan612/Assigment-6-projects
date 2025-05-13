class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee  # Aggregation: reference to an independent Employee object

    def show_employee(self):
        print(f"Department: {self.department_name}, Employee: {self.employee.name}")

# Example usage:
if __name__ == "__main__":
    emp = Employee("Alice")
    dept = Department("HR", emp)
    dept.show_employee()
    # Employee object exists independently
    print(emp.name) 