from domain.models.MainServices import ServicesIncluide
from repository.persistence.ServicesIncluideRepository import ServicesIncluideRepository
from application.ServicesIncluideAp import ServiceIcluideAp
class ServicesIncluideInput:
    def __init__(self):
        self.servicesincluide = ServicesIncluide(None,None,None,None,None)
        self.servicesincluideRepository = ServicesIncluideRepository

    def register_services_incluide(self, servicesincluide ,db):
        reception = input("ingrese la recepcion")
        self.servicesincluide.reception
        toilet = input("servicio de aseo")
        self.servicesincluide.toilet
        food = input("ingrese tipo de alimento")
        self.servicesincluide.food
        security = input("ingrese si hara uso de la seguridad")
        self.servicesincluide.security
        tecnology = input("uso de tecnologia")
        self.servicesincluide.tecnology

        self.servicesincluideRepository.create_service_include_repository(self.servicesincluide,db)

    def print_data_servicesI(self):
        self.