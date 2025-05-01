from msilib.schema import Property


class Booking:
    def __init__(self, id_booking, guest, bedroom, main_service, optional_service, employee, booking_date, checkout_date):
        self._id_booking = id_booking
        self._guest = guest
        self._bedroom = bedroom
        self._main_service = main_service
        self._optional_service = optional_service
        self._employee = employee
        self._booking_date = booking_date
        self._checkout_date = checkout_date

    @Property
    def id_booking(self):
        return self._id_booking

    @id_booking.setter
    def id_booking(self, id_booking):
        self._id_booking = id_booking

    @Property
    def booking_date(self):
        return self._booking_date

    @booking_date.setter
    def booking_date(self, booking_date):
        self._booking_date = booking_date

    @Property
    def checkout_date(self):
        return self._checkout_date

    @checkout_date.setter
    def checkout_date(self, checkout_date):
        self._checkout_date = checkout_date
