from datetime import datetime
from domain.models.Booking import Booking
from domain.models.Guest import Guest
from domain.models.BedRoom import BedRoom
from domain.models.MainServices import MainServices
from domain.models.OptionalServices import OptionalServices
from repository.persistence.BookingRepository import BookingRepository

class BookingInput:
    def __init__(self):
        self.booking = Booking(None, None, None, None, None, None, None)
        self.booking_repository = BookingRepository()

    def create_booking(self, db):
        try:
            id_ = int(input("ID reserva: "))
        except ValueError:
            print("Error: El ID debe ser un número.")
            return

        def parse_date(prompt):
            s = input(prompt)
            try:
                return datetime.strptime(s, "%Y-%m-%d").date()
            except ValueError:
                print("Error: Fecha debe tener formato YYYY-MM-DD.")
                return None

        booking_date = parse_date("Fecha reserva (YYYY-MM-DD): ")
        if not booking_date:
            return
        checkout_date = parse_date("Fecha salida (YYYY-MM-DD): ")
        if not checkout_date:
            return

        # IDs referenciales
        try:
            guest_id = int(input("ID huésped: "))
            room_id = int(input("ID habitación: "))
            main_id = int(input("ID servicio principal: "))
            opt_id = int(input("ID servicio opcional (0 = ninguno): "))
        except ValueError:
            print("Error: Todos los IDs deben ser números.")
            return


        self.booking.id_booking = id_
        self.booking.booking_date = booking_date
        self.booking.checkout_date = checkout_date
        self.booking.guest = Guest(guest_id, None, None, None, None, None, None, None, None)
        self.booking.bedroom = BedRoom(room_id, None, None, None)
        self.booking.main_service = MainServices(main_id, None, None, None, None)
        self.booking.optional_service = OptionalServices(opt_id or None, None, None, None, None)


        self.booking_repository.create_booking_repository(self.booking, db)
