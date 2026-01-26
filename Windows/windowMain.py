import customtkinter
from CTkTable import *
from CTkMessagebox import *
import windowRedact
from PIL import Image

values_segmented_search: list[str] = ['Email', 'Asunto', 'Fecha']

inbox: list[list[str]]= [['h', 'o', 'l', 'a'],
                         ['h', 'o', 'l', 'a'],
                         ['h', 'o', 'l', 'a'],
                         ['h', 'o', 'l', 'a']]

class Main_windows(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Correo')
        self.attributes('-fullscreen', True)
        self.grid_columnconfigure(1, weight= 1)
        self.grid_rowconfigure(3, weight=1)
        customtkinter.set_appearance_mode('light')
        self.toplevel_window = None
        ucla_img_data_white = Image.open('ucla_logo_light.png')
        ucla_img_data_dark = Image.open('ucla_logo_light.png')


        self.img_ucla = customtkinter.CTkImage(dark_image= ucla_img_data_dark,
                                               light_image= ucla_img_data_white,
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

        table_inbox = CTkTable(self.scroll_table, 
                               values=inbox, 
                               colors=["#9ecde1", "#dbe9ee"], 
                               header_color="#166088", 
                               hover_color="#c0dedf")
        table_inbox.grid(row= 0, 
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

        self.button_2do_1 = customtkinter.CTkButton(self.frame_buttons, 
                                                    text='????', 
                                                    corner_radius=32, 
                                                    command=self.get_search, 
                                                    fg_color= '#166088')
        self.button_2do_1.grid(row=0, 
                               column=0, 
                               padx=10, 
                               pady= (15, 0))

        self.button_2do_2 = customtkinter.CTkButton(self.frame_buttons, 
                                                    text='????', 
                                                    corner_radius=32, 
                                                    command=self.to_do, 
                                                    fg_color= '#166088')
        self.button_2do_2.grid(row=1, 
                               column=0, 
                               padx=10, 
                               pady= 0)

        self.button_2do_3= customtkinter.CTkButton(self.frame_buttons, 
                                                   text='????', 
                                                   corner_radius=32, 
                                                   command=self.to_do, 
                                                   fg_color= '#166088')
        self.button_2do_3.grid(row=2, 
                               column=0, 
                               padx=10, 
                               pady= 0)

        self.button_2do_4 = customtkinter.CTkButton(self.frame_buttons, 
                                                    text='????', 
                                                    corner_radius=32, 
                                                    command=self.to_do, 
                                                    fg_color= '#166088')
        self.button_2do_4.grid(row=3, 
                               column=0, 
                               padx=10, 
                               pady= 0)

        self.button_2do_5 = customtkinter.CTkButton(self.frame_buttons, 
                                                    text='????', 
                                                    corner_radius=32, 
                                                    command=self.message_error, 
                                                    fg_color= '#166088')
        self.button_2do_5.grid(row=4, 
                               column=0, 
                               padx=10, 
                               pady= 0)

        self.button_2do_6 = customtkinter.CTkButton(self.frame_buttons, 
                                                    text='????', 
                                                    corner_radius=32, 
                                                    command=self.change_new_message, 
                                                    fg_color= '#166088')
        self.button_2do_6.grid(row=5, 
                               column=0, 
                               padx=10, 
                               pady= (0, 15))


    def open_window_redacter(self):
        print('opening window_redacter...')
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = windowRedact.WindowRedacter(self)
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

    def message_error(self) -> None:
        CTkMessagebox(title= 'Error', message= 'Mensaje de error', icon= 'cancel')

if __name__ == '__main__':
    main_windows = Main_windows()
    main_windows.mainloop()
