from domain.models.BedRoom import BedRoom

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
