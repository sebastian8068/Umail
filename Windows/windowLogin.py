import customtkinter
from typing import Optional, Union, Tuple
from PIL import Image


class WindowLogin(customtkinter.CTk):
    def __init__(self, fg_color: Optional[Union[str, Tuple[str, str]]] = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.title('Inicio')
        self.geometry('800x600')
        self.resizable(False, False)
        customtkinter.set_appearance_mode('light')
        #customtkinter.set_appearance_mode('dark')
        self.side_img_data = Image.open('side_img.png') #tiene que se del mismo tamanio las dos img
        
        self.side_img = customtkinter.CTkImage(dark_image= self.side_img_data,
                                               light_image= self.side_img_data,
                                               size= (300, 600))
        self.label_side_img = customtkinter.CTkLabel(self, 
                                 text= '',
                                 image= self.side_img)
        self.label_side_img.grid(row= 0,
                     column= 0)
        

        self.frame_form = customtkinter.CTkFrame(self, width=500, height=600, fg_color="#ffffff")
        
        self.frame_form.grid_propagate(False)  # evitamos que el frame cambie de tamaño
        
        self.frame_form.grid(row=0, 
                     column=1, 
                     sticky="nsew")

        self.label_title = customtkinter.CTkLabel(self.frame_form,
                              text="Bienvenido!",
                              font=customtkinter.CTkFont(size=40, weight="bold"),
                              text_color="#000000",
                              anchor='n',
                              justify='left')
        
        self.label_title.grid(row=0, 
                      column=0, 
                      padx=20, 
                      pady=(40, 10), 
                      sticky="w")

        self.label_subtitle = customtkinter.CTkLabel(self.frame_form,
                                 text="Inicia sesión o Registrate",
                                 font=customtkinter.CTkFont(size=16),
                                 text_color="#000000",
                                 anchor='n',
                                 justify='left')

        self.label_subtitle.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")


        self.tabview = customtkinter.CTkTabview(self.frame_form,
                           #width=400,
                            #height=450,
                            fg_color="#dbe9ee",
                            corner_radius=20,
                            segmented_button_fg_color="#166088",
                            segmented_button_unselected_color="#166088",
                            segmented_button_unselected_hover_color="#85aec0",
                            segmented_button_selected_color="#1C78AA",
                            segmented_button_selected_hover_color="#9ecde1"
                            )
        
        self.tabview.grid(row=2, 
                 column=0, 
                 padx=50, 
                 pady=20,
                 sticky="ew")
        
        self.tab_iniciar = self.tabview.add("Iniciar Sesión")
        self.tab_registrarse = self.tabview.add("Registrarse")
        
      
        self.label_email = customtkinter.CTkLabel(
            master=self.tab_iniciar,
            text="Email",
            text_color="#000000",
            anchor="w",
            justify="left",
            font=("Arial", 16))
        
        self.label_email.grid(row=0, column=0, padx=(30, 0), sticky="we")

        self.entry_email = customtkinter.CTkEntry(
            master=self.tab_iniciar,
            width=255,
            fg_color="#5c7c8a",
            text_color="#FFFFFF",
            placeholder_text="usuario@dominio.com",
            corner_radius=20)

        self.entry_email.grid(row=1, column=0, padx=(25, 25), sticky="we")


        self.label_passw = customtkinter.CTkLabel(
            master=self.tab_iniciar,
            text="Contraseña",
            text_color="#000000",
            anchor="w",
            justify="left",
            font=("Arial", 16))
        
        self.label_passw.grid(row=2, column=0, padx=(30, 0), pady=(40, 0), sticky="w")

        self.entry_passw = customtkinter.CTkEntry(
            master=self.tab_iniciar,
            width=255,
            fg_color="#5c7c8a",
            text_color="#FFFFFF",
            placeholder_text="***********",
            corner_radius=20)

        self.entry_passw.grid(row=3, column=0, padx=(25, 25), pady=(0, 80), sticky="we")


        self.button_acced = customtkinter.CTkButton(master=self.tab_iniciar, 
                                                     text='Acceder',
                                                     font=("Arial", 28, "bold"), 
                                                     corner_radius=32,
                                                     fg_color= '#9ecde1', 
                                                     text_color='black', 
                                                     height= 40)
        self.button_acced.grid(row=6, 
                                column=0, 
                                padx= 100, 
                                pady= (60, 0),
                                sticky= 'we')

        # --- Controles para la pestaña "Registrarse" (tab_2) ---
        self.label_reg_email = customtkinter.CTkLabel(
            master=self.tab_registrarse,
            text="Email",
            text_color="#000000",
            anchor="w",
            justify="left",
            font=("Arial", 16))
        self.label_reg_email.grid(row=0, column=0, padx=(5, 0), sticky="w")

        self.entry_reg_email = customtkinter.CTkEntry(
            master=self.tab_registrarse,
            fg_color="#5c7c8a",
            text_color="#FFFFFF",
            placeholder_text="usuario@dominio.com",
            corner_radius=20)
        self.entry_reg_email.grid(row=1, column=0, 
                                  #padx=(25, 25), 
                                  pady=(0, 3), sticky="we")

        self.label_reg_passw = customtkinter.CTkLabel(
            master=self.tab_registrarse,
            text="Contraseña",
            text_color="#000000",
            anchor="w",
            justify="left",
            font=("Arial", 16))
        self.label_reg_passw.grid(row=2, column=0, 
                                  padx=(5, 0), 
                                  sticky="w")

        self.entry_reg_passw = customtkinter.CTkEntry(
            master=self.tab_registrarse,
            fg_color="#5c7c8a",
            text_color="#FFFFFF",
            placeholder_text="***********",
            corner_radius=20,
            show='*')
        self.entry_reg_passw.grid(row=3, column=0, 
                                  #padx=(25, 25), 
                                  pady=(0, 3), sticky="we")

        self.label_confirm_passw = customtkinter.CTkLabel(
            master=self.tab_registrarse,
            text="Confirmar contraseña",
            text_color="#000000",
            anchor="w",
            justify="left",
            font=("Arial", 16))
        
        self.label_confirm_passw.grid(row=4, column=0, padx=(5, 0), 
                                      sticky="w")

        self.entry_confirm_passw = customtkinter.CTkEntry(
            master=self.tab_registrarse,
            fg_color="#5c7c8a",
            text_color="#FFFFFF",
            placeholder_text="***********",
            corner_radius=20,
            show='*')
        self.entry_confirm_passw.grid(row=5, column=0, #padx=(25, 25), 
                                      pady=(0, 3), sticky="we")

        self.label_name = customtkinter.CTkLabel(
            master=self.tab_registrarse,
            text="Nombre",
            text_color="#000000",
            anchor="w",
            justify="left",
            font=("Arial", 16))
        self.label_name.grid(row=6, column=0, padx=(5, 0), 
                             sticky="w")

        self.entry_name = customtkinter.CTkEntry(
            master=self.tab_registrarse,
            fg_color="#5c7c8a",
            text_color="#FFFFFF",
            placeholder_text="Nombre completo",
            corner_radius=20)
        self.entry_name.grid(row=7, column=0, #padx=(25, 25), 
                             pady=(0, 3), sticky="we")

        self.label_phone = customtkinter.CTkLabel(
            master=self.tab_registrarse,
            text="Teléfono",
            text_color="#000000",
            anchor="w",
            justify="left",
            font=("Arial", 16))
        self.label_phone.grid(row=8, column=0, padx=(5, 0), 
                              sticky="we")

        self.entry_phone = customtkinter.CTkEntry(
            master=self.tab_registrarse,
            fg_color="#5c7c8a",
            text_color="#FFFFFF",
            placeholder_text="+51 xxxx xxx xxxx",
            corner_radius=20)
        self.entry_phone.grid(row=9, column=0, #padx=(25, 25), 
                              pady=(0, 10), sticky="we")

        self.button_create = customtkinter.CTkButton(master=self.tab_registrarse, 
                                                     text='Crear cuenta',
                                                     font=("Arial", 20, "bold"), 
                                                     corner_radius=32,
                                                     fg_color= '#9ecde1', 
                                                     text_color='black',
                                                     height= 30)
        self.button_create.grid(row=10, 
                                column=0, 
                                padx= 100, 
                                sticky= 'we')




    def closeLoginWindow(self):
        self.destroy()


if __name__ == '__main__':
    window_login = WindowLogin()
    window_login.mainloop()
