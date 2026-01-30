import mysql.connector
from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.errors import Error
from mysql.connector.pooling import PooledMySQLConnection

def connect() -> MySQLConnectionAbstract | PooledMySQLConnection:
    try:
        connection: MySQLConnectionAbstract | PooledMySQLConnection = mysql.connector.connect(
            host='localhost',
            database='umail',
            user='root',
            password='12345'
        )
        if not connection.is_connected():
            connection.close()
            raise Error('Conexión establecida pero no activa') from None

        print('Conexión exitosa')
        return connection
    except Error as e:
        raise Error(f'Error: {e}') from e

def disconnect(connection: MySQLConnectionAbstract | PooledMySQLConnection):
    try:
        if connection.is_connected():
            connection.close()
            print("Conexión cerrada exitosamente")
    except Error as e:
        print(f"Error al cerrar la conexión: {e}")
        # raise Error(f'Error: {e}')
