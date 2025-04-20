from domain.models.BedRoom import BedRoom

class BedRoomService:
    register_data = []

    def __init__(self):
        self.bedroom = BedRoom (None,None,None,None)

    def createBedRoom(self, bedroom):
        bedroom.roomId = self.register_data[0]
        bedroom.number= self.register_data[1]
        bedroom.roomType = self.register_data[2]
        bedroom.status = self.register_data[3]


    def print_data_service(self, ):
        for data in self.register_data:
            print(data)














































