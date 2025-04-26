from domain.models.MainServices import MainServices

class MainService_Service:

    register_data = []

    def __init__(self):
        self.mainservices = MainServices(None,None,None,None,None)


    def create_main_services(self, mainservices):
        mainservices.codeService = self.register_data[0]
        mainservices.nameService = self.register_data[1]
        mainservices.description = self.register_data[2]
        mainservices.price = self.register_data[3]
        mainservices.status = self.register_data[4]

    def print_data_main_services(self,):
        for data in self.register_data:
            print(data)
