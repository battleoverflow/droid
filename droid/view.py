"""
    Owner: battleoverflow (https://github.com/battleoverflow)
    Project: Droid (https://github.com/battleoverflow/droid)
    License: MIT
"""

import tkinter, customtkinter, platform, time, json
from tkinter import PhotoImage, messagebox
from subprocess import getoutput
from os.path import getsize, exists

if platform.system() == 'Darwin':
    adb = "$HOME/Library/Android/sdk/platform-tools/adb"
elif platform.system() == 'Windows':
    adb = "%LOCALAPPDATA%\Android\sdk\platform-tools\\adb"
elif platform.system() == 'Linux':
    whoami = getoutput("whoami")
    adb = f"/home/{whoami}/Android/Sdk/platform-tools/adb"

if platform.system() == 'Darwin':
    import sys, os
    
    def import_resources(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

INFO_CODE = "[INFO]"

class View(customtkinter.CTk):

        def __init__(self, version):
            super().__init__()

            self.title(f"Droid | v{version}")
            self.geometry("1400x750")
            self.set_appearance_mode("Dark")

            self.grid_columnconfigure(1, weight=1)
            self.grid_rowconfigure(0, weight=1)

            # Logo isn't working with PyPI, removing for now
            # if platform.system() == 'Darwin':
            #     img = PhotoImage(file=f"{import_resources('assets/droid.png')}")
            #     self.iconphoto(True, img)

            # Sidebar
            self.frame_left = customtkinter.CTkFrame(master=self, width=200, corner_radius=0)
            self.frame_left.grid(row=0, column=0, sticky="nswe")

            self.frame_middle = customtkinter.CTkFrame(master=self)
            self.frame_middle.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

            self.frame_right = customtkinter.CTkFrame(master=self)
            self.frame_right.grid(row=0, column=2, sticky="nswe", padx=20, pady=20)

            self.header = customtkinter.CTkLabel(master=self.frame_left, text=f"Droid | v{version}", text_font=("Roboto Medium", -18)) 
            self.header.grid(row=1, column=0, pady=10, padx=10)

            self.connect_ip_addr = customtkinter.CTkButton(master=self.frame_left, text="Connect", command=self.btn_connect)
            self.connect_ip_addr.grid(row=2, column=0, pady=10, padx=20)

            self.disconnect_ip_addr = customtkinter.CTkButton(master=self.frame_left, text="Disconnect", command=self.btn_disconnect)
            self.disconnect_ip_addr.grid(row=3, column=0, pady=10, padx=20)

            self.reboot_android = customtkinter.CTkButton(master=self.frame_left, text="Reboot", command=self.btn_reboot)
            self.reboot_android.grid(row=4, column=0, pady=10, padx=20)

            self.screenshot_android = customtkinter.CTkButton(master=self.frame_left, text="Screenshot", command=self.btn_screenshot)
            self.screenshot_android.grid(row=5, column=0, pady=10, padx=20)

            self.download_android = customtkinter.CTkButton(master=self.frame_left, text="Download File", command=self.btn_download_file)
            self.download_android.grid(row=6, column=0, pady=10, padx=20)

            self.upload_android = customtkinter.CTkButton(master=self.frame_left, text="Upload File", command=self.btn_upload_file)
            self.upload_android.grid(row=7, column=0, pady=10, padx=20)

            self.file_modifier = customtkinter.CTkButton(master=self.frame_left, text="Modify", command=self.btn_modify_file)
            self.file_modifier.grid(row=8, column=0, pady=10, padx=20)

            self.upload_apk = customtkinter.CTkButton(master=self.frame_left, text="Upload APK", command=self.btn_upload_apk)
            self.upload_apk.grid(row=9, column=0, pady=10, padx=20)

            self.remove_apk = customtkinter.CTkButton(master=self.frame_left, text="Remove APK", command=self.btn_remove_apk)
            self.remove_apk.grid(row=10, column=0, pady=10, padx=20)

            self.set_bluetooth_status = customtkinter.CTkButton(master=self.frame_left, text="Bluetooth", command=self.btn_bluetooth)
            self.set_bluetooth_status.grid(row=11, column=0, pady=10, padx=20)

            self.set_wifi_status = customtkinter.CTkButton(master=self.frame_left, text="Wifi", command=self.btn_wifi)
            self.set_wifi_status.grid(row=12, column=0, pady=10, padx=20)

            self.close_app = customtkinter.CTkButton(master=self.frame_left, text="Close Droid", command=self.btn_destroy)
            self.close_app.grid(row=13, column=0, pady=10, padx=20)

            self.help_menu = customtkinter.CTkButton(master=self.frame_left, text="Help", command=self.btn_help)
            self.help_menu.grid(row=14, column=0, pady=10, padx=20)

            self.droid_logs = customtkinter.CTkLabel(master=self.frame_right, text=f"Droid Logs | v{version}")
            self.droid_logs.grid(row=0, column=1, columnspan=5, rowspan=1, pady=5, padx=5, sticky="nsew")
            
            self.mainloop()

        def btn_connect(self):

            # Buttons
            try:
                self.start_file_download.destroy()
            except AttributeError:
                pass

            try:
                self.start_file_upload.destroy()
            except AttributeError:
                pass

            try:
                self.start_apk_upload.destroy()
            except AttributeError:
                pass

            try:
                self.start_apk_remove.destroy()
            except AttributeError:
                pass

            try:
                self.start_disconnect.destroy()
            except AttributeError:
                pass

            try:
                self.start_reboot.destroy()
            except AttributeError:
                pass

            try:
                self.start_screenshot.destroy()
            except AttributeError:
                pass

            try:
                self.start_bluetooth.destroy()
            except AttributeError:
                pass

            try:
                self.stop_bluetooth.destroy()
            except AttributeError:
                pass

            try:
                self.start_wifi.destroy()
            except AttributeError:
                pass

            try:
                self.stop_wifi.destroy()
            except AttributeError:
                pass

            try:
                self.start_file_modification.destroy()
            except AttributeError:
                pass

            # Input Fields
            try:
                self.download_file.destroy()
            except AttributeError:
                pass

            try:
                self.upload_file.destroy()
            except AttributeError:
                pass

            try:
                self.filename.destroy()
            except AttributeError:
                pass

            try:
                self.name_of_apk.destroy()
            except AttributeError:
                pass

            try:
                self.apk_package_name.destroy()
            except AttributeError:
                pass

            try:
                self.ip_addr.destroy()
            except AttributeError:
                pass

            try:
                self.screenshot_file.destroy()
            except AttributeError:
                pass

            try:
                self.name_of_file.destroy()
            except AttributeError:
                pass

            try:
                self.new_content.destroy()
            except AttributeError:
                pass

            self.ip_addr = customtkinter.CTkEntry(master=self.frame_middle, width=400, placeholder_text="IP Address of the Android device")
            self.ip_addr.grid(row=6, column=1, pady=10, padx=20)

            self.json_file_name = customtkinter.CTkEntry(master=self.frame_middle, width=400, placeholder_text="Location of the JSON file on the local system (ex: ~/Documents/droid_ip_addr.json)")
            self.json_file_name.grid(row=7, column=1, pady=10, padx=20)

            self.ip_addr_json = customtkinter.CTkEntry(master=self.frame_middle, width=400, placeholder_text="Key assigned in JSON file (ex: localhost)")
            self.ip_addr_json.grid(row=8, column=1, pady=10, padx=20)

            def submit():
                if exists(self.json_file_name.get()) and getsize(self.json_file_name.get()) > 4:
                    try:
                        with open(self.json_file_name.get(), "r") as ip_file:
                            ip_addr = json.load(ip_file)
                    except FileNotFoundError:
                        pass

                    try:
                        connect_ip_addr = getoutput(f'{adb} connect {ip_addr[self.ip_addr_json.get()]}')
                    except KeyError:
                        connect_ip_addr = getoutput(f'{adb} connect {self.ip_addr.get()}')
                else:
                    connect_ip_addr = getoutput(f'{adb} connect {self.ip_addr.get()}')

                print(f"{INFO_CODE} {connect_ip_addr}")

                self.droid_logs_lvl_1 = customtkinter.CTkLabel(master=self.frame_right, text=f"{INFO_CODE} {connect_ip_addr}", corner_radius=6, fg_color=("white", "gray38"))
                self.droid_logs_lvl_1.grid(row=1, column=1, columnspan=5, rowspan=1, pady=5, padx=5, sticky="nsew")

            self.start_connect = customtkinter.CTkButton(master=self.frame_middle, text="Submit", command=submit)
            self.start_connect.grid(row=9, column=1, pady=10, padx=20)

        def btn_download_file(self):

            # Buttons
            try:
                self.start_connect.destroy()
            except AttributeError:
                pass

            try:
                self.start_file_upload.destroy()
            except AttributeError:
                pass

            try:
                self.start_apk_upload.destroy()
            except AttributeError:
                pass

            try:
                self.start_apk_remove.destroy()
            except AttributeError:
                pass

            try:
                self.start_disconnect.destroy()
            except AttributeError:
                pass

            try:
                self.start_reboot.destroy()
            except AttributeError:
                pass

            try:
                self.start_screenshot.destroy()
            except AttributeError:
                pass

            try:
                self.start_bluetooth.destroy()
            except AttributeError:
                pass

            try:
                self.stop_bluetooth.destroy()
            except AttributeError:
                pass

            try:
                self.start_wifi.destroy()
            except AttributeError:
                pass

            try:
                self.stop_wifi.destroy()
            except AttributeError:
                pass

            try:
                self.start_file_modification.destroy()
            except AttributeError:
                pass

            # Input Fields
            try:
                self.ip_addr.destroy()
            except AttributeError:
                pass

            try:
                self.json_file_name.destroy()
            except AttributeError:
                pass

            try:
                self.ip_addr_json.destroy()
            except AttributeError:
                pass

            try:
                self.upload_file.destroy()
            except AttributeError:
                pass

            try:
                self.filename.destroy()
            except AttributeError:
                pass

            try:
                self.name_of_apk.destroy()
            except AttributeError:
                pass

            try:
                self.apk_package_name.destroy()
            except AttributeError:
                pass

            try:
                self.ip_addr.destroy()
            except AttributeError:
                pass

            try:
                self.screenshot_file.destroy()
            except AttributeError:
                pass

            try:
                self.name_of_file.destroy()
            except AttributeError:
                pass

            try:
                self.new_content.destroy()
            except AttributeError:
                pass

            self.download_file = customtkinter.CTkEntry(master=self.frame_middle, width=400, placeholder_text="Location of File on the Android device")
            self.download_file.grid(row=6, column=1, pady=10, padx=20)

            def submit():
                download_android_file = getoutput(f'{adb} pull {self.download_file.get()}')
                print(f"{INFO_CODE} {download_android_file}")

                self.droid_logs_lvl_2 = customtkinter.CTkLabel(master=self.frame_right, text=f"{INFO_CODE} {download_android_file}", corner_radius=6, fg_color=("white", "gray38"))
                self.droid_logs_lvl_2.grid(row=2, column=1, columnspan=5, rowspan=1, pady=5, padx=5, sticky="nsew")

            self.start_file_download = customtkinter.CTkButton(master=self.frame_middle, text="Submit", command=submit)
            self.start_file_download.grid(row=7, column=1, pady=10, padx=20)

        def btn_upload_file(self):

            # Buttons
            try:
                self.start_connect.destroy()
            except AttributeError:
                pass

            try:
                self.start_file_download.destroy()
            except AttributeError:
                pass

            try:
                self.start_apk_upload.destroy()
            except AttributeError:
                pass

            try:
                self.start_apk_remove.destroy()
            except AttributeError:
                pass

            try:
                self.start_disconnect.destroy()
            except AttributeError:
                pass

            try:
                self.start_reboot.destroy()
            except AttributeError:
                pass

            try:
                self.start_screenshot.destroy()
            except AttributeError:
                pass

            try:
                self.start_bluetooth.destroy()
            except AttributeError:
                pass

            try:
                self.stop_bluetooth.destroy()
            except AttributeError:
                pass

            try:
                self.start_wifi.destroy()
            except AttributeError:
                pass

            try:
                self.stop_wifi.destroy()
            except AttributeError:
                pass

            try:
                self.start_file_modification.destroy()
            except AttributeError:
                pass

            # Input Fields
            try:
                self.ip_addr.destroy()
            except AttributeError:
                pass

            try:
                self.json_file_name.destroy()
            except AttributeError:
                pass

            try:
                self.ip_addr_json.destroy()
            except AttributeError:
                pass

            try:
                self.download_file.destroy()
            except AttributeError:
                pass

            try:
                self.name_of_apk.destroy()
            except AttributeError:
                pass

            try:
                self.apk_package_name.destroy()
            except AttributeError:
                pass

            try:
                self.ip_addr.destroy()
            except AttributeError:
                pass

            try:
                self.screenshot_file.destroy()
            except AttributeError:
                pass

            try:
                self.name_of_file.destroy()
            except AttributeError:
                pass

            try:
                self.new_content.destroy()
            except AttributeError:
                pass

            self.upload_file = customtkinter.CTkEntry(master=self.frame_middle, width=400, placeholder_text="Location to push the file on the Android device")
            self.upload_file.grid(row=6, column=1, pady=10, padx=20)

            self.filename = customtkinter.CTkEntry(master=self.frame_middle, width=400, placeholder_text="Name of the file on your local machine")
            self.filename.grid(row=7, column=1, pady=10, padx=20)

            def submit():
                upload_android_file = getoutput(f'{adb} push {self.filename.get()} {self.upload_file.get()}')
                print(f"{INFO_CODE} {upload_android_file}")

                self.droid_logs_lvl_3 = customtkinter.CTkLabel(master=self.frame_right, text=f"{INFO_CODE} {upload_android_file}", corner_radius=6, fg_color=("white", "gray38"))
                
                self.droid_logs_lvl_3.grid(row=3, column=1, columnspan=5, rowspan=1, pady=5, padx=5, sticky="nsew")

            self.start_file_upload = customtkinter.CTkButton(master=self.frame_middle, text="Submit", command=submit)
            self.start_file_upload.grid(row=8, column=1, pady=10, padx=20)

        def btn_upload_apk(self):

            # Buttons
            try:
                self.start_connect.destroy()
            except AttributeError:
                pass

            try:
                self.start_file_download.destroy()
            except AttributeError:
                pass

            try:
                self.start_file_upload.destroy()
            except AttributeError:
                pass

            try:
                self.start_apk_remove.destroy()
            except AttributeError:
                pass

            try:
                self.start_disconnect.destroy()
            except AttributeError:
                pass

            try:
                self.start_reboot.destroy()
            except AttributeError:
                pass

            try:
                self.start_screenshot.destroy()
            except AttributeError:
                pass

            try:
                self.start_bluetooth.destroy()
            except AttributeError:
                pass

            try:
                self.stop_bluetooth.destroy()
            except AttributeError:
                pass

            try:
                self.start_wifi.destroy()
            except AttributeError:
                pass

            try:
                self.stop_wifi.destroy()
            except AttributeError:
                pass

            try:
                self.start_file_modification.destroy()
            except AttributeError:
                pass

            # Input Fields
            try:
                self.ip_addr.destroy()
            except AttributeError:
                pass

            try:
                self.json_file_name.destroy()
            except AttributeError:
                pass

            try:
                self.ip_addr_json.destroy()
            except AttributeError:
                pass

            try:
                self.download_file.destroy()
            except AttributeError:
                pass

            try:
                self.upload_file.destroy()
            except AttributeError:
                pass

            try:
                self.filename.destroy()
            except AttributeError:
                pass

            try:
                self.apk_package_name.destroy()
            except AttributeError:
                pass

            try:
                self.ip_addr.destroy()
            except AttributeError:
                pass

            try:
                self.screenshot_file.destroy()
            except AttributeError:
                pass

            try:
                self.name_of_file.destroy()
            except AttributeError:
                pass

            try:
                self.new_content.destroy()
            except AttributeError:
                pass

            self.name_of_apk = customtkinter.CTkEntry(master=self.frame_middle, width=400, placeholder_text="Absolute path of the APK")
            self.name_of_apk.grid(row=6, column=1, pady=10, padx=20)

            def submit():
                upload_android_apk = getoutput(f'{adb} install -r {self.name_of_apk.get()}')
                print(f"{INFO_CODE} {upload_android_apk}")

                self.droid_logs_lvl_4 = customtkinter.CTkLabel(master=self.frame_right, text=f"{INFO_CODE} {upload_android_apk}", corner_radius=6, fg_color=("white", "gray38"))
                
                self.droid_logs_lvl_4.grid(row=4, column=1, columnspan=5, rowspan=1, pady=5, padx=5, sticky="nsew")
            
            self.start_apk_upload = customtkinter.CTkButton(master=self.frame_middle, text="Submit", command=submit)
            self.start_apk_upload.grid(row=7, column=1, pady=10, padx=20)

        def btn_remove_apk(self):

            # Buttons
            try:
                self.start_connect.destroy()
            except AttributeError:
                pass

            try:
                self.start_file_download.destroy()
            except AttributeError:
                pass

            try:
                self.start_file_upload.destroy()
            except AttributeError:
                pass

            try:
                self.start_apk_upload.destroy()
            except AttributeError:
                pass

            try:
                self.start_disconnect.destroy()
            except AttributeError:
                pass

            try:
                self.start_reboot.destroy()
            except AttributeError:
                pass

            try:
                self.start_screenshot.destroy()
            except AttributeError:
                pass

            try:
                self.start_bluetooth.destroy()
            except AttributeError:
                pass

            try:
                self.stop_bluetooth.destroy()
            except AttributeError:
                pass

            try:
                self.start_wifi.destroy()
            except AttributeError:
                pass

            try:
                self.stop_wifi.destroy()
            except AttributeError:
                pass

            try:
                self.start_file_modification.destroy()
            except AttributeError:
                pass

            # Input Fields
            try:
                self.ip_addr.destroy()
            except AttributeError:
                pass

            try:
                self.json_file_name.destroy()
            except AttributeError:
                pass

            try:
                self.ip_addr_json.destroy()
            except AttributeError:
                pass

            try:
                self.download_file.destroy()
            except AttributeError:
                pass

            try:
                self.upload_file.destroy()
            except AttributeError:
                pass

            try:
                self.filename.destroy()
            except AttributeError:
                pass

            try:
                self.name_of_apk.destroy()
            except AttributeError:
                pass

            try:
                self.ip_addr.destroy()
            except AttributeError:
                pass

            try:
                self.screenshot_file.destroy()
            except AttributeError:
                pass

            try:
                self.name_of_file.destroy()
            except AttributeError:
                pass

            try:
                self.new_content.destroy()
            except AttributeError:
                pass

            self.apk_package_name = customtkinter.CTkEntry(master=self.frame_middle, width=400, placeholder_text="Package Name for APK")
            self.apk_package_name.grid(row=6, column=1, pady=10, padx=20)

            def submit():
                remove_android_apk = getoutput(f'{adb} uninstall {self.apk_package_name.get()}')
                print(f"{INFO_CODE} {remove_android_apk}")

                self.droid_logs_lvl_5 = customtkinter.CTkLabel(master=self.frame_right, text=f"{INFO_CODE} {remove_android_apk}", corner_radius=6, fg_color=("white", "gray38"))
                self.droid_logs_lvl_5.grid(row=5, column=1, columnspan=5, rowspan=1, pady=5, padx=5, sticky="nsew")

            self.start_apk_remove = customtkinter.CTkButton(master=self.frame_middle, text="Submit", command=submit)
            self.start_apk_remove.grid(row=7, column=1, pady=10, padx=20)
        
        def btn_disconnect(self):

            # Buttons
            try:
                self.start_connect.destroy()
            except AttributeError:
                pass

            try:
                self.start_file_download.destroy()
            except AttributeError:
                pass

            try:
                self.start_file_upload.destroy()
            except AttributeError:
                pass

            try:
                self.start_apk_upload.destroy()
            except AttributeError:
                pass

            try:
                self.start_apk_remove.destroy()
            except AttributeError:
                pass

            try:
                self.start_reboot.destroy()
            except AttributeError:
                pass

            try:
                self.start_screenshot.destroy()
            except AttributeError:
                pass

            try:
                self.start_bluetooth.destroy()
            except AttributeError:
                pass

            try:
                self.stop_bluetooth.destroy()
            except AttributeError:
                pass

            try:
                self.start_wifi.destroy()
            except AttributeError:
                pass

            try:
                self.stop_wifi.destroy()
            except AttributeError:
                pass

            try:
                self.start_file_modification.destroy()
            except AttributeError:
                pass

            # Input Fields
            try:
                self.ip_addr.destroy()
            except AttributeError:
                pass

            try:
                self.json_file_name.destroy()
            except AttributeError:
                pass

            try:
                self.ip_addr_json.destroy()
            except AttributeError:
                pass

            try:
                self.download_file.destroy()
            except AttributeError:
                pass

            try:
                self.upload_file.destroy()
            except AttributeError:
                pass

            try:
                self.filename.destroy()
            except AttributeError:
                pass

            try:
                self.name_of_apk.destroy()
            except AttributeError:
                pass

            try:
                self.apk_package_name.destroy()
            except AttributeError:
                pass

            try:
                self.screenshot_file.destroy()
            except AttributeError:
                pass

            try:
                self.name_of_file.destroy()
            except AttributeError:
                pass

            try:
                self.new_content.destroy()
            except AttributeError:
                pass

            self.ip_addr = customtkinter.CTkEntry(master=self.frame_middle, width=400, placeholder_text="IP Address of the Android device (leave blank to disconnect everything)")
            self.ip_addr.grid(row=6, column=1, pady=10, padx=20)

            def submit():
                disconnect_ip_addr = getoutput(f'{adb} disconnect {self.ip_addr.get()}')
                print(f"{INFO_CODE} {disconnect_ip_addr}")

                self.droid_logs_lvl_6 = customtkinter.CTkLabel(master=self.frame_right, text=f"{INFO_CODE} {disconnect_ip_addr}", corner_radius=6, fg_color=("white", "gray38"))
                self.droid_logs_lvl_6.grid(row=6, column=1, columnspan=5, rowspan=1, pady=5, padx=5, sticky="nsew")

            self.start_disconnect = customtkinter.CTkButton(master=self.frame_middle, text="Submit", command=submit)
            self.start_disconnect.grid(row=7, column=1, pady=10, padx=20)

        def btn_reboot(self):

            # Buttons
            try:
                self.start_connect.destroy()
            except AttributeError:
                pass

            try:
                self.start_file_download.destroy()
            except AttributeError:
                pass

            try:
                self.start_file_upload.destroy()
            except AttributeError:
                pass

            try:
                self.start_apk_upload.destroy()
            except AttributeError:
                pass

            try:
                self.start_apk_remove.destroy()
            except AttributeError:
                pass

            try:
                self.start_disconnect.destroy()
            except AttributeError:
                pass

            try:
                self.start_screenshot.destroy()
            except AttributeError:
                pass

            try:
                self.start_bluetooth.destroy()
            except AttributeError:
                pass

            try:
                self.stop_bluetooth.destroy()
            except AttributeError:
                pass

            try:
                self.start_wifi.destroy()
            except AttributeError:
                pass

            try:
                self.stop_wifi.destroy()
            except AttributeError:
                pass

            try:
                self.start_file_modification.destroy()
            except AttributeError:
                pass

            # Input Fields
            try:
                self.ip_addr.destroy()
            except AttributeError:
                pass

            try:
                self.json_file_name.destroy()
            except AttributeError:
                pass

            try:
                self.ip_addr_json.destroy()
            except AttributeError:
                pass

            try:
                self.download_file.destroy()
            except AttributeError:
                pass

            try:
                self.upload_file.destroy()
            except AttributeError:
                pass

            try:
                self.filename.destroy()
            except AttributeError:
                pass

            try:
                self.name_of_apk.destroy()
            except AttributeError:
                pass

            try:
                self.apk_package_name.destroy()
            except AttributeError:
                pass

            try:
                self.screenshot_file.destroy()
            except AttributeError:
                pass

            try:
                self.name_of_file.destroy()
            except AttributeError:
                pass

            try:
                self.new_content.destroy()
            except AttributeError:
                pass

            self.ip_addr = customtkinter.CTkEntry(master=self.frame_middle, width=400, placeholder_text="IP Address of the Android device")
            self.ip_addr.grid(row=6, column=1, pady=10, padx=20)

            def submit():
                reboot_output = getoutput(f'{adb} reboot {self.ip_addr.get()}')
                print(f"{INFO_CODE} {reboot_output}")

                self.droid_logs_lvl_7 = customtkinter.CTkLabel(master=self.frame_right, text=f"{INFO_CODE} {reboot_output}", corner_radius=6, fg_color=("white", "gray38"))
                self.droid_logs_lvl_7.grid(row=7, column=1, columnspan=5, rowspan=1, pady=5, padx=5, sticky="nsew")

            self.start_reboot = customtkinter.CTkButton(master=self.frame_middle, text="Submit", command=submit)
            self.start_reboot.grid(row=7, column=1, pady=10, padx=20)

        def btn_screenshot(self):

            # Buttons
            try:
                self.start_connect.destroy()
            except AttributeError:
                pass

            try:
                self.start_file_download.destroy()
            except AttributeError:
                pass

            try:
                self.start_file_upload.destroy()
            except AttributeError:
                pass

            try:
                self.start_apk_upload.destroy()
            except AttributeError:
                pass

            try:
                self.start_apk_remove.destroy()
            except AttributeError:
                pass

            try:
                self.start_disconnect.destroy()
            except AttributeError:
                pass

            try:
                self.start_reboot.destroy()
            except AttributeError:
                pass

            try:
                self.start_bluetooth.destroy()
            except AttributeError:
                pass

            try:
                self.stop_bluetooth.destroy()
            except AttributeError:
                pass

            try:
                self.start_wifi.destroy()
            except AttributeError:
                pass

            try:
                self.stop_wifi.destroy()
            except AttributeError:
                pass

            try:
                self.start_file_modification.destroy()
            except AttributeError:
                pass

            # Input Fields
            try:
                self.ip_addr.destroy()
            except AttributeError:
                pass

            try:
                self.json_file_name.destroy()
            except AttributeError:
                pass

            try:
                self.ip_addr_json.destroy()
            except AttributeError:
                pass

            try:
                self.download_file.destroy()
            except AttributeError:
                pass

            try:
                self.upload_file.destroy()
            except AttributeError:
                pass

            try:
                self.filename.destroy()
            except AttributeError:
                pass

            try:
                self.name_of_apk.destroy()
            except AttributeError:
                pass

            try:
                self.apk_package_name.destroy()
            except AttributeError:
                pass

            try:
                self.ip_addr.destroy()
            except AttributeError:
                pass

            try:
                self.name_of_file.destroy()
            except AttributeError:
                pass

            try:
                self.new_content.destroy()
            except AttributeError:
                pass

            self.screenshot_file = customtkinter.CTkEntry(master=self.frame_middle, width=400, placeholder_text="Filename (omit extension)")
            self.screenshot_file.grid(row=6, column=1, pady=10, padx=20)

            def submit():
                screenshot_output = getoutput(f"{adb} exec-out screencap -p > droid_{self.screenshot_file.get()}.png")
                print(f"{INFO_CODE} {screenshot_output}")

                self.droid_logs_lvl_8 = customtkinter.CTkLabel(master=self.frame_right, text=f"{INFO_CODE} {screenshot_output}", corner_radius=6, fg_color=("white", "gray38"))
                self.droid_logs_lvl_8.grid(row=8, column=1, columnspan=5, rowspan=1, pady=5, padx=5, sticky="nsew")

            self.start_screenshot = customtkinter.CTkButton(master=self.frame_middle, text="Submit", command=submit)
            self.start_screenshot.grid(row=7, column=1, pady=10, padx=20)

        def btn_bluetooth(self):

            # Buttons
            try:
                self.start_connect.destroy()
            except AttributeError:
                pass

            try:
                self.start_file_download.destroy()
            except AttributeError:
                pass

            try:
                self.start_file_upload.destroy()
            except AttributeError:
                pass

            try:
                self.start_apk_upload.destroy()
            except AttributeError:
                pass

            try:
                self.start_apk_remove.destroy()
            except AttributeError:
                pass

            try:
                self.start_disconnect.destroy()
            except AttributeError:
                pass

            try:
                self.start_reboot.destroy()
            except AttributeError:
                pass

            try:
                self.start_screenshot.destroy()
            except AttributeError:
                pass

            try:
                self.start_bluetooth.destroy()
            except AttributeError:
                pass

            try:
                self.stop_bluetooth.destroy()
            except AttributeError:
                pass

            try:
                self.start_wifi.destroy()
            except AttributeError:
                pass

            try:
                self.stop_wifi.destroy()
            except AttributeError:
                pass

            try:
                self.start_file_modification.destroy()
            except AttributeError:
                pass

            # Input Fields
            try:
                self.ip_addr.destroy()
            except AttributeError:
                pass

            try:
                self.json_file_name.destroy()
            except AttributeError:
                pass

            try:
                self.ip_addr_json.destroy()
            except AttributeError:
                pass

            try:
                self.upload_file.destroy()
            except AttributeError:
                pass

            try:
                self.filename.destroy()
            except AttributeError:
                pass

            try:
                self.name_of_apk.destroy()
            except AttributeError:
                pass

            try:
                self.apk_package_name.destroy()
            except AttributeError:
                pass

            try:
                self.ip_addr.destroy()
            except AttributeError:
                pass

            try:
                self.screenshot_file.destroy()
            except AttributeError:
                pass

            try:
                self.name_of_file.destroy()
            except AttributeError:
                pass

            try:
                self.new_content.destroy()
            except AttributeError:
                pass

            try:
                self.download_file.destroy()
            except AttributeError:
                pass

            def start_bluetooth():
                # Restarts adb in root
                root_output = getoutput(f'{adb} root')

                # Starts bluetooth service
                bluetooth_output = getoutput(f'{adb} shell service call bluetooth_manager 6')

                print(f"{INFO_CODE} {root_output}")
                print(f"{INFO_CODE} {bluetooth_output}")

                self.droid_logs_lvl_9 = customtkinter.CTkLabel(master=self.frame_right, text=f"{INFO_CODE} {root_output}", corner_radius=6, fg_color=("white", "gray38"))
                self.droid_logs_lvl_9.grid(row=9, column=1, columnspan=5, rowspan=1, pady=5, padx=5, sticky="nsew")

                self.droid_logs_lvl_10 = customtkinter.CTkLabel(master=self.frame_right, text=f"{INFO_CODE} {bluetooth_output}", corner_radius=6, fg_color=("white", "gray38"))
                self.droid_logs_lvl_10.grid(row=10, column=1, columnspan=5, rowspan=1, pady=5, padx=5, sticky="nsew")
            
            def stop_bluetooth():
                # Restarts adb in root
                root_output = getoutput(f'{adb} root')

                # Stops bluetooth service
                bluetooth_output = getoutput(f'{adb} shell service call bluetooth_manager 8')

                print(f"{INFO_CODE} {root_output}")
                print(f"{INFO_CODE} {bluetooth_output}")

                self.droid_logs_lvl_11 = customtkinter.CTkLabel(master=self.frame_right, text=f"{INFO_CODE} {root_output}", corner_radius=6, fg_color=("white", "gray38"))
                self.droid_logs_lvl_11.grid(row=11, column=1, columnspan=5, rowspan=1, pady=5, padx=5, sticky="nsew")

                self.droid_logs_lvl_12 = customtkinter.CTkLabel(master=self.frame_right, text=f"{INFO_CODE} {bluetooth_output}", corner_radius=6, fg_color=("white", "gray38"))
                self.droid_logs_lvl_12.grid(row=12, column=1, columnspan=5, rowspan=1, pady=5, padx=5, sticky="nsew")

            
            self.start_bluetooth = customtkinter.CTkButton(master=self.frame_middle, text="Start Bluetooth", command=start_bluetooth)
            self.start_bluetooth.grid(row=1, column=0, pady=10, padx=20)

            self.stop_bluetooth = customtkinter.CTkButton(master=self.frame_middle, text="Stop Bluetooth", command=stop_bluetooth)
            self.stop_bluetooth.grid(row=2, column=0, pady=10, padx=20)

        def btn_wifi(self):

            # Buttons
            try:
                self.start_connect.destroy()
            except AttributeError:
                pass

            try:
                self.start_file_download.destroy()
            except AttributeError:
                pass

            try:
                self.start_file_upload.destroy()
            except AttributeError:
                pass

            try:
                self.start_apk_upload.destroy()
            except AttributeError:
                pass

            try:
                self.start_apk_remove.destroy()
            except AttributeError:
                pass

            try:
                self.start_disconnect.destroy()
            except AttributeError:
                pass

            try:
                self.start_reboot.destroy()
            except AttributeError:
                pass

            try:
                self.start_screenshot.destroy()
            except AttributeError:
                pass

            try:
                self.start_bluetooth.destroy()
            except AttributeError:
                pass

            try:
                self.stop_bluetooth.destroy()
            except AttributeError:
                pass

            try:
                self.start_file_modification.destroy()
            except AttributeError:
                pass

            # Input Fields
            try:
                self.ip_addr.destroy()
            except AttributeError:
                pass

            try:
                self.json_file_name.destroy()
            except AttributeError:
                pass

            try:
                self.ip_addr_json.destroy()
            except AttributeError:
                pass

            try:
                self.upload_file.destroy()
            except AttributeError:
                pass

            try:
                self.filename.destroy()
            except AttributeError:
                pass

            try:
                self.name_of_apk.destroy()
            except AttributeError:
                pass

            try:
                self.apk_package_name.destroy()
            except AttributeError:
                pass

            try:
                self.ip_addr.destroy()
            except AttributeError:
                pass

            try:
                self.screenshot_file.destroy()
            except AttributeError:
                pass

            try:
                self.name_of_file.destroy()
            except AttributeError:
                pass

            try:
                self.new_content.destroy()
            except AttributeError:
                pass

            try:
                self.download_file.destroy()
            except AttributeError:
                pass

            def start_wifi():
                # Restarts adb in root
                root_output = getoutput(f'{adb} root')

                # Starts wifi service
                wifi_output = getoutput(f"{adb} shell 'svc wifi enable'")

                print(f"{INFO_CODE} {root_output}")
                print(f"{INFO_CODE} {wifi_output}")

                self.droid_logs_lvl_13 = customtkinter.CTkLabel(master=self.frame_right, text=f"{INFO_CODE} {root_output}", corner_radius=6, fg_color=("white", "gray38"))
                self.droid_logs_lvl_13.grid(row=13, column=1, columnspan=5, rowspan=1, pady=5, padx=5, sticky="nsew")

                self.droid_logs_lvl_14 = customtkinter.CTkLabel(master=self.frame_right, text=f"{INFO_CODE} {wifi_output}", corner_radius=6, fg_color=("white", "gray38"))
                self.droid_logs_lvl_14.grid(row=14, column=1, columnspan=5, rowspan=1, pady=5, padx=5, sticky="nsew")

            def stop_wifi():
                # Restarts adb in root
                root_output = getoutput(f'{adb} root')

                # Stops wifi service
                wifi_output = getoutput(f"{adb} shell 'svc wifi disable'")

                print(f"{INFO_CODE} {root_output}")
                print(f"{INFO_CODE} {wifi_output}")

                self.droid_logs_lvl_15 = customtkinter.CTkLabel(master=self.frame_right, text=f"{INFO_CODE} {root_output}", corner_radius=6, fg_color=("white", "gray38"))
                self.droid_logs_lvl_15.grid(row=15, column=1, columnspan=5, rowspan=1, pady=5, padx=5, sticky="nsew")

                self.droid_logs_lvl_16 = customtkinter.CTkLabel(master=self.frame_right, text=f"{INFO_CODE} {wifi_output}", corner_radius=6, fg_color=("white", "gray38"))
                self.droid_logs_lvl_16.grid(row=16, column=1, columnspan=5, rowspan=1, pady=5, padx=5, sticky="nsew")


            self.start_wifi = customtkinter.CTkButton(master=self.frame_middle, text="Start Wifi", command=start_wifi)
            self.start_wifi.grid(row=1, column=0, pady=10, padx=20)

            self.stop_wifi = customtkinter.CTkButton(master=self.frame_middle, text="Stop Wifi", command=stop_wifi)
            self.stop_wifi.grid(row=2, column=0, pady=10, padx=20)

        def btn_modify_file(self):

            # Buttons
            try:
                self.start_connect.destroy()
            except AttributeError:
                pass

            try:
                self.start_file_download.destroy()
            except AttributeError:
                pass

            try:
                self.start_file_upload.destroy()
            except AttributeError:
                pass

            try:
                self.start_apk_upload.destroy()
            except AttributeError:
                pass

            try:
                self.start_apk_remove.destroy()
            except AttributeError:
                pass

            try:
                self.start_disconnect.destroy()
            except AttributeError:
                pass

            try:
                self.start_reboot.destroy()
            except AttributeError:
                pass

            try:
                self.start_screenshot.destroy()
            except AttributeError:
                pass

            try:
                self.start_bluetooth.destroy()
            except AttributeError:
                pass

            try:
                self.stop_bluetooth.destroy()
            except AttributeError:
                pass

            try:
                self.start_wifi.destroy()
            except AttributeError:
                pass

            try:
                self.stop_wifi.destroy()
            except AttributeError:
                pass

            # Input Fields
            try:
                self.ip_addr.destroy()
            except AttributeError:
                pass

            try:
                self.json_file_name.destroy()
            except AttributeError:
                pass

            try:
                self.ip_addr_json.destroy()
            except AttributeError:
                pass

            try:
                self.download_file.destroy()
            except AttributeError:
                pass

            try:
                self.upload_file.destroy()
            except AttributeError:
                pass

            try:
                self.filename.destroy()
            except AttributeError:
                pass

            try:
                self.name_of_apk.destroy()
            except AttributeError:
                pass

            try:
                self.apk_package_name.destroy()
            except AttributeError:
                pass

            try:
                self.ip_addr.destroy()
            except AttributeError:
                pass

            try:
                self.screenshot_file.destroy()
            except AttributeError:
                pass
            
            self.name_of_file = customtkinter.CTkEntry(master=self.frame_middle, width=400, placeholder_text="Name of the file to modify")
            self.name_of_file.grid(row=6, column=1, pady=10, padx=20)

            self.new_content = customtkinter.CTkEntry(master=self.frame_middle, width=400, placeholder_text="Content to add into the modified file")
            self.new_content.grid(row=7, column=1, pady=10, padx=20)

            def submit():
                # Modifies a file without downloading the file
                file_write_output = getoutput(f"{adb} shell 'echo '{self.new_content.get()}' > {self.name_of_file.get()}'")
                print(f"{INFO_CODE} {file_write_output}")

                self.droid_logs_lvl_17 = customtkinter.CTkLabel(master=self.frame_right, text=f"{INFO_CODE} {file_write_output}", corner_radius=6, fg_color=("white", "gray38"))
                
                self.droid_logs_lvl_17.grid(row=17, column=1, columnspan=5, rowspan=1, pady=5, padx=5, sticky="nsew")

            self.start_file_modification = customtkinter.CTkButton(master=self.frame_middle, text="Submit", command=submit)
            self.start_file_modification.grid(row=8, column=1, pady=10, padx=20)
        
        def btn_help(self):
            msg = "\n \
                Connect    | Connects to the Android device\n \
                Disconnect | Disconnects from the Android device\n \
                Reboot     | Remotely reboots the Android device\n \
                Screenshot | Takes a screenshot of the current screen\n \
                Download   | Download a file from the Android device\n \
                Upload     | Upload a file to the Android device\n \
                Remove APK | Remove an apk from the Android device\n \
                Upload APK | Upload an apk to the Android device\n \
                Bluetooth  | Start/stop the Bluetooth service\n \
                Wifi       | Start/stop the Wifi service\n \
                Close      | Closes Droid and disconnects from Android device\n \
                Modify     | Modify a file on the Android device without downloading anything\n \
                Help       | This help menu\n \
            "

            print(msg)

            messagebox.showinfo("Help Menu", "Check terminal for help menu")

        def btn_destroy(self):
            print("Exiting...")
            time.sleep(1)
            self.destroy()
