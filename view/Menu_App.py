from application.GuestInput import GuestInput
from application.BedRoomInput import BedRoomInput
from application.BookingInput import BookingInput
from application.MainServicesInput import MainServicesInput
from application.OptionalServicesInput import OptionalServicesInput
from repository.conexion.Conexion import Conexion

class Menu_App:
    def __init__(self):
        self.db = Conexion('localhost', 3307, 'root', '', 'hotel_saturday')
        self.db.connection()
        self.guest_input = GuestInput()
        self.bedroom_input = BedRoomInput()
        self.booking_input = BookingInput()
        self.main_input = MainServicesInput()
        self.opt_input = OptionalServicesInput()

    def init_app(self):
        while True:
            try:
                print("\n--- Menú Principal ---")
                print("1. Registrar Huésped")
                print("2. Registrar Habitación")
                print("3. Registrar Servicio Principal")
                print("4. Registrar Servicio Opcional")
                print("5. Registrar Reserva")
                print("6. Exportar a CSV")
                print("0. Salir")
                opc = int(input("Seleccione: "))
            except ValueError:
                print("Error: ingrese un número válido.")
                continue

            if opc == 1:
                self.guest_input.register(self.db)
            elif opc == 2:
                self.bedroom_input.register_bedroom(self.db)
            elif opc == 3:
                self.main_input.register(self.db)
            elif opc == 4:
                self.opt_input.register(self.db)
            elif opc == 5:
                self.booking_input.create_booking(self.db)
            elif opc == 6:
                self.exportar_csv()
            elif opc == 0:
                print("¡Hasta luego!")
                self.db.disconnect()
                break
            else:
                print("Opción no válida.")



#  Submenú para exportar a CSV
    def exportar_csv(self):
        while True:
            print("\n--- Exportar a CSV ---")
            print("1. Exportar Huéspedes")
            print("2. Exportar Habitaciones")
            print("3. Exportar Reservas")
            print("4. Exportar Servicios Principales")
            print("5. Exportar Servicios Opcionales")
            print("0. Volver al menú principal")
            try:
                sub_opc = int(input("Seleccione una opción: "))
            except ValueError:
                print("Error: ingrese un número válido.")
                continue

            if sub_opc == 1:
                self.guest_input.exportar_Guest_csv()
            elif sub_opc == 2:
                self.bedroom_input.exportar_BedRoom_csv()
            elif sub_opc == 3:
                self.booking_input.exportar_Booking_csv()
            elif sub_opc == 4:
                self.main_input.exportar_MainServices_csv()
            elif sub_opc == 5:
                self.opt_input.exportar_OptionalServices_csv()
            elif sub_opc == 0:
                break
            else:
                print("Opción no válida.")