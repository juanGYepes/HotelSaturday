class EmployeeRepository:
    def __init__(self):
        self.employees = []

    def save(self, employee):
        if not all([employee.id, employee.name, employee.role]):
            print("🚨 El empleado debe tener ID, nombre y rol.")
            return

        self.employees.append(employee)
        print("✅ Empleado guardado correctamente.")

    def get_all(self):
        return self.employees
