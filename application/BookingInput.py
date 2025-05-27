from datetime import datetime
from domain.models.Booking import Booking
from domain.models.Guest import Guest
from domain.models.BedRoom import BedRoom
from domain.models.MainServices import MainServices
from domain.models.OptionalServices import OptionalServices
#Exportar
from repository.persistence.BookingRepository import BookingRepository
from application.ExportUtils import exportar_a_csv

class BookingInput:
    def __init__(self):
        self.booking = Booking(None, None, None, None, None, None, None)
        self.booking_repository = BookingRepository()

    # Metodo para exportar, obtener datos en GuestRepository
    def exportar_Booking_csv(self):
        datos = BookingRepository.obtener_todas()
        columnas = ["id_booking", "booking_date", "checkout_date", "guest_id", "bedroom_id", "main_service_id"," optional_service_id"]

        exportar_a_csv("Booking.csv", columnas, datos)


    def create_booking(self, db):
        try:
            id_booking = int(input("ID reserva: "))
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


        self.booking.id_booking = id_booking
        self.booking.booking_date = booking_date
        self.booking.checkout_date = checkout_date
        self.booking.guest = Guest(guest_id, None, None, None, None, None, None, None, None)
        self.booking.bedroom = BedRoom(room_id, None, None, None)
        self.booking.main_service = MainServices(main_id, None, None, None, None)
        self.booking.optional_service = OptionalServices(opt_id or None, None, None, None, None)


        self.booking_repository.create_booking_repository(self.booking,db)