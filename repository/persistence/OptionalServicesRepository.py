from domain.models.OptionalServices import OptionalServices

class OptionalServicesRepository:
    def __init__(self):
        self.optionalservices = OptionalServices

    def create_optional_services_repository(self,optionalservices,db):
        query="INSERT INTO mainservices(codeServiceOp, nameServiceOp,description,price,status) VALUES(%s,%s,%s,%s,%s)"
        values = (optionalservices.codeService,optionalservices.nameService,optionalservices.description,optionalservices.price,optionalservices.status)
        db.execute_query(query , values)
