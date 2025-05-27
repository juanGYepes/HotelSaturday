from domain.models.BedRoom import BedRoom
from repository.persistence.BedRoomRepository import BedRoomRepository
from application.ExportUtils import exportar_a_csv

class BedRoomInput:
    def __init__(self):
        self.bedroom = BedRoom(None, None, None, None)
        self.bedroom_repository = BedRoomRepository()

    # Metodo para exportar, obtener datos en GuestRepository
    def exportar_BedRoom_csv(self):
        datos = BedRoomRepository.obtener_todas()
        columnas = ["roomId", "number"," roomType"," status"]

        exportar_a_csv("BedRoom.csv", columnas, datos)

    def register_bedroom(self, db):
        try:
            roomId = int(input("ID habitación: "))
            number = int(input("Número habitación: "))
        except ValueError:
            print("Error: El ID y el número deben ser enteros.")
            return

        roomType = input("Tipo de habitación: ").strip()
        status = input("Estado (disponible/ocupada): ").strip()

        if not roomType or not status:
            print("Error: Todos los campos son obligatorios.")
            return

        self.bedroom.roomId = roomId
        self.bedroom.number = number
        self.bedroom.roomType = roomType
        self.bedroom.status = status

        self.bedroom_repository.create_bed_room_repository(self.bedroom,db)