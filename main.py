# ------------------------------------------------------------------------------------------#
#                                                                                           #
# main.py                                                                                   #
#                                                                                           #
# Author(s): Hifumi1337                                                                     #
# ------------------------------------------------------------------------------------------#

import os, argparse, sys, time, platform
from subprocess import getoutput
from utils.view import View

author = "Hifumi1337"
version = "1.2.9"

parser = argparse.ArgumentParser()

parser.add_argument('-v', '--version', help="Version information", action='store_true', default=None, required=False)
parser.add_argument('-ip', '--ip_address', help="IP address of the Android device", default=None, required=False)
parser.add_argument('-up', '--upload', help="Name & location of the APK to upload (ex: ~/Downloads/ApkName.apk)", default=None, required=False)
parser.add_argument('-rm', '--remove', help="Removes the old APK with the same package name", action='store_true', default=False, required=False)
parser.add_argument('-c', '--connect', help="Connects to the Android device", action='store_true', default=False, required=False)
parser.add_argument('-d', '--disconnect', help="Disconnects from the Android device", action='store_true', default=False, required=False)
parser.add_argument('-r', '--reboot', help="Remotely reboots the Android device", action='store_true', default=False, required=False)
parser.add_argument('-p', '--package', help="The package name of the APK (ex: com.android.ui)", default=None, required=False)
parser.add_argument('-dn', '--download', help="Download a file from the Android device", default=None, required=False)
parser.add_argument('-f', '--file', help="Name & location of the file on your local machine", default=None, required=False)
parser.add_argument('-loc', '--location', help="Location on the Android device to push or remove the selected file", default=None, required=False)
parser.add_argument('-rmf', '--rmfile', help="Remove a file from the Android device (set the absolute path using -loc)", action='store_true', default=False, required=False)
parser.add_argument('-bl', '--bluetooth', help="Start or stop bluetooth service for the Android device", default=None, required=False)
parser.add_argument('-w', '--wifi', help="Start or stop wifi service for the Android device", default=None, required=False)
parser.add_argument('-g', '--gui', help="Opens Droid in a graphical user interface (setting other args does not auto-populate)", action='store_true', default=False, required=False)

args = parser.parse_args()

