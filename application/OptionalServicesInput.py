from domain.models.OptionalServices import OptionalServices
from repository.persistence.OptionalServicesRepository import OptionalServicesRepository
from application.OptionalServices_Service import OptionalService_Service

class OptionalServicesInput:
    def __init__(self):
        self.optionalservices=OptionalServices(None,None,None,None,None)
        self.optionalservicesrepository = OptionalServicesRepository
        self.optionalservices_services = OptionalService_Service

    def register_optional_services(self, optionalservices ,db):
        codeServiceOp = input("ingrese el codigo del servicio: ")
        self.optionalservices.codeServiceOp
        nameServiceOp = input("Ingrese el nombre del servicio: ")
        self.optionalservices.nameServiceOp
        description = input("Ingrese descripcion del servicio: ")
        self.optionalservices.description
        price = int(input("digite el costo del servicio: "))
        self.optionalservices.price
        status = input("ingrese el estado del servicio: ")
        self.optionalservices.status

        self.optionalservicesrepository.create_optional_services_repository(self.optionalservices,db)

    def print_data_servicesOp(self):
        self.optionalservices_services.print_data_optional_services()