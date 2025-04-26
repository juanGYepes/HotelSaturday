class OptionalServices:

    def __init__(self, codeServiceOp, nameServiceOp,description,price,status):
        self._codeServiceOp = codeServiceOp
        self._nameServiceOp = nameServiceOp
        self._description = description
        self._price = price
        self._status = status

    @property
    def codeServiceOp(self):
        return self._codeServiceOp

    @codeServiceOp.setter
    def codeServiceOp(self,codeServiceOp):
        self._codeServiceOp = codeServiceOp

    @property
    def nameServiceOp(self):
        return self._nameServiceOp

    @nameServiceOp.setter
    def nameServiceOp(self, nameServiceOp):
        self._nameServiceOp = nameServiceOp

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