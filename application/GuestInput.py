from domain.models.Guest import Guest
from repository.persistence.GuestRepository import GuestRepository
#metodo para exportar
from application.ExportUtils import exportar_a_csv
class GuestInput:
    def __init__(self):
        self.guest = Guest(None, None, None, None, None, None, None, None, None)
        self.guest_repository = GuestRepository()

    # Metodo para exportar, obtener datos en GuestRepository
    def exportar_Guest_csv(self):
        datos = GuestRepository.obtener_todas()
        columnas = ["id", "name", "last_name", "phone", "email", "password", "status", "origin", "occupation"]

        exportar_a_csv("Guest.csv", columnas, datos)

    def register(self, db):
        try:
            id_ = int(input("Documento (ID): "))
        except ValueError:
            print("Error: El documento debe ser un número.")
            return

        name = input("Nombre: ").strip()
        last_name = input("Apellido: ").strip()
        phone = input("Teléfono: ").strip()
        email = input("Email: ").strip()
        password = input("Contraseña: ").strip()
        status = input("Estado (activo/inactivo): ").strip()
        origin = input("Ciudad de origen: ").strip()
        occupation = input("Ocupación: ").strip()

        # Campos obligatorios
        if not all([name, last_name, phone, email, password, status, origin, occupation]):
            print("Error: Todos los campos son obligatorios.")
            return



        self.guest.id = id_
        self.guest.name = name
        self.guest.last_name = last_name
        self.guest.phone = phone
        self.guest.email = email
        self.guest.password = password
        self.guest.status = status
        self.guest.origin = origin
        self.guest.occupation = occupation

        self.guest_repository.create_guest_repository(self.guest,db)