# Droid
Droid is a remote communications script created to communicate with an Android device on the local network over the Android debug bridge (adb) in a much easier way

NOTE: Script does require Android platform tools (adb) to be installed

## Usage
```bash
python3 droid.py -ip 127.0.0.1
```

## Options
```
-ip, --ip_address  |   IP address of the Android device
-up, --upload      |   Name & location of the APK to upload (ex: ~/Downloads/ApkName.apk)
-rm, --remove      |   Removes the old APK with the same package name
-c,  --connect     |   Connects to the Android device
-d,  --disconnect  |   Disconnects from the Android device
-r,  --reboot      |   Remotely reboots the Android device
-p,  --package     |   The package name of the APK (ex: com.android.ui)
-dn,  --download   |   Download a file from the Android device
-ps,  --push       |   Name & location of the file on your local machine
-loc,  --location  |   Location on the Android device to push the selected file
```

I would recommend running this command before doing anything else to confirm you can successfully connect to the Android device on your network
```bash
python3 droid.py -ip 127.0.0.1 -c
```

## Example(s)
This example connects to the Android device (127.0.0.1 is an example), removes the specified APK package (`com.android.ui`), and then uploads a new APK called `test_apk_v1.apk`
```bash
python3 droid.py -ip 127.0.0.1 -c -rm -p com.android.ui -up ~/Downloads/test_apk_v1.apk
```

This example connects to the Android device (127.0.0.1 is an example) and downloads an image
```bash
python3 droid.py -ip 127.0.0.1 --download /sdcard/cool_pic.png
```

Once you're finished working within the Android environment, you can run this command to disconnect:
```bash
python3 droid.py -ip 127.0.0.1 -d
```
