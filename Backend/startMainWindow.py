from mysql.connector.cursor import MySQLCursorDict
from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection
from mysql.connector.errors import Error
from typing import Any, Dict, Tuple, List, Optional

try:
    from Backend.dataBase import connect, disconnect
except ModuleNotFoundError:
    from dataBase import connect, disconnect

class StartMainWindow:
    @staticmethod
    def getInBox(email: str) -> Optional[List[List[str]]]:
        """
        Obtiene los correos recibidos por un usuario
        
        Args:
            email: Email del destinatario
            
        Returns:
            Lista de listas con los datos de los correos recibidos:
            [[Readed, Email (remitente), Asunto, Fecha, Body, Phone_number, Recipient_id, Name], ...]
            None si hay error
        """
        connected: PooledMySQLConnection | MySQLConnectionAbstract = connect()
        
        try:
            cursor: MySQLCursorDict | Any = connected.cursor(dictionary=True)
            
            with cursor:
                # Consulta SQL con JOIN para unir Recipient, Message y User
                # Ahora incluyendo el campo name del remitente
                sql_query: str = """
                SELECT 
                    r.readed, 
                    u.email as sender_email,
                    m.subject,
                    m.date,
                    m.body,
                    u.phone_number,
                    r.recipient_id,
                    u.name
                FROM umail.Recipient r 
                INNER JOIN umail.Message m ON r.message_id_fk = m.message_id 
                INNER JOIN umail.User u ON r.user_id_fk = u.user_id
                WHERE r.email_recipient = %s AND r.deleted = 0 
                ORDER BY m.date DESC
                """
                
                cursor.execute(sql_query, (email,))
                results: List[Dict[str, Any]] = cursor.fetchall()
                
                # Convertir los resultados a una lista de listas
                # Ahora con 8 columnas incluyendo el nombre del remitente
                emails_list: List[List[str]] = [
                    ['Leído', 'Email', 'Asunto', 'Fecha', 'Body', 'Teléfono', 'Recipient ID', 'Nombre']
                ]
                
                for row in results:
                    # Determinar estado de "Leído" basado en el campo readed
                    read_status: str = "✓" if row.get('readed', 0) == 1 else ""
                    
                    # Convertir todos los valores a string para consistencia
                    email_data: List[str] = [
                        read_status,                      # Leído (checkmark si está leído)
                        str(row.get('sender_email', '')), # Email del remitente
                        str(row.get('subject', '')),      # Asunto
                        str(row.get('date', '')),         # Fecha
                        str(row.get('body', '')),         # Body del mensaje
                        str(row.get('phone_number', '')), # Teléfono del remitente
                        str(row.get('recipient_id', '')), # ID del recipient
                        str(row.get('name', ''))          # Nombre del remitente (nuevo)
                    ]
                    emails_list.append(email_data)
                
                return emails_list
                
        except Error as e:
            print(f'Error al obtener la bandeja de entrada para "{email}": {e}')
            return None
        finally:
            disconnect(connected)
