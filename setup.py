"""
    Owner: battleoverflow (https://github.com/battleoverflow)
    Project: Droid (https://github.com/battleoverflow/droid)
    License: MIT
"""

import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "droid",
    version = "1.4.22",
    author = "battleoverflow",
    description = "Droid is a remote communication application created to communicate with Android devices on the local network over the Android debug bridge (adb). Available as a CLI or GUI.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/battleoverflow/droid",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages = ["droid"],
    install_requires=[
        "argparse",
        "customtkinter==4.6.3"
    ],
    scripts=["droid/main.py"],
    entry_points={
        "console_scripts": ["droid=droid.main:Droid.main"]
    },
    python_requires = ">=3.6"
)