#!/bin/bash

function build_droid() {

    echo "Generating executable..."

    current_os="Unknown"

    if [[ "$OSTYPE" == "linux-gnu"* ]]
    then
        # Linux
        pyinstaller --noconfirm --onefile --add-data "/home/hifumi/.local/lib/python3.8/site-packages/customtkinter:customtkinter/" "main.py" --name droid-$(uname)_$(uname -i)
    elif [[ "$OSTYPE" == "darwin"* ]]
    then
        # macOS
        pyinstaller --noconfirm --onefile --add-data "/usr/local/lib/python3.10/site-packages/customtkinter:customtkinter/" "main.py" --name droid-$(uname)
    else
        pyinstaller --noconfirm --onefile --add-data "/usr/local/lib/python3.10/site-packages/customtkinter;customtkinter/" "main.py" --name droid-$(echo $current_os)
    fi
}

build_droid
