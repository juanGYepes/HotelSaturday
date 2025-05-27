from domain.models.OptionalServices import OptionalServices
from repository.conexion.Conexion import Conexion

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
            print("⚠ Todos los campos son obligatorios.")
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

#Metodo de obtener los datos
    @staticmethod
    def obtener_todas():
        # Parámetros de conexión
        conexion = Conexion(
            host='localhost',
            port=3307,
            user='root',
            password='',
            database='hotel_saturday'
        ).connection()

        if not conexion:
            return []

        cursor = conexion.cursor()

        cursor.execute("""
                SELECT codeServiceOp, nameServiceOp, description, price, status
                FROM optionalservices
            """)
        resultados = cursor.fetchall()

        cursor.close()
        conexion.close()
        return resultados