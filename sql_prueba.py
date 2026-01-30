import mysql.connector
from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection
from typing import List, Dict, Any

from mysql.connector.types import RowItemType

def connect() -> MySQLConnectionAbstract | PooledMySQLConnection | None:
# Establece conexión a la base de datos
    try:
        connection: MySQLConnectionAbstract | PooledMySQLConnection = mysql.connector.connect(
            host='localhost',
            database='umail',
            user='root',
            password='12345'
        )
        if connection.is_connected():
            print('Conexión exitosa')
            return connection
        return None
    except Exception as e:
        print(f"Error al conectar: {e}")
        return None

connected: MySQLConnectionAbstract | PooledMySQLConnection | None = connect()

def disconnect(connection: MySQLConnectionAbstract | PooledMySQLConnection | None):
    try:
        if connection and connection.is_connected():
            connection.close()
            print("Conexión cerrada exitosamente")
    except Exception as e:
        print(f"Error al cerrar la conexión: {e}")

def consultar_usuarios():
    try:
        if connected is None:
            print('No hay conexión disponible')
            return

        cursor = connected.cursor(dictionary=True)
        cursor.execute("SELECT user_id, name, email FROM umail.User")

        resultados: List[Dict[str, RowItemType]] | Any= cursor.fetchall()

        for fila in resultados:
            print(f"Nombre: {fila['name']}, email: {fila['email']}")

        cursor.close()
    except Exception as e:
        print(f"Error en consulta: {e}")

consultar_usuarios()
disconnect(connected)
