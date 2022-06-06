import os, argparse, sys, time, platform

from subprocess import getoutput

parser = argparse.ArgumentParser()

parser.add_argument('-ip', '--ip_address', help="IP address of the Android device", default=None, required=True)
parser.add_argument('-up', '--upload', help="Name & location of the APK to upload (ex: ~/Downloads/ApkName.apk)", default=None, required=False)
parser.add_argument('-rm', '--remove', help="Removes the old APK with the same package name", action='store_true', default=False, required=False)
parser.add_argument('-c', '--connect', help="Connects to the Android device", action='store_true', default=False, required=False)
parser.add_argument('-d', '--disconnect', help="Disconnects from the Android device", action='store_true', default=False, required=False)
parser.add_argument('-r', '--reboot', help="Remotely reboots the Android device", action='store_true', default=False, required=False)
parser.add_argument('-p', '--package', help="The package name of the APK (ex: com.android.ui)", default=None, required=False)
parser.add_argument('-dn', '--download', help="Download a file from the Android device", default=None, required=False)
parser.add_argument('-ps', '--push', help="Name & location of the file on your local machine", default=None, required=False)
parser.add_argument('-loc', '--location', help="Location on the Android device to push the selected file", default=None, required=False)

args = parser.parse_args()

author = "Hifumi1337"
version = "0.2.6"

if platform.system() == 'Darwin':
    adb = "$HOME/Library/Android/sdk/platform-tools/adb"
elif platform.system() == 'Windows':
    adb = "%LOCALAPPDATA%\Android\sdk\platform-tools/adb"
elif platform.system() == 'Linux':
    whoami = getoutput("whoami")
    adb = f"/home/{whoami}/Android/Sdk/platform-tools/adb"

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

    def connect_ip(self):
        try:
            ip_address = args.ip_address
            print("Connecting...")
            time.sleep(0.2)
            os.system(f'{adb} connect {ip_address}')
        except:
            print(f"Unable to connect to device {ip_address}")
            time.sleep(0.5)
            sys.exit(0)
    
    def disconnect_ip(self):
        try:
            ip_address = args.ip_address
            print("Disconnecting...")
            time.sleep(0.2)
            os.system(f'{adb} disconnect {ip_address}')
        except:
            print(f"Unable to connect to device {ip_address}")
            time.sleep(0.5)
            sys.exit(0)

    def remove_apk(self):
        try:
            package_name = args.package # Package Name
            os.system(f'{adb} uninstall {package_name}')
            print(f"{package_name} successfully removed")
        except:
            print(f"Unable to locate {package_name}")
        
    def upload_apk(self):
        try:
            name_of_apk = args.upload
            os.system(f'{adb} install -r {name_of_apk}')
            print(f"{name_of_apk} successfully uploaded")
        except:
            print(f"{name_of_apk} upload unsuccessful")
    
    def push(self):
        try:
            name_of_file = args.push
            location_to_push = args.location
            os.system(f'{adb} push {name_of_file} {location_to_push}')
            print(f"{name_of_file} successfully uploaded")
        except:
            print(f"{name_of_file} upload unsuccessful")
    
    if args.package == False and args.remove == True:
        print("A package name is required to remove an APK")
        sys.exit(0)
    
    def reboot(self):
        try:
            ip_address = args.ip_address
            os.system(f"{adb} reboot {ip_address}")
        except:
            print("Device is unresponsive. Please check the connection")
        
    def download(self):
        try:
            file_location = args.download
            os.system(f"{adb} pull {file_location}")
        except:
            print(f"Unable to locate {file_location}")

if __name__ == '__main__':
    D = Droid()
    D.banner()

    if args.connect:
        D.connect_ip()

    if args.remove and args.package:
        D.remove_apk()
    
    if args.push and args.location:
        D.push()

    if args.upload:
        D.upload_apk()
    
    if args.download:
        D.download()

    if args.reboot:
        D.reboot()
    
    if args.disconnect:
        D.disconnect_ip()
