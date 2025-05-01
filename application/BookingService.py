from domain.models.Booking import Booking

class BookingService:

    register_data = []

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

    def create_booking(self, booking):
        booking.id = self.register_data[0]
        booking.booking_date = self.register_data[1]
        booking.checkout_date = self.register_data[2]
        booking.guest = self.register_data[3]
        booking.bedroom = self.register_data[4]
        booking.main_service = self.register_data[5]
        booking.optional_service = self.register_data[6]
        booking.employee = self.register_data[7]

    def print_data_service(self):
        for data in self.register_data:
            print(data)

