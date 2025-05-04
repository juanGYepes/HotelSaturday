from domain.models.OptionalServices import OptionalServices


class OptionalServicesRepository:
    def __init__(self):
        self.optionalservices = OptionalServices

    def create_optional_services_repository(self, optionalservices, db):
        if not all([
            optionalservices.codeServiceOp,
            optionalservices.nameServiceOp,
            optionalservices.description,
            optionalservices.price,
            optionalservices.status
        ]):
            print("⚠️ Todos los campos son obligatorios.")
            return

        query = "INSERT INTO optionalservices(codeServiceOp, nameServiceOp, description, price, status) VALUES (%s, %s, %s, %s, %s)"
        values = (
            optionalservices.codeServiceOp,
            optionalservices.nameServiceOp,
            optionalservices.description,
            optionalservices.price,
            optionalservices.status
        )
        db.execute_query(query, values)
