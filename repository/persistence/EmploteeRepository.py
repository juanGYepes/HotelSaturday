class EmployeeRepository:
    def __init__(self):
        self.employees = []

    def save(self, employee):
        self.employees.append(employee)
        print("Empleado guardado correctamente.")

    def get_all(self):
        return self.employees
