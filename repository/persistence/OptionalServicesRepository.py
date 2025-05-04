from domain.models.OptionalServices import OptionalServices

class OptionalServicesRepository:
    def __init__(self):
        self.optionalservices = OptionalServices

    def create_optional_services_repository(self, optionalservices, db):
        if not all([optionalservices.codeService, optionalservices.nameService,
                    optionalservices.description, optionalservices.price, optionalservices.status]):
            print("🚨 Todos los campos del servicio opcional son obligatorios.")
            return

        if not isinstance(optionalservices.price, (int, float)):
            print("🚨 El precio debe ser numérico.")
            return

        query = "INSERT INTO optionalservices(codeServiceOp, nameServiceOp, description, price, status) VALUES(%s, %s, %s, %s, %s)"
        values = (optionalservices.codeService, optionalservices.nameService,
                  optionalservices.description, optionalservices.price, optionalservices.status)
        db.execute_query(query, values)
