from domain.models.BedRoom import BedRoom
from repository.conexion.Conexion import Conexion

class BedRoomRepository:

    def __init__(self):
        self.bedroom = BedRoom

    def create_bed_room_repository(self, bedroom, db):
        if not all([bedroom.roomId, bedroom.number, bedroom.roomType, bedroom.status]):
            print("🚨 Todos los campos de habitación son obligatorios.")
            return

        if not isinstance(bedroom.number, int):
            print("🚨 El número de habitación debe ser un número entero.")
            return

        query = "INSERT INTO bedroom(roomId, number, roomType, status) VALUES(%s, %s, %s, %s)"
        values = (bedroom.roomId, bedroom.number, bedroom.roomType, bedroom.status)
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
            SELECT roomId, number, roomType, status
            FROM bedroom
        """)
        resultados = cursor.fetchall()

        cursor.close()
        conexion.close()
        return resultados