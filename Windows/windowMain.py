import customtkinter
from CTkTable import CTkTable
from CTkMessagebox import CTkMessagebox
from PIL import Image
import os
from typing import List, Optional, Union, Tuple
from Windows.windowRedact import WindowRedacter
from Windows.windowRead import WindowRead

values_segmented_search: list[str] = ['Email', 'Asunto', 'Fecha', 'Todo']

class WindowMain(customtkinter.CTkToplevel):
    def __init__(self, 
                 *args, 
                 inbox: List[List[str]] = [['Leído', 'Email', 'Asunto', 'Fecha']],
                 current_user_email: str,
                 fg_color: Optional[Union[str, Tuple[str, str]]] = None, 
                 **kwargs):
        super().__init__(*args, 
                         fg_color=fg_color, 
                         **kwargs)
        self.title('Correo')
        self.attributes('-fullscreen', True)
        self.grid_columnconfigure(1, weight= 1)
        self.grid_rowconfigure(3, weight=1)
        customtkinter.set_appearance_mode('light')
        self.toplevel_window = None
        self.inbox = inbox
        self.filtered_inbox = [row[:4] for row in inbox]
        self.current_user_email = current_user_email

        ucla_img_path_light: str = os.path.join(os.path.dirname(__file__), "ucla_logo_light.png")
        ucla_img_path_dark: str = os.path.join(os.path.dirname(__file__), "ucla_logo_light.png")
        ucla_img_data_light = Image.open(ucla_img_path_light)
        ucla_img_data_dark = Image.open(ucla_img_path_dark)


        self.img_ucla = customtkinter.CTkImage(dark_image= ucla_img_data_dark,
                                               light_image= ucla_img_data_light,
                                               size= (70, 70))
        self.img_label_ucla = customtkinter.CTkLabel(self, 
                                                     text='', 
                                                     image= self.img_ucla)
        self.img_label_ucla.grid(row= 0,
                                 column= 0,
                                 rowspan= 2,
                                 sticky= 'nsew')

        self.label_new_message = customtkinter.CTkLabel(self, 
                                                        corner_radius= 20, 
                                                        text='Recibiste xx correos nuevos desde tu última conexión', 
                                                        fg_color='#166088', 
                                                        text_color='white', 
                                                        height=30, 
                                                        anchor='w')
        self.label_new_message.grid(row=0, 
                                    column=1, 
                                    padx= 10, 
                                    pady= 10, 
                                    sticky= 'ew', 
                                    columnspan= 2)

        self.entry_search = customtkinter.CTkEntry(self, 
                                                   corner_radius= 32, 
                                                   placeholder_text='Buscar', 
                                                   fg_color= '#5c7c8a', 
                                                   width= 500, 
                                                   placeholder_text_color= 'white')
        self.entry_search.grid(row= 1, 
                               column= 2, 
                               padx= 10, 
                               pady= 10, 
                               sticky= 'e')

        self.seg_button_search = customtkinter.CTkSegmentedButton(self, 
                                                                  values= values_segmented_search, 
                                                                  command= self.get_seg_button_search)
        self.seg_button_search.grid(row= 1, 
                                    column= 1, 
                                    padx= 10, 
                                    pady= 10)
        
        self.scroll_table = customtkinter.CTkScrollableFrame(self, 
                                                             corner_radius=20)
        self.scroll_table.grid(row= 2, 
                               column= 1, 
                               padx= 10, 
                               pady= 0, 
                               sticky= 'nwse', 
                               rowspan= 2, 
                               columnspan= 2)
        self.scroll_table.grid_columnconfigure(0, weight=1)

        self.table_inbox = CTkTable(self.scroll_table, 
                               values=self.filtered_inbox, 
                               colors=["#9ecde1", "#dbe9ee"], 
                               header_color="#166088", 
                               hover_color="#c0dedf",
                               command= self.on_table_click)
        self.table_inbox.grid(row= 0, 
                         column= 0, 
                         padx= 0, 
                         pady= 0, 
                         sticky= 'we')

        self.button_redact = customtkinter.CTkButton(self, 
                                                     text='Redactar', 
                                                     corner_radius=32, 
                                                     command=self.open_window_redacter, 
                                                     fg_color= '#9ecde1', 
                                                     text_color='black', 
                                                     height= 70)
        self.button_redact.grid(row=2, 
                                column=0, 
                                padx= 5, 
                                pady= (40, 10), 
                                sticky= 'we')


        self.frame_buttons = customtkinter.CTkFrame(self, 
                                                    fg_color='#166088', 
                                                    corner_radius=35)
        self.frame_buttons.grid(row= 3, 
                                column= 0, 
                                padx= 5, 
                                pady= 10, 
                                sticky= 'ns')

        self.button_dark = customtkinter.CTkButton(self.frame_buttons, 
                                                    text='Oscuro', 
                                                    corner_radius=32, 
                                                    command=self.setDarkMode, 
                                                    fg_color= '#166088')
        self.button_dark.grid(row=0, 
                               column=0, 
                               padx=10, 
                               pady= (15, 0))

        self.button_light = customtkinter.CTkButton(self.frame_buttons, 
                                                    text='Claro', 
                                                    corner_radius=32, 
                                                    command=self.setLightMode, 
                                                    fg_color= '#166088')
        self.button_light.grid(row=1, 
                               column=0, 
                               padx=10, 
                               pady= 0)

        # self.button_2do_3= customtkinter.CTkButton(self.frame_buttons, 
        #                                            text='????', 
        #                                            corner_radius=32, 
        #                                            command=self.to_do, 
        #                                            fg_color= '#166088')
        # self.button_2do_3.grid(row=2, 
        #                        column=0, 
        #                        padx=10, 
        #                        pady= 0)
        #
        # self.button_2do_4 = customtkinter.CTkButton(self.frame_buttons, 
        #                                             text='????', 
        #                                             corner_radius=32, 
        #                                             command=self.to_do, 
        #                                             fg_color= '#166088')
        # self.button_2do_4.grid(row=3, 
        #                        column=0, 
        #                        padx=10, 
        #                        pady= 0)
        #
        # self.button_2do_5 = customtkinter.CTkButton(self.frame_buttons, 
        #                                             text='????', 
        #                                             corner_radius=32, 
        #                                             command=self.message_error, 
        #                                             fg_color= '#166088')
        # self.button_2do_5.grid(row=4, 
        #                        column=0, 
        #                        padx=10, 
        #                        pady= 0)
        #
        # self.button_2do_6 = customtkinter.CTkButton(self.frame_buttons, 
        #                                             text='????', 
        #                                             corner_radius=32, 
        #                                             command=self.change_new_message, 
        #                                             fg_color= '#166088')
        # self.button_2do_6.grid(row=5, 
        #                        column=0, 
        #                        padx=10, 
        #                        pady= (0, 15))


    def open_window_redacter(self):
        print('opening window_redacter...')
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = WindowRedacter(self, sender_email=self.current_user_email)
        else:
            self.toplevel_window.focus()

    def change_new_message(self):
        number_new_message: int = 0
        self.label_new_message.configure(
            text= f'Recibiste {number_new_message} correos nuevos desde tu última conexión')

    def to_do(self):
        print('to_do')

    def get_search(self):
        print(f"Searching {self.entry_search.get()}")
        self.entry_search.delete(0, 'end')

    def get_seg_button_search(self, segmented_button):
        match segmented_button:
            case 'Email':
                print(f"segment {segmented_button} selected")
            case 'Asunto':
                print(f"segment {segmented_button} selected")
            case 'Fecha':
                print(f"segment {segmented_button} selected")

    # def on_table_click(self, data):
    #     print('on_table_click llamado...')
    #     window_read = WindowRead()
    #     window_read.setSender('a', data['value'])
    #     print(data)

    def on_table_click(self, data):
        clicked_row = data['row']
    
    # Solo procesa si NO es el header (fila 0)
        if clicked_row > 0:
        # Obtiene TODOS los datos de la fila seleccionada
            full_row_data = self.inbox[clicked_row]
        
        # Extrae cada campo según su posición en la lista
            leido = full_row_data[0]       # 'Leído' (si lo necesitas)
            email = full_row_data[1]       # 'Email'
            asunto = full_row_data[2]      # 'Asunto'
            fecha = full_row_data[3]       # 'Fecha'
            cuerpo = full_row_data[4]      # 'Body'
            telefono = full_row_data[5]    # 'Teléfono'
            recipient_id = full_row_data[6] # 'Recipient ID'
            nombre = full_row_data[7]      # 'Nombre'
        
            print(f"Fila {clicked_row} clickeada: {asunto}")
        
        # Crea y configura la ventana de lectura
            window_read = WindowRead(self)  # Pasa self como master
            window_read.setSender(nombre, email)  # Nombre y Email
            window_read.setTitle(asunto)          # Asunto como título de ventana
            window_read.setBody(cuerpo)           # Cuerpo del mensaje
            window_read.setSenderTlf(telefono)    # Teléfono
        
        # Hace que la ventana sea modal (opcional)
            window_read.focus()
            window_read.grab_set()
        else:
            print("Click en header - ignorando")

    def setDarkMode(self):
        customtkinter.set_appearance_mode('dark')

    def setLightMode(self):
        customtkinter.set_appearance_mode('light')

