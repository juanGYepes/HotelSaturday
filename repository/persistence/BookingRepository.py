from domain.models.Booking import Booking

class BookingRepository:

    def __init__(self):
        self.booking = Booking

    def create_booking_repository(self, booking, db):
        query = "INSERT INTO booking (id, booking_date, checkout_date, guest_id, bedroom_id, main_service_id, optional_service_id, employee_id)"
        values = (
            booking.id,
            booking.booking_date,
            booking.checkout_date,
            booking.guest.id,
            booking.bedroom.id,
            booking.main_service.id,
            booking.optional_service.id,
            booking.employee.id
        )

        db.execute_query(query, values)

