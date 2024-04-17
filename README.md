# Droid

<img src="https://raw.githubusercontent.com/battleoverflow/droid/main/.github/assets/droid_logo.png" />

Droid is a desktop application created to communicate with Android devices on the local network over the Android debug bridge (adb). You can access the Android device directly over USB or connect to the device through Droid via `adb`. Droid allows you to completely control the Android device using multiple options, including a CLI and a GUI.

IMPORTANT NOTE: Application does require Android debug bridge (adb) to be installed on the system.

## Install

Droid can be installed via `pip`

```bash
pip install droid
```

You can also download the executable from `itch.io`: https://battleoverflow.itch.io/droid

## GUI

If you would like to run the GUI, you can run this command to boot it up

```bash
droid

# or

droid -g
```

Current state of the user interface

<img src="https://raw.githubusercontent.com/battleoverflow/droid/main/.github/assets/gui.png" />

## Simple usage (CLI)

```bash
droid -ip 127.0.0.1 -c
```

## Options

```
-h,   --help	    |	Help menu
-v,   --version	    |	Version information for Droid
-ip,  --ip_address  |   IP address of the Android device
-up,  --upload      |   Absolute path of the APK to upload (ex: ~/Downloads/ApkName.apk)
-rm,  --remove      |   Removes the old APK with the same package name (requires the -p flag)
-c,   --connect     |   Connects to the Android device (requires the -ip flag)
-d,   --disconnect  |   Disconnects from the Android device
-r,   --reboot      |   Remotely reboots the Android device
-p,   --package     |   The package name of the APK you would like to replace (ex: com.android.ui)
-dn,  --download    |   Download a file from the Android device
-f,   --file        |   Name of the file on your local machine (ex: ~/Downloads/ApkName.apk)
-fs,  --file_system |   Name & location of the file on the Android device
-loc, --location    |   Location on the Android device to push or remove the selected file (ex: /sdcard/Downloads)
-rmf, --rmfile      |   Remove a file from the Android device (set the absolute path using -loc)
-bl,  --bluetooth   |   Start or stop bluetooth service for the Android device
-w,  --wifi         |   Start or stop wifi service for the Android device
-s,  --screenshot   |   Take a screenshot of the current Android screen
-o,  --output       |   Name of the output file when taking a screenshot (omit the extension)
-l,  --log          |   Outputs Logcat logs in real time to a set file
-g,  --gui          |   A graphical user interface built to communicate with an Android device
-co   --content     |   Update a file on the Android device without downloading it
```

I would recommend running this command before doing anything else to confirm you can successfully connect to the Android device on your network

```bash
droid -ip 127.0.0.1 -c
```

## Example(s)

This example connects to the Android device (127.0.0.1), removes the specified APK package (`com.android.ui`), and then uploads a new APK called `test_apk_v1.apk`

```bash
droid -ip 127.0.0.1 -c -rm -p com.android.ui -up ~/Downloads/test_apk_v1.apk
```

This example downloads a test images from the Android device onto your local machine (automatically saves it in the ~/Downloads folder on most platforms)

```bash
droid -ip 127.0.0.1 --download /sdcard/cool_pic.png
```

Once you're finished working within the environment, you can run this command to disconnect from the Android device:

```bash
droid -ip 127.0.0.1 -d
```

We now have the option to control the bluetooth service on Android devices. You can `start` the service by running this command (stopping the service uses the `stop` argument):

```bash
droid -ip 127.0.0.1 -bl=start
```

You can `stop` the service by running this command (starting the service uses the `start` argument):

```bash
droid -ip 127.0.0.1 -w=stop
```

NOTE: When turning the wifi off, if you are communicating with the Android device remotely, this will result in the device being disconnected and unusable until the network is re-established.

This command will take a screenshot of the current Android screen while monitoring Logcat in real-time:

```bash
droid -ip 127.0.0.1 -sl -o screenshot
```

# More Info

A wiki for common Android snippets is also available. This wiki shows examples of how Droid can used with the Android operating system

Wiki: https://github.com/battleoverflow/droid/wiki/Helpful-Android-Snippets