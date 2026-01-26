import customtkinter
from typing import Optional, Tuple, Union

class WindowRedacter(customtkinter.CTkToplevel):
    def __init__(self, *args, fg_color: Optional[Union[str, Tuple[str, str]]] = None, **kwargs):
        super().__init__(*args, fg_color=fg_color, **kwargs)
        self.geometry('850x500')
        self.configure(fg_color= ('#dbe9ee', '#4f6d7a'))
        self.title('Nuevo mensaje')
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.index_segmen_file: int = 0

        self.entry_recipient = customtkinter.CTkEntry(self, 
                                                      placeholder_text= 'Destinatarios', 
                                                      fg_color= 'transparent')
        self.entry_recipient.grid(row= 0, 
                                  column= 0)

        self.entry_issue = customtkinter.CTkEntry(self, 
                                                  placeholder_text= 'Asunto', 
                                                  fg_color= 'transparent')
        self.entry_issue.grid(row= 1, 
                              column= 0,
                              columnspan= 3,
                              sticky= 'ew')

        self.texbox_body = customtkinter.CTkTextbox(self, 
                                                    fg_color= 'transparent', 
                                                    border_width= 2, 
                                                    wrap= 'word')
        self.texbox_body.grid(row= 2, 
                              column= 0,
                              columnspan= 3,
                              sticky= 'ewns')

        self.scroll_files = customtkinter.CTkScrollableFrame(self,
                                                             orientation= 'horizontal',
                                                             height=30)
        self.scroll_files.grid(row= 3,
                               column= 0,
                               columnspan= 3,
                               sticky= 'ew')

        self.segment_files = customtkinter.CTkSegmentedButton(self.scroll_files,
                                                             values= [])
                                                             
        self.segment_files.grid(row= 0, column= 0)

        self.button_send = customtkinter.CTkButton(self, 
                                                   text='Enviar')
        self.button_send.grid(row= 4, 
                              column= 0)

        self.button_addfile = customtkinter.CTkButton(self, 
                                                      text= 'Adjuntar',
                                                      command= self.add_file)
        self.button_addfile.grid(row= 4, 
                                 column= 1)

        self.button_clear = customtkinter.CTkButton(self, 
                                                    text= 'Limpiar',
                                                    command= self.clear_body)
        self.button_clear.grid(row= 4,
                               column= 2)

    def add_file(self):
        file_name = customtkinter.filedialog.askopenfilename()

        self.segment_files.insert(self.index_segmen_file, file_name)

        self.index_segmen_file += 1

    def clear_body(self):
        self.texbox_body.delete(0.0, 'end')
