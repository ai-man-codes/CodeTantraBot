import customtkinter as ctk

import os

from PIL import Image

from src.Bots.DataStructures import bot as DS_bot
from src.Bots.PythonLearning import bot as PYL_bot
from src.Bots.PythonPractical import bot as PYP_bot

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

appWidth = 800
appHeight = 500

img_dir = os.path.dirname(os.path.abspath(__file__))

icon_path = os.path.join(img_dir, 'assets/favicon.ico')
header_path = os.path.join(img_dir, 'assets/logo-white-text.png')

DS_CONTENT = " Data Structures Content"
PY_LEARNING_CONTENT = " Python Learning Content"
PY_PRACTICAL_CONTENT = "    Python Lab Content"

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title('CodeTantraBot ~ Ai-man')
        
        try:
            self.iconbitmap(icon_path)

        except Exception as e:
            print("icon not found !")
            print(f"Error : {e}")

        self.geometry(f"{appWidth}x{appHeight}")
        self.resizable(False, False)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)  

        self.header_image = ctk.CTkImage(light_image=Image.open(header_path),
                                         dark_image=Image.open(header_path),
                                         size=(500, 80),
                                         )  
        self.header = ctk.CTkLabel(self, image=self.header_image, text="")
        self.header.grid()

        self.option_menu = ctk.CTkOptionMenu(self, values=[DS_CONTENT, PY_LEARNING_CONTENT, PY_PRACTICAL_CONTENT],
                                             width=280, height=32,
                                             font=("Lucida Console", 16),
                                             )
        self.option_menu.grid(pady=30, padx=20)

        self.username = ctk.CTkEntry(self, placeholder_text="\t\t     Email",
                                     width=350, height=40,
                                     font=("Arial", 14),
                                     )
        self.username.grid(padx=10, pady=10)

        self.password = ctk.CTkEntry(self, placeholder_text="\t\t  Password",
                                     width=350, height=40,
                                     font=("Arial", 14),
                                     )
        self.password.grid(padx=10, pady=10)

        self.startBtn = ctk.CTkButton(self, text="Start",
                                     width=80, height=35 ,
                                     font=("Lucida Console", 16),
                                     command=self.start,
                                     )
        self.startBtn.grid(padx=30, pady=30)
        
        self.warningLabel = ctk.CTkLabel(self, text="DO NOT TOUCH ANYTHING IN THE BROWSER !",
                                         height=25,
                                         text_color="white",
                                         )
        self.warningLabel.grid(pady= 10)

    def start(self):
        username = self.username.get()
        password = self.password.get()

        selected_option = self.option_menu.get()
        
        if selected_option == DS_CONTENT:
            DS_bot.main(username, password)
        
        if selected_option == PY_PRACTICAL_CONTENT:
            PYP_bot.main(username, password)

        if selected_option == PY_LEARNING_CONTENT:
            PYL_bot.main(username, password)

if __name__ == '__main__':
    app = App()
    app.mainloop()
    
