class MainServices:

    def __init__(self, codeService, nameService,description,price,status):
        self._codService = codeService
        self._nameService = nameService
        self._description = description
        self._price = price
        self._status = status

    @property
    def codeService(self):
        return self._codeService

    @codeService.setter
    def reception(self,codeService):
        self._codeService = codeService

    @property
    def nameService(self):
        return self._nameService

    @nameService.setter
    def toilet(self, nameService):
        self._nameService = nameService

    @property
    def description(self):
        return self._description

    @description.setter
    def food(self, description):
        self.description = description

    @property
    def price(self):
        return self._price
    @price.setter
    def security(self,price):
        self._price = price

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self,status):
        self._status = status

