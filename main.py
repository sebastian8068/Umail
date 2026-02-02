from CTkMessagebox import CTkMessagebox
from Windows.windowMain import WindowMain
from Windows.windowLogin import WindowLogin
from Backend.user import User, UserManagment
import customtkinter
from typing import Optional, Union, Tuple

class RootWindow(customtkinter.CTk):
    def __init__(self, 
                 fg_color: Optional[Union[str, Tuple[str, str]]] = None, 
                 **kwargs):
         super().__init__(fg_color, **kwargs)
         self.withdraw()
         self.openLoginWindow()

    def openLoginWindow(self):
        print('opening login window...')
        self.top_level_login = WindowLogin(master= self, on_login_callback= self.onLoginSuccess)

    def openMainWindow(self):
        print('opening main window')
        self.top_level_main = WindowMain(self)

    def onLoginSuccess(self, email: str, password: str):
        if UserManagment.validateEmail(email) == False:
            CTkMessagebox(title= 'Error',
                          message= 'Usuario no encontrado',
                          icon= 'cancel')
            return

        if UserManagment.validateCredentials(email, password):
            print('login exitoso')
            # if hasattr(self, 'top_level_login'):
            self.top_level_login.destroy()

            self.openMainWindow()
        else:
          CTkMessagebox(title='Error',
                       message= 'Credenciales incorrectas',
                       icon= 'cancel')


def main() -> None:
    root_window = RootWindow()
    root_window.mainloop()

if __name__ == '__main__':
    main()
