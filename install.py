"""
File: install.py
Author: lnus 
Github: https://github.com/lnus
Description: Installs all the required things for Mp3DL-Lite
"""

import os

"""
Installs correct version of PyTube
Creates the folder Mp3DL on the C drive
It puts the mp3.bat script file in there
It puts the install.py script file in there
"""

os.system("pip install pytube==6.2.2")
os.system("mkdir C:\\Mp3DL")
os.system("copy Installfiles\\mp3.bat C:\\Mp3DL\\mp3.bat")
os.system("copy main.py C:\\Mp3DL\\main.py")
