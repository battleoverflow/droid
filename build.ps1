# RUN BEFORE: powershell -ep bypass

function Build-Droid {
    $loggedInUser = ([System.Environment]::UserName)
    $version = "1.4.21"

    if (((Get-CimInstance -ClassName CIM_OperatingSystem).OSArchitecture) == "ARM 64-bit Processor") {
        $arch = "arm_64"
    } else {
        $arch = ((Get-CimInstance -ClassName CIM_OperatingSystem).OSArchitecture)
    }

    echo "Generating executable..."

    # Windows
    pyinstaller.exe --noconfirm --onefile --add-data "C:\Users\$loggedInUser\AppData\Local\Programs\Python\Python311-arm64\Lib\site-packages\customtkinter;customtkinter/" "droid/main.py" --name droid_Windows_$arch_v$version
}

Build-Droid
