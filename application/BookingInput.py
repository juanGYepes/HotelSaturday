from domain.models.Booking import Booking
from repository.persistence.BookingRepository import BookingRepository
from domain.models.Guest import Guest
from domain.models.BedRoom import BedRoom
from domain.models.MainServices import MainServices
from domain.models.OptionalServices import OptionalServices
from domain.models.Employee import Employee

class BookingInput:

    def __init__(self):
        self.booking = Booking(
            None,  # id
            None,  # booking_date
            None,  # checkout_date
            None,  # guest
            None,  # bedroom
            None,  # main_service
            None,  # optional_service
            None   # employee
        )
        self.booking_repository = BookingRepository()

    def create_booking(self, db):
        id = int(input("Ingrese el ID de la reserva: "))
        self.booking.id = id

        booking_date = input("Ingrese la fecha de reserva (YYYY-MM-DD): ")
        self.booking.booking_date = booking_date

        checkout_date = input("Ingrese la fecha de salida (YYYY-MM-DD): ")
        self.booking.checkout_date = checkout_date

        # Aquí se podría buscar el invitado en la base de datos con su ID, pero simulamos la creación simple
        guest_id = int(input("Ingrese el ID del huésped: "))
        self.booking.guest = Guest(id=guest_id)

        bedroom_id = int(input("Ingrese el ID de la habitación: "))
        self.booking.bedroom = BedRoom(id=bedroom_id)

        main_service_id = int(input("Ingrese el ID del servicio principal: "))
        self.booking.main_service = MainServices(id=main_service_id)

        optional_service_id = int(input("Ingrese el ID del servicio opcional (0 si no aplica): "))
        self.booking.optional_service = OptionalServices(id=optional_service_id if optional_service_id != 0 else None)

        employee_id = int(input("Ingrese el ID del empleado que realizó la reserva: "))
        self.booking.employee = Employee(id=employee_id)

        self.booking_repository.create_booking_repository(self.booking, db)
