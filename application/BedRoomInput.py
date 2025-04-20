from domain.models.BedRoom import BedRoom
from repository.persistence.BedRoomRepository import BedRoomRepository
from application.BedRoomService import BedRoomService

class BedRoomInput:

    def __init__(self):
        self.bedroom = BedRoom(None,None,None,None)
        self.bedroom_repository = BedRoomRepository()

    def register_bedroom(self, bedroom, db ):
        roomId = int(input("Ingrese el ID de la habitacion: "))
        self.bedroom.roomId = roomId
        number = int(input("Ingrese el numero de la habitacion: "))
        self.bedroom.number= number
        roomType = input("Ingrese el tipo de la habitacion: ")
        self.bedroom.roomType= roomType
        status = input("Ingrese el estado de la habitacion: ")
        self.bedroom.status= status

        self.bedroom_repository.create_bed_room_repository(self.bedroom, db)

    def print_data(self):
        self.bedroom_service.print_data_bedroom_service()


































