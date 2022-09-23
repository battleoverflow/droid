################################################
# File: view.py                                #
#                                              #
# Author(s): {                                 #
#   Hifumi1337 <https://github.com/Hifumi1337> #
# }                                            #
################################################

import tkinter, customtkinter, os, platform
from subprocess import getoutput

if platform.system() == 'Darwin':
    adb = "$HOME/Library/Android/sdk/platform-tools/adb"
elif platform.system() == 'Windows':
    adb = "%LOCALAPPDATA%\Android\sdk\platform-tools\\adb"
elif platform.system() == 'Linux':
    whoami = getoutput("whoami")
    adb = f"/home/{whoami}/Android/Sdk/platform-tools/adb"

class View(customtkinter.CTk):

        def __init__(self, version):
            super().__init__()

            self.title(f"Droid | v{version}")
            self.geometry("600x400")
            self.set_appearance_mode("Dark")

            self.grid_columnconfigure(1, weight=1)
            self.grid_rowconfigure(0, weight=1)

            # Sidebar
            self.frame_left = customtkinter.CTkFrame(master=self, width=180, corner_radius=0)
            self.frame_left.grid(row=0, column=0, sticky="nswe")

            self.frame_right = customtkinter.CTkFrame(master=self)
            self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

            self.frame_left.grid_rowconfigure(0, minsize=10)
            self.frame_left.grid_rowconfigure(5, weight=1)
            self.frame_left.grid_rowconfigure(8, minsize=20)
            self.frame_left.grid_rowconfigure(11, minsize=10)

            self.label_1 = customtkinter.CTkLabel(master=self.frame_left, text=f"Droid | v{version}", text_font=("Roboto Medium", -18)) 
            self.label_1.grid(row=1, column=0, pady=10, padx=10)

            self.button_1 = customtkinter.CTkButton(master=self.frame_left, text="Connect", command=self.btn_connect)
            self.button_1.grid(row=2, column=0, pady=10, padx=20)

            self.button_2 = customtkinter.CTkButton(master=self.frame_left, text="Disconnect", command=self.btn_disconnect)
            self.button_2.grid(row=3, column=0, pady=10, padx=20)

            self.button_3 = customtkinter.CTkButton(master=self.frame_left, text="Close Droid", command=self.btn_destroy)
            self.button_3.grid(row=10, column=0, pady=10, padx=20)

            # Main Content
            self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
            self.frame_right.rowconfigure(7, weight=10)
            self.frame_right.columnconfigure((0, 1), weight=1)
            self.frame_right.columnconfigure(2, weight=0)

            self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
            self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

            # self.frame_info.rowconfigure(0, weight=1)
            # self.frame_info.columnconfigure(0, weight=1)

            # connection_info = f"Welcome, {getoutput('whoami')}"

            # self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info, text=connection_info, corner_radius=6, fg_color=("white", "gray38"))
            # self.label_info_1.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

            self.mainloop()

        def btn_connect(self):
            os.system(f'{adb} connect 1270.0.0.1')
            print("Connected")
        
        def btn_disconnect(self):
            os.system(f'{adb} disconnect 1270.0.0.1')
            print("Disconnected")
        
        def btn_destroy(self):
            os.system(f'{adb} disconnect 1270.0.0.1')
            self.destroy()