import mysql.connector

def connect() -> mysql.connector.connection_cext.CMySQLConnection | None:
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='umail',
            user='root',
            password='12345'
        )
        if connection.is_connected():
            print('Conexión exitosa')
            return connection
    except Exception as e:
        print(f"Error al conectar: {e}")
        return None

connected = connect()

def disconnect(connection: mysql.connector.connection_cext.CMySQLConnection):
    try:
        if connection and connection.is_connected():
            connection.close()
            print("Conexión cerrada exitosamente")
    except Exception as e:
        print(f"Error al cerrar la conexión: {e}")

def consultar_usuarios():
    try:
        cursor = connected.cursor(dictionary=True)
        cursor.execute("SELECT user_id, name, email FROM umail.User")

        resultados = cursor.fetchall()

        for fila in resultados:
            print(f"Nombre: {fila["name"]}, email: {fila["email"]}")

        cursor.close()
    except Exception as e:
        print(f"Error en consulta: {e}")

consultar_usuarios()
disconnect(connected)

