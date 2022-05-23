# Droid
Droid is an Android remote communications script created to communicate with an Android device on the local network over the Android debug bridge (adb).

## Usage
```bash
python3 droid.py
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
-i,  --info        |   Learn more about the Android device
-dn,  --download   |   Download a file from the Android device
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

This example connects to the Android device (127.0.0.1 is an example), downloads an image, and then shows information about the Android device
```bash
python3 droid.py -ip 127.0.0.1 --download /sdcard/cool_pic.png -i
```

Once you're finished working within the Android environment, you can run this command to disconnect:
```bash
python3 droid.py -ip 127.0.0.1 -d
```