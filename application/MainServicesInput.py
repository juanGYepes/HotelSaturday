from domain.models.MainServices import MainServices
from repository.persistence.MainServicesRepository import MainServicesRepository

class MainServicesInput:
    def __init__(self):
        self.mainservices = MainServices(None, None, None, None, None)
        self.repo = MainServicesRepository()

    def register(self, db):
        code = input("Código servicio: ").strip()
        name = input("Nombre servicio: ").strip()
        desc = input("Descripción: ").strip()
        try:
            price = float(input("Precio: "))
        except ValueError:
            print("Error: Precio numérico.")
            return
        status = input("Estado: ").strip()

        if not all([code, name, desc, status]):
            print("Error: Todos los campos son obligatorios.")
            return

        self.mainservices.codeService = code
        self.mainservices.nameService = name
        self.mainservices.description = desc
        self.mainservices.price = price
        self.mainservices.status = status
        self.repo.create_main_services_repository(self.mainservices, db)