from domain.models.MainServices import MainServices
from repository.persistence.MainServicesRepository import MainServicesRepository
from application.ExportUtils import exportar_a_csv
class MainServicesInput:
    def __init__(self):
        self.mainservices = MainServices(None, None, None, None, None)
        self.repo = MainServicesRepository()

    # Metodo para exportar, obtener datos en GuestRepository
    def exportar_MainServices_csv(self):
        datos = MainServicesRepository.obtener_todas()
        columnas = ["codeService", "nameService", "description", "price", "status"]

        exportar_a_csv("MainServices.csv", columnas, datos)


    def register(self, db):
        code = input("Código servicio: ").strip()
        name = input("Nombre servicio: ").strip()
        desc = input("Descripción: ").strip()
        try:
            price = float(input("Precio: "))
        except ValueError:
            print("Error: Precio numérico.")
            return
        status = input("Estado (activo/inactivo): ").strip()

        if not all([code, name, desc, status]):
            print("Error: Todos los campos son obligatorios.")
            return

        self.mainservices.codeService = code
        self.mainservices.nameService = name
        self.mainservices.description = desc
        self.mainservices.price = price
        self.mainservices.status = status
        self.repo.create_main_services_repository(self.mainservices,db)