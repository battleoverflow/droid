# Droid
Droid is a remote communications script created to communicate with Android devices on the local network over the Android debug bridge (adb)

NOTE: Script does require Android debug bridge (adb) to be installed before 

First release is now available! Versions for Linux and macOS are currently available.

## Usage
```bash
./droid -ip 127.0.0.1
```

## Options
```
-ip,  --ip_address  |   IP address of the Android device
-up,  --upload      |   Absolute path of the APK to upload (ex: ~/Downloads/ApkName.apk)
-rm,  --remove      |   Removes the old APK with the same package name (requires the -p flag)
-c,   --connect     |   Connects to the Android device (requires the -ip flag)
-d,   --disconnect  |   Disconnects from the Android device
-r,   --reboot      |   Remotely reboots the Android device
-p,   --package     |   The package name of the APK you would like to replace (ex: com.android.ui)
-dn,  --download    |   Download a file from the Android device
-f,   --file        |   Name of the file on your local machine (ex: ~/Downloads/ApkName.apk)
-loc, --location    |   Location on the Android device to push or remove the selected file (ex: /sdcard/Downloads)
-rmf, --rmfile      |   Remove a file from the Android device (set the absolute path using -loc)
-bl,  --bluetooth   |   Start or stop bluetooth service for the Android device
-w,  --wifi         |   Start or stop wifi service for the Android device
```

I would recommend running this command before doing anything else to confirm you can successfully connect to the Android device on your network
```bash
./droid -ip 127.0.0.1 -c
```

## Example(s)
This example connects to the Android device (127.0.0.1), removes the specified APK package (`com.android.ui`), and then uploads a new APK called `test_apk_v1.apk`
```bash
./droid -ip 127.0.0.1 -c -rm -p com.android.ui -up ~/Downloads/test_apk_v1.apk
```

This example downloads a test images from the Android device onto your local machine (automatically saves it in the ~/Downloads folder on most platforms)
```bash
./droid -ip 127.0.0.1 --download /sdcard/cool_pic.png
```

Once you're finished working within the environment, you can run this command to disconnect from the Android device:
```bash
./droid -ip 127.0.0.1 -d
```

We now have the option to control the bluetooth service on Android devices. You can `start` the service by running this command (stopping the service uses the `stop` argument):
```bash
./droid -ip 127.0.0.1 -bl=start
```

You can `stop` the service by running this command (starting the service uses the `start` argument):
```bash
./droid -ip 127.0.0.1 -w=stop
```
NOTE: When turning the wifi off, if you are communicating with the Android device remotely, this will result in the device being disconnected and unusable until the network is re-established.