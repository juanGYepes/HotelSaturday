class EmployeeInput:
    @staticmethod
    def create_employee():
        try:
            id = int(input("ID: "))
            name = input("Nombre: ")
            last_name = input("Apellido: ")
            phone = input("Teléfono: ")
            email = input("Email: ")
            password = input("Contraseña: ")
            status = input("Estado (activo/inactivo): ")
            rol = input("Rol del empleado: ")
            return id, name, last_name, phone, email, password, status, rol
        except ValueError:
            print("Error: el ID debe ser un número.")
            return None
