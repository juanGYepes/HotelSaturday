from domain.models.Employee import Employee

class EmployeeService:
    def __init__(self, repository):
        self.repository = repository

    def add_employee(self, id, name, last_name, phone, email, password, status, rol):
        employee = Employee(id, name, last_name, phone, email, password, status, rol)
        self.repository.save(employee)

    def list_employees(self):
        return self.repository.get_all()
