from domain.models.MainServices import MainServices

class MainServicesRepository:
    def __init__(self):
        self.mainservices = MainServices

    def create_main_services_repository(self,mainservices,db):
        query="INSERT INTO mainservices(codeService, nameService,description,price,status) VALUES(%s,%s,%s,%s,%s)"
        values = (mainservices.codeService,mainservices.nameService,mainservices.description,mainservices.price,mainservices.status)
        db.execute_query(query , values)
