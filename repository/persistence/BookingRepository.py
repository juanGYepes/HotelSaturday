from domain.models.Booking import Booking
from repository.conexion.Conexion import Conexion

class BookingRepository:

    def __init__(self):
        self.booking = Booking

    def create_booking_repository(self, booking, db):
        required_fields = [booking.id_booking, booking.booking_date, booking.checkout_date,
                           booking.guest.id, booking.bedroom._roomId, booking.main_service.codeService,
                           booking.optional_service.codeServiceOp]

        if not all(required_fields):
            print("🚨 Todos los campos de reserva son obligatorios.")
            return

        query = """
            INSERT INTO booking (
                id_booking, booking_date, checkout_date, guest_id, bedroom_id,
                main_service_id, optional_service_id
            ) VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            booking.id_booking,
            booking.booking_date,
            booking.checkout_date,
            booking.guest.id,
            booking.bedroom._roomId,
            booking.main_service.codeService,
            booking.optional_service.codeServiceOp,
        )

        db.execute_query(query, values)

    # Metodo de obtener los datos
    @staticmethod
    def obtener_todas():
        # Parámetros de conexión
        conexion = Conexion(
            host='localhost',
            port=3307,
            user='root',
            password='',
            database='hotel_saturday'
        ).connection()

        if not conexion:
            return []

        cursor = conexion.cursor()

        cursor.execute("""
                SELECT id_booking, booking_date, checkout_date, guest_id, bedroom_id, main_service_id, optional_service_id
                FROM booking
            """)
        resultados = cursor.fetchall()

        cursor.close()
        conexion.close()
        return resultados