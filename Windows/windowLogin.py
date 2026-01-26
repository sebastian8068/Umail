import customtkinter
from typing import Optional, Union, Tuple
from PIL import Image

class WindowLogin(customtkinter.CTk):
    def __init__(self, fg_color: Optional[Union[str, Tuple[str, str]]] = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.title('Inicio')
        self.geometry('600x480')
        self.resizable(False, False)
        self.side_img_data = Image.open('side_img.png')
        
        self.side_img = customtkinter.CTkImage(dark_image= self.side_img_data,
                                               light_image= self.side_img_data,
                                               size= (300, 480))
        self.side_img_label = customtkinter.CTkLabel(self, 
                                                     text= '',
                                                     image= self.side_img)
        self.side_img_label.grid(row= 0,
                                 column= 0)

    def closeLoginWindow(self):
        self.destroy()

if __name__ == '__main__':
    window_login = WindowLogin()
    window_login.mainloop()
