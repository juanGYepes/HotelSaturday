from domain.models.OptionalServices import OptionalServices

class OptionalService_Service:

    register_data = []

    def __init__(self):
        self.optionalservices = OptionalServices(None,None,None,None,None)


    def create_optional_services(self, optionalservices):
        optionalservices.codeServiceOp = self.register_data[0]
        optionalservices.nameServiceOp = self.register_data[1]
        optionalservices.description = self.register_data[2]
        optionalservices.price = self.register_data[3]
        optionalservices.status = self.register_data[4]

    def print_data_optional_services(self,):
        for data in self.register_data:
            print(data)