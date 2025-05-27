from domain.models.OptionalServices import OptionalServices
from repository.persistence.OptionalServicesRepository import OptionalServicesRepository
from application.ExportUtils import exportar_a_csv

class OptionalServicesInput:
    def __init__(self):
        self.opt = OptionalServices(None, None, None, None, None)
        self.repo = OptionalServicesRepository()

    # Metodo para exportar, obtener datos en GuestRepository
    def exportar_OptionalServices_csv(self):
        datos = OptionalServicesRepository.obtener_todas()
        columnas = ["codeServiceOp", "nameServiceOp", "description", "price", "status"]

        exportar_a_csv("OptionalServices.csv", columnas, datos)

    def register(self, db):
        code = input("Código opcional: ").strip()
        name = input("Nombre opcional: ").strip()
        desc = input("Descripción: ").strip()
        try:
            price = float(input("Precio: "))
        except ValueError:
            print("Error: Precio numérico.")
            return
        status = input("Estado(activo/inactivo): ").strip()

        if not all([code, name, desc, status]):
            print("Error: Todos los campos son obligatorios.")
            return

        self.opt.codeServiceOp = code
        self.opt.nameServiceOp = name
        self.opt.description = desc
        self.opt.price = price
        self.opt.status = status
        self.repo.create_optional_services_repository(self.opt,db)