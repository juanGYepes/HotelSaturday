from optparse import Values

from domain.models.BedRoom import BedRoom

class BedRoomRepository:

    def __init__(self):
        self.bedroom = BedRoom

    def create_bed_room_repository(self, bedroom, db):
        query = "INSERT INTO bedroom(roomId, number, roomType,status) VALUES(%s,%s,%s,%s)"
        values = (bedroom.roomId,bedroom.number,bedroom.roomType,bedroom.status)
        db.execute_query(query , values )






















