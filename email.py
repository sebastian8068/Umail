from mysql.connector.cursor import MySQLCursorDict
from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection
from mysql.connector.errors import Error
from typing import Any, Dict, Tuple, List, Optional
from datetime import datetime
import os
import customtkinter as ctk
from tkinter import filedialog, messagebox

try:
    from Backend.dataBase import connect, disconnect
    from user import User 
except ModuleNotFoundError:
    from dataBase import connect, disconnect
    from user import UserManagment

class Email:
    def __init__(self, sender: str, receiver: str, subject: str = "", body: str = "", 
                 files: List[None] = None) -> None:
        
        self._sender = sender
        self._receiver = receiver
        self._subject = subject
        self._body = body
        # Inicializamos lista vacía si es None para evitar errores
        self._files = files if files is not None else []
        # Si no se pasa fecha, se asigna la actual
        self._date = datetime.now()

    @property
    def sender(self) -> str:
        return self._sender

    @property
    def receiver(self) -> str:
        return self._receiver

    @property
    def subject(self) -> str:
        return self._subject

    @property
    def body(self) -> str:
        return self._body
    
    @property
    def files(self) -> List[None]:
        return self._files
    
    @property
    def date(self) -> datetime:
        return self._date


class EmailManagement: 

    @staticmethod
    def sendEmail(email_obj: Email, id_sender: int, receiver_email: str) -> bool:
        """
        Realiza la transacción:
        1. Inserta en 'message' y obtiene el ID generado.
        2. Usa el 'sender_id' (int) y 'receiver_email' (str) recibidos por parámetro
           para insertar en la tabla 'recipient'.
        """
        connected = connect()

        try:
            with connected.cursor() as cursor:
                # PASO 1: Insertar el mensaje
                sql_message = "INSERT INTO `umail`.`message` (`subject`, `body`, `edited`, `date`)" \
                " VALUES (%s, %s, %s, %s)"
                val_message = (email_obj.subject, email_obj.body, 0, email_obj.date)

                cursor.execute(sql_message, val_message)

                # Obtenemos el ID del mensaje recién creado automáticamente
                message_id = cursor.lastrowid 

                # PASO 2: Insertar en RECIPIENT (Una sola vez)
                # Recibimos sender_id (int) y receiver_email (str) directamente por parámetro

                sql_recipient = """
                    INSERT INTO `umail`.`recipient` 
                    (`message_id_fk`, `user_id_fk`, `email_recipient`, `Readed`, `deleted`) 
                    VALUES (%s, %s, %s, %s, %s)
                """
                # Nota: sender_id es el emisor, receiver_email es el receptor
                val_recipient = (message_id, id_sender, receiver_email, 0, 0)
                cursor.execute(sql_recipient, val_recipient)

                # --- PASO 3: Insertar en la tabla ADJUNTED (Archivos) ---
                # Schema: adjunted_id, file(medium_blob), message_id
                
                if email_obj.files:
                    sql_adjunted = "INSERT INTO `umail`.`adjunted` (`file`, `message_id_fk`) " \
                    "VALUES (%s, %s)"
                    
                    for file_path in email_obj.files:
                        # Verificamos que el archivo exista antes de intentar leerlo
                        if os.path.exists(file_path):
                            with open(file_path, 'rb') as file_blob:
                                binary_data = file_blob.read()
                                cursor.execute(sql_adjunted, (binary_data, message_id))
                        else:
                            print(f"Advertencia: El archivo {file_path} no se encontró y no se adjuntó.")

                # Si todo salió bien, guardamos los cambios (Commit de la transacción)
                connected.commit()
                print(f'Email enviado exitosamente con ID: {message_id}')
                return True

        except Error as e:
            # Si algo falla en cualquiera de los pasos, revertimos TODO (Rollback)
            if connected.is_connected():
                connected.rollback()
            print(f'Error crítico al enviar el email: {e}')
            return False
            
        except Exception as ex:
            # Captura errores de archivos (FileNotFound, permisos, etc.)
            if connected.is_connected():
                connected.rollback()
            print(f'Error general (archivos o lógica): {ex}')
            return False

        finally:
            disconnect(connected)

    #Este método se encarga exclusivamente de hablar con la base de datos. 
    # Es puro, rápido y no sabe nada de ventanas o botones.
    @staticmethod
    def get_attachments(message_id: int) -> List[Dict[str, Any]]:
        """
        CAPA DE DATOS: Solo extrae los binarios.
        """
        connected = connect()
        try:
            cursor = connected.cursor(dictionary=True)
            # Nota: Usamos %s para MySQL
            sql = "SELECT adjunted_id, file FROM `umail`.`adjunted` WHERE message_id_fk = %s"
            cursor.execute(sql, (message_id,))
            return cursor.fetchall()
        except Error as e:
            print(f"Error al recuperar adjuntos: {e}")
            return []
        finally:
            disconnect(connected)

    #Esta función combina la interactividad del filedialog 
    #con la inteligencia de evitar archivos duplicados.    
    @staticmethod
    def smart_download(binary_data: bytes, default_name: str = "adjunto"):
        """
        CAPA DE INTERFAZ: Maneja la lógica de guardado inteligente.
        """
        # 1. Preguntamos al usuario dónde quiere guardar
        ruta_seleccionada = filedialog.asksaveasfilename(
            title="Seleccionar destino",
            initialfile=default_name,
            defaultextension=".*",
            filetypes=[("Todos los archivos", "*.*")]
        )

        if not ruta_seleccionada:
            return # El usuario canceló

        # 2. Lógica de "Evitar Duplicados" (Fusionado del Código 1)
        carpeta_destino = os.path.dirname(ruta_seleccionada)
        nombre_archivo = os.path.basename(ruta_seleccionada)
        nombre_base, extension = os.path.splitext(nombre_archivo)
        
        ruta_final = ruta_seleccionada
        contador = 1
        
        while os.path.exists(ruta_final):
            nuevo_nombre = f"{nombre_base}({contador}){extension}"
            ruta_final = os.path.join(carpeta_destino, nuevo_nombre)
            contador += 1

        # 3. Escritura física (Modo Binario 'wb')
        try:
            with open(ruta_final, 'wb') as f:
                f.write(binary_data)
            
            messagebox.showinfo("Éxito", f"Archivo guardado como:\n{os.path.basename(ruta_final)}")
            return ruta_final
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo escribir el archivo: {e}")
            return None

    @staticmethod
    def getInbox(email_user: str) -> List[Email]:
       connected = connect()
       inbox = []
       try:
           cursor = connected.cursor(dictionary=True)
           
           # Buscamos mensajes donde email_recipient somos nosotros
           # Y traemos el email del Emisor haciendo JOIN con la tabla User
           sql = """
               SELECT 
                   m.message_id, m.subject, m.body, m.date,
                   u.email AS sender_email
               FROM `umail`.`message` m
               INNER JOIN `umail`.`recipient` r ON m.message_id = r.message_id_fk
               INNER JOIN `umail`.`User` u ON r.user_id_fk = u.user_id
               WHERE r.email_recipient = %s AND r.deleted = 0
               ORDER BY m.date DESC
           """
           cursor.execute(sql, (email_user,))
           results = cursor.fetchall()

           for row in results:
               email_obj = Email(
                   id=row['message_id'],
                   sender=row['sender_email'], # <--- El emisor real desde el JOIN
                   receiver=email_user,
                   subject=row['subject'],
                   body=row['body'],
                   date=row['date']
               )
               inbox.append(email_obj)
           return inbox
       except Error as e:
           print(f"Error: {e}")
           return []
       finally:
           disconnect(connected)

'''# Pruebas
if __name__ == '__main__':
    # Ejemplo de prueba rápida (requiere DB/SMTP configurados)
    try:


        # 1. usuarios para la prueba
        destino_user = User('Juan', '0123', 'juan@ucla.com', 'sadggrg')
        remitente_user  = User('mauricio', '696969', 'cha@ucla.com', 'hitler')
        

        # 2. Ahora sí, enviar el email
        test_email = Email(
            sender=remitente_user.email,
            receiver=destino_user.email,
            subject='Prueba con usuarios reales loquito',
            body='Prueba de envío entre usuarios loquito.',
            files=[]
        )

        sent = EmailManagement.sendEmail(test_email) 
        print('Envío exitoso:', sent)

    except Exception as e:
        print('Error en prueba:', e)'''