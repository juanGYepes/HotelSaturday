from domain.models.MainServices import ServicesIncluide

class ServiceIcluideAp:

    register_data = []

    def __init__(self):
        self.servicesincluide = ServicesIncluide(None,None,None,None,None)


    def create_services_icluide(self, servicesincluide):
        servicesincluide.reception = self.register_data[0]
        servicesincluide.toilet = self.register_data[1]
        servicesincluide.food = self.register_data[2]
        servicesincluide.security = self.register_data[3]
        servicesincluide.security = self.register_data[4]

    def print_data_incluide_service(self,):
        for data in self.register_data:
            print(data)
