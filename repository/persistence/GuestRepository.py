import re
from domain.models.Guest import Guest

class GuestRepository:

    def __init__(self):
        self.guest = Guest

    def create_guest_repository(self, guest, db):
        # Validaciones
        if not all([guest.id, guest.name, guest.last_name, guest.phone,
                    guest.email, guest.password, guest.status, guest.origin, guest.occupation]):
            print("🚨 Todos los campos del huésped son obligatorios.")
            return

        if not re.match(r"[^@]+@[^@]+\.[^@]+", guest.email):
            print("🚨 El correo no tiene un formato válido.")
            return

        if len(guest.password) < 6:
            print("🚨 La contraseña debe tener al menos 6 caracteres.")
            return

        query = """
            INSERT INTO guest (
                id, name, last_name, phone, email, password,
                status, origin, occupation
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            guest.id,
            guest.name,
            guest.last_name,
            guest.phone,
            guest.email,
            guest.password,
            guest.status,
            guest.origin,
            guest.occupation
        )
        db.execute_query(query, values)
