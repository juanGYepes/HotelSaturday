from domain.models.MainServices import MainServices
from repository.persistence.MainServicesRepository import MainServicesRepository
from application.MainServices_Service import MainService_Service

class MainServicesInput:
    def __init__(self):
        self. mainservices= MainServices(None,None,None,None,None)
        self.mainservicesrepository = MainServicesRepository
        self.mainservices_services = MainService_Service

    def register_main_services(self, mainservices ,db):
        codeService = input("ingrese el codigo del servicio ")
        self.mainservices.codeService
        nameService = input("Ingrese el nombre del servicio ")
        self.mainservices.nameService
        description = input("Ingrese descripcion del servicio ")
        self.mainservices.description
        price = int(input("digite el costo del servicio "))
        self.mainservices.price
        status = input("ingrese el estado del servicio")
        self.mainservices.status

        self.mainservicesrepository.create_main_services_repository(self.mainservices,db)

    def print_data_servicesI(self):
        self.mainservices_services.print_data_main_services()