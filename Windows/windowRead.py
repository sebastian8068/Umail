import customtkinter
from typing import Optional, Tuple, Union

class WindowRead(customtkinter.CTk):
    def __init__(self, *args, fg_color: Optional[Union[str, Tuple[str, str]]] = None, **kwargs):
        super().__init__(*args, fg_color=fg_color, **kwargs)
        self.geometry('850x500')
        self.configure(fg_color= ('#dbe9ee', '#4f6d7a'))
        self.title('Nuevo mensaje')
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.index_segmen_file: int = 0

        self.recipient_frame=customtkinter.CTkFrame(self,
                                                    border_width=2,
                                                    fg_color='transparent')
        
        self.recipient_frame.grid(row= 0, 
                                column= 0,
                                columnspan= 3,
                                sticky= 'ewns')

        self.output_sender = customtkinter.CTkLabel(self.recipient_frame,
                                                    text= ' ',
                                                    anchor='w',
                                                    font=("Roboto", 20, "bold"), 
                                                    fg_color= 'transparent')
        
        self.output_sender.grid(row= 0, 
                                column= 0,
                                padx=4,
                                pady=2,
                                sticky='w')

        self.output_sender_tlf = customtkinter.CTkLabel(self.recipient_frame, 
                                                      text= ' ',
                                                      anchor='w',
                                                      font=("Roboto", 12), 
                                                      fg_color= 'transparent')
        
        self.output_sender_tlf.grid(row= 1, 
                                  column= 0,
                                   padx= 4,
                                   pady= 2,
                                   sticky='w')

        self.texbox_body = customtkinter.CTkTextbox(self, 
                                                    fg_color= 'transparent', 
                                                    border_width= 2, 
                                                    wrap= 'word',)
        self.texbox_body.grid(row= 1, 
                              column= 0,
                              columnspan= 3,
                              sticky= 'ewns')
        
        self.texbox_body.configure(state="disabled")

        self.scroll_files = customtkinter.CTkScrollableFrame(self,
                                                             orientation= 'horizontal',
                                                             height=30)
        self.scroll_files.grid(row= 2,
                               column= 0,
                               columnspan= 3,
                               sticky= 'ewsn')

        self.segment_files = customtkinter.CTkSegmentedButton(self.scroll_files,
                                                             values= [])
                                                             
        self.segment_files.grid(row= 0,
                                column= 0)
    
    def setBody(self, body: str) -> None:
        self.texbox_body.insert("0.0",body)

    def setTitle(self, issue: str) -> None:
        self.title(issue)

    def setSender(self, name, email: str) -> None:
        self.output_sender.configure(text='De: '+name+' - '+email)

    def setSenderTlf(self, tlf: str) -> None:
        self.output_recipient.configure(text=tlf)
    
    def setFiles(self, file_name: str) -> None:
        self.segment_files.insert(self.index_segmen_file, file_name)
        self.index_segmen_file += 1

