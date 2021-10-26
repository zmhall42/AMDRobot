# Introduction

This markdown file (.md) is a step by step installation guide on how to install the needed GPIO python packages needed to work with the GPIO pins on Manjaro ARM installed on the Reaspberry Pi 4 B.



# **README**

**NOTE: Install all packages through the command terminal with root privlages (sudo) (It is not always safe to use root. In this tutorial it is).**

**NOTE: When installing python packages it is best to use pip.  Pip is the package installer recommeded by PyPA (Python Packaging Authority).**

**NOTE: Be sure Wi-Fi stays connected, otherwise the packages cannot be downloaded.**



# Installation of GPIO Packages:


1.) Install the build-essential package

    sudo apt install build-essential


2.) Install the most up to date version of pip. Run the following command in the terminal:

    sudo apt install python3-pip


3.) Restart the raspberry pi to let any updates take effect. Run the following in the command terminal to restart the raspberry pi:

    sudo shutdown -r now


4.) Install RPi.GPIO:

    sudo env CFLAGS="-fcommon" pip install RPi.GPIO


5.) Install gpiozero:

    sudo pip install gpiozero


6.) Restart the raspberry pi to let any updates take effect. Run the following in the command terminal to restart the raspberry pi:

    sudo shutdown -r now



Unbuntu can now interface with the GPIO pins.
