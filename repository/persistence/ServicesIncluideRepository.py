from domain.models.ServicesIncluide import ServiceIncluide

class ServicesIncluideRepository:
    def __init__(self):
        self.servicesincluide = ServiceIncluide

    def create_service_include_repository(self,servicesincluide,db):
        query="INSERT INTO servicesincluide(reception, toilet,food,security,tecnology) VALUES(%s,%s,%s,%s,%s)"
        values = (servicesincluide.reception,servicesincluide.toilet,servicesincluide.food,servicesincluide.security,servicesincluide.tecnology)
        db.execute_query(query , values)