import re
from domain.models.User import User

class Guest(User):
    def __init__(self, id, name, last_name, phone, email, password, status, origin, occupation):
        super().__init__(id, name, last_name, phone, email, password, status)
        self._origin = origin
        self._occupation = occupation

    @property
    def occupation(self):
        return self._occupation

    @occupation.setter
    def occupation(self, occupation):
        self._occupation = occupation

    @property
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self, origin):
        self._origin = origin

    def validate_email(self):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern, self.email):
            raise ValueError("Email inválido.")

    def validate_phone(self):
        if not re.match(r'^\+?[0-9]{7,15}$', self.phone):
            raise ValueError("Teléfono inválido.")