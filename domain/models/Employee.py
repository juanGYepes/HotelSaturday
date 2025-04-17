from domain.models.User import User


class Employee(User):

    def _init_(self, id, name, last_name, phone, email, password, status, rol):
        super().__init__(id, name, last_name, phone, email, password, status)

        self._rol = rol

    @property
    def rol(self):
        return self._rol

    @rol.setter
    def rol(self, rol):
        self._rol = rol

    #Metodo string
    def __str__(self):
        return f"rol{self._rol}"