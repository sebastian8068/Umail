from mysql.connector.cursor import MySQLCursorDict
from mysql.connector.types import ResultType
from dataBase import connect, disconnect
from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection
from mysql.connector.errors import Error
from typing import Any, Dict, Tuple

class User:
    def __init__(self, name: str, number: str, email: str, password: str) -> None:
        self._name = name
        self._number = number
        self._email = email
        self._password = password

    @property
    def name(self) -> str:
        return self._name

    @property
    def number(self) -> str:
        return self._number

    @property
    def email(self) -> str:
        return self._email

    @property
    def password(self) -> str:
        return self._password

class UserManagment:
    @staticmethod
    def add_user(user: User) -> None:
        connected:  PooledMySQLConnection | MySQLConnectionAbstract = connect()

        try:
            with connected.cursor() as cursor:
                sql_add_user: str = "INSERT INTO `umail`.`User` (`name`, `password`, `phone_number`, `email`) VALUES (%s, %s, %s, %s)"
                values: Tuple[str, str, str, str] = (user.name, user.password, user.number, user.email)

                cursor.execute(sql_add_user, values)
                connected.commit()

                print(f'Usuario {user.name} agregado exitosamente')
                print(f'ID generado: {cursor.lastrowid}')
        except Error as e:
            if connected.is_connected():
                connected.rollback()

            print(f'Error al agregar el usuario: {e}')
        finally:
            disconnect(connected)

    @staticmethod
    def validateEmail(email: str) -> bool | None:
        connected: PooledMySQLConnection | MySQLConnectionAbstract = connect()

        try:
            cursor: MySQLCursorDict| Any = connected.cursor(dictionary= True)
            with cursor:
                cursor.execute("SELECT email FROM umail.User WHERE email = %s", (email, ))

                result: Dict[str, Any] | None = cursor.fetchone()


                return result is not None

        except Error as e:
            print(f"Error al validar el email '{email}': {e}")
            return None
        finally:
            disconnect(connected)

    @staticmethod
    def validateCredentials(email: str, password: str) -> bool | None:
        connected: PooledMySQLConnection | MySQLConnectionAbstract = connect()

        try:
            cursor: MySQLCursorDict | Any = connected.cursor(dictionary= True)

            with cursor:
                cursor.execute("SELECT email FROM umail.User WHERE email = %s AND password = %s", (email,password))
                result: Dict[str, Any] | None = cursor.fetchone()

                return result is not None
        except Error as e:
            print(f'Error al validar las credenciales {e}')
            return None
        finally:
            disconnect(connected)

    @staticmethod
    def getID(email: str) -> int | None:
        connected: PooledMySQLConnection | MySQLConnectionAbstract = connect()

        try:
            cursor: MySQLCursorDict | Any = connected.cursor()

            with cursor:
                cursor.execute("SELECT user_id FROM umail.User WHERE email = %s", (email, ))
                result: Any | None = cursor.fetchone()

                if result:
                    return int(result[0])
                else:
                    return None

        except Error as e:
            print(f'Error para obtener ID para email "{email}": {e}')
            return None
        finally:
            disconnect(connected)
    
# Tests
if __name__ == '__main__':
    p_usuario = User('Juan', '0123', 'juan@ucla.com', 'sadggrg')
    # UserManagment.add_user(p_usuario)
    print(UserManagment.validateEmail(p_usuario.email))
    print(UserManagment.validateEmail('aaa'))
    print(UserManagment.validateCredentials(p_usuario.email, p_usuario.password))
    print(UserManagment.getID(p_usuario.email))
