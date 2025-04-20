

class BedRoom:

    def __init__(self, roomId, number, roomType,status):
        self._roomId=roomId
        self._number=number
        self._roomType=roomType
        self._status=status

        @property
        def roomId(self):
            return self._roomId

        @roomId.setter
        def roomId(self, roomId):
            self._roomId = roomId

        @property
        def number(self):
            return self._number

        @number.setter
        def number(self,number):
            self._number=number

        @property
        def roomType(self):
            return self._roomType

        @roomType.setter
        def roomType(self,roomType):
            self._roomType=roomType

        @property
        def status(self):
            return self._status

        @status.setter
        def status(self,status):
            self._status=status


























