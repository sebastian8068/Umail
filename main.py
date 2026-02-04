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

    def errorMessage(self, message: str) -> None:
        CTkMessagebox(title= 'Error', message= message, icon= 'cancel')

    def openLoginWindow(self):
        print('opening login window...')
        self.top_level_login = WindowLogin(master= self, 
                                           login_callback= self.onLoginSuccess,
                                           sing_in_callback= self.onSingInSuccess)

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
            self.top_level_login.destroy()

            self.openMainWindow()
        else:
            self.errorMessage('Credenciales incorrectas')

    def onSingInSuccess(self, name: str, number: str, email: str, password: str, confirm_password: str):
        valid, error = WindowLogin.validateSingInData(email, password, confirm_password, name, number)

        if not valid:
            if isinstance(error, str):
                self.errorMessage(error)

        elif UserManagment.validateEmail(email):
            self.errorMessage('El email ya está en uso')

        else:
            user = User(name, number, email, password)
            UserManagment.add_user(user)
            CTkMessagebox(title= 'Éxito', message= 'Cuenta creada exitosamente', icon= 'check')


def main() -> None:
    root_window = RootWindow()
    root_window.mainloop()

if __name__ == '__main__':
    main()
