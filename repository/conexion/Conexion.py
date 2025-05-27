import mysql
from mysql import connector

class Conexion:

    def __init__(self, host, port, user, password , database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.conn = None  # aquí el cambio

    def connection(self):
        try:
            self.conn = mysql.connector.connect(  # ⚠ CAMBIO
                host = self.host,
                port = self.port,
                user = self.user,
                password = self.password,
                database = self.database
            )
            print("✅ Conexión Establecida")
            #CAMBIO
            return self.conn  # ✅ Retorna la conexión
        except mysql.connector.Error as err:
            print("❌ Error al conectar a la base de datos:", err)
            return None

    def disconnect(self):
        if self.conn:
            self.conn.close()
            print("🔌 Conexión Cerrada")

    def execute_query(self, query , params=None):
        if not self.conn:
            print("⚠ No hay conexión activa.")
            return None
        cursor = self.conn.cursor(buffered=True)
        try:
            cursor.execute(query, params)
            self.conn.commit()
            print("📥 Registro guardado exitosamente")
            if query.strip().lower().startswith("select"):
                return cursor.fetchall()
        except mysql.connector.Error as err:
            print("🚨 Error al ejecutar la consulta:", err)
        finally:
          cursor.close()
