from domain.models.MainServices import MainServices
from repository.conexion.Conexion import Conexion
class MainServicesRepository:
    def __init__(self):
        self.mainservices = MainServices

    def create_main_services_repository(self, mainservices, db):
        if not all([mainservices.codeService, mainservices.nameService,
                    mainservices.description, mainservices.price, mainservices.status]):
            print("🚨 Todos los campos del servicio principal son obligatorios.")
            return

        if not isinstance(mainservices.price, (int, float)):
            print("🚨 El precio debe ser numérico.")
            return

        query = "INSERT INTO mainservices(codeService, nameService, description, price, status) VALUES(%s, %s, %s, %s, %s)"
        values = (mainservices.codeService, mainservices.nameService,
                  mainservices.description, mainservices.price, mainservices.status)
        db.execute_query(query, values)

    # Metodo de obtener los datos
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
                SELECT codeService, nameService, description, price, status	
                FROM mainservices
            """)
        resultados = cursor.fetchall()

        cursor.close()
        conexion.close()
        return resultados