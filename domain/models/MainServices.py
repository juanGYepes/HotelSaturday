class MainServices:
    def __init__(self, codeService, nameService, description, price, status):
        self._codeService = codeService
        self._nameService = nameService
        self._description = description
        self._price = price
        self._status = status

    @property
    def codeService(self):
        return self._codeService

    @codeService.setter
    def codeService(self, codeService):
        self._codeService = codeService

    @property
    def nameService(self):
        return self._nameService

    @nameService.setter
    def nameService(self, nameService):
        self._nameService = nameService

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