class Droid:

    def banner(self):
        print(f"""
            ·▄▄▄▄  ▄▄▄        ▪  ·▄▄▄▄  
            ██· ██ ▀▄ █· ▄█▀▄ ██ ██· ██ 
            ▐█▪ ▐█▌▐▀▀▄ ▐█▌.▐▌▐█·▐█▪ ▐█▌
            ██. ██ ▐█•█▌▐█▌.▐▌▐█▌██. ██ 
            ▀▀▀▀▀• .▀  ▀ ▀█▄▀▪▀▀▀▀▀▀▀▀• 
                
                {author} | v{version}
        """)

    def main(self):

        # Default adb location on macOS, Windows, and Linux
        if platform.system() == 'Darwin':
            adb = "$HOME/Library/Android/sdk/platform-tools/adb"
        elif platform.system() == 'Windows':
            adb = "%LOCALAPPDATA%\Android\sdk\platform-tools\\adb"
        elif platform.system() == 'Linux':
            whoami = getoutput("whoami")
            adb = f"/home/{whoami}/Android/Sdk/platform-tools/adb"
        
        """
        Connect to the Android device
        """
        def connect_ip(self):
            try:
                ip_address = args.ip_address
                print("Connecting...")
                time.sleep(0.2)
                os.system(f'{adb} connect {ip_address}')
            except:
                print(f"Unable to connect to device: {ip_address}")
                time.sleep(0.5)
                sys.exit(0)
        
        """
        Disconnect from the Android device
        """
        def disconnect_ip(self):
            try:
                ip_address = args.ip_address
                print("Disconnecting...")
                time.sleep(0.2)
                os.system(f'{adb} disconnect {ip_address}')
            except:
                print(f"Unable to disconnect from device: {ip_address}")
                time.sleep(0.5)
                sys.exit(0)

        """
        Allows you to upload an apk from the Android device
        """
        def upload_apk(self):
            try:
                name_of_apk = args.upload
                os.system(f'{adb} install -r {name_of_apk}')
            except:
                print(f"Unable to upload apk: {name_of_apk}")
        
        """
        Allows you to remove an apk from the Android device
        """
        def remove_apk(self):
            try:
                package_name = args.package # Package Name
                os.system(f'{adb} uninstall {package_name}')
            except:
                print(f"Unable to locate: {package_name}")
        
        """
        Allows you to upload a file to the Android device
        """
        def upload_file(self):
            try:
                name_of_file = args.file
                location_to_push = args.location
                os.system(f'{adb} push {name_of_file} {location_to_push}')
            except:
                print(f"Unable to upload file: {name_of_file}")
        
        """
        Allows you to remove a file from the Android device
        """
        def remove_file(self):
            try:
                location_to_remove = args.location
                os.system(f'{adb} shell rm -rf {location_to_remove}')
            except:
                print(f"Unable to remove: {location_to_remove}")
        
        if args.package == False and args.remove:
            print("A package name is required to remove an apk")
            sys.exit(0)
        
        """
        Reboots the Android device
        """
        def reboot(self):
            try:
                ip_address = args.ip_address
                os.system(f"{adb} reboot {ip_address}")
            except:
                print("Device is unresponsive. Please check connection")
        
        """
        Downloads a file from the Android device
        """
        def download(self):
            try:
                file_location = args.download
                os.system(f"{adb} pull {file_location}")
            except:
                print(f"Unable to locate file: {file_location}")
        
        """
        Controls the bluetooth service on the Android device
        """
        def bluetooth(self):
            if args.bluetooth == 'start':
                try:
                    os.system(f'{adb} root')
                    os.system(f'{adb} shell service call bluetooth_manager 6') # Starts bluetooth service
                except:
                    print("Unable to start bluetooth service")
            elif args.bluetooth == 'stop':
                try:
                    os.system(f'{adb} root')
                    os.system(f'{adb} shell service call bluetooth_manager 8') # Stops bluetooth service
                except:
                    print("Unable to stop bluetooth service")
            else:
                print("Please set to either start or stop for your desired response")
        
        """
        Controls the wifi service on the Android device
        """
        def wifi(self):
            if args.wifi == 'start':
                try:
                    os.system(f'{adb} root')
                    os.system(f"{adb} shell 'svc wifi enable'") # Starts wifi service
                except:
                    print("Unable to start wifi service")
            elif args.wifi == 'stop':
                try:
                    os.system(f'{adb} root')
                    os.system(f"{adb} shell 'svc wifi disable'") # Stops wifi service
                except:
                    print("Unable to stop wifi service")
            else:
                print("Please set to either start or stop for your desired response")

if __name__ == '__main__':

    if len(sys.argv) > 1:

        d = Droid()

        if args.connect:
            d.banner()

            try:
                d.connect_ip()
            except AttributeError:
                print("Please enter an IP address using this: -ip")

        if args.remove and args.package:
            d.banner()
            d.remove_apk()
        
        if args.file and args.location:
            d.banner()
            d.upload_file()
        
        if args.rmfile and args.location:
            d.banner()
            d.remove_file()

        if args.upload:
            d.banner()
            d.upload_apk()
        
        if args.download:
            d.banner()
            d.download()

        if args.reboot:
            d.banner()
            d.reboot()
        
        if args.disconnect:
            d.banner()
            d.disconnect_ip()
        
        if args.bluetooth:
            d.banner()
            d.bluetooth()
        
        if args.wifi:
            d.banner()
            d.wifi()
        
        if args.version:
            print(f"Droid Version: {version}")

        if args.gui:
            d.banner()

            v = View(version)

            try:
                v.__init__()
            except TypeError:
                pass
    else:
        print("Nothing happened. Try using this: -h")
        exit(0)