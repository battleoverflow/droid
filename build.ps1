# RUN BEFORE: powershell -ep bypass

function Build-Droid {
    $arch = ((Get-CimInstance -ClassName CIM_OperatingSystem).OSArchitecture)
    $loggedInUser = ([System.Environment]::UserName)

    echo "Generating executable..."

    # Windows
    pyinstaller.exe --noconfirm --onefile --add-data "c:\users\$loggedInUser\appdata\local\programs\python\python39\lib\site-packages\customtkinter;customtkinter/" "main.py" --name droid-Windows_$arch
}

Build-Droid
