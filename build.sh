#!/bin/bash

function build_droid() {
    echo "Generating executable..."

    user=$(whoami)
    version="1.4.21"

    if [[ "$OSTYPE" == "linux-gnu"* ]]
    then
        # Linux
        pyinstaller --noconfirm --onefile --add-data "/home/$user/.local/lib/python3.8/site-packages/customtkinter:customtkinter/" "droid/main.py" --name droid_$(uname)_$(uname -i)_v$version
    elif [[ "$OSTYPE" == "darwin"* ]]
    then
        # macOS
        pyinstaller --noconfirm --onefile --add-data "/opt/homebrew/lib/python3.11/site-packages/customtkinter:customtkinter/" "droid/main.py" --name droid_$(uname)_v$version
    else
        echo "$OSTYPE is not supported yet"
    fi
}

build_droid
