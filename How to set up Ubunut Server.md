# Introduction:

This markdown file (.md) is a step by step installation guide on how to install Ubuntu Server on a Raspberry Pi 4.



# **README**

**NOTE: Be sure Wi-Fi stays connected, otherwise the packages cannot be downloaded.**

**NOTE: Only use** `sudo` **(administratro privlages) when instructed. Using** `sudo` **could corrupt the the system if not careful.**

**NOTE: The following link should be read throughly before continuing:** https://ubuntu.com/tutorials/how-to-install-ubuntu-on-your-raspberry-pi#1-overview




# Istallation of Ubuntu ARM:

1.) Search for a Long Term Support (LTS) version of Ubuntu Server and download the image file.  The LTS versions work best for the Raspberry Pi's.


2.) Once Ubuntu is downloaded flash the image file to the SD card using Raspberry Pi imager or balenaEtcher.


3.) Put the SD card in the Raspberry Pi then power on the Raspberry Pi, let the boot process finish entirely before trying to login.  The user will be prompted to login before the setup process is complete.  A few more lines of output will appear when the setup is complete.

When the output is complete press enter.


4.) When trying to login, the login is:

username: `ubuntu`

password: `ubuntu`



# Setting up the Wi-Fi:

The next step is to set up the Wi-Fi.

1.) Run the following line in the terminal:

    `ls /sys/class/net`

There will be three outputs.  One output will start with `eth`, one output will be `lo`, and the third output will start with `wlan`.  The output that starts with the `wlan` is the name of the Wi-Fi module.  This will needed for the next part of this step.


2.) Run the following in the command terminal:

    `sudo nano /etc/netplan/50-cloud-init.yaml`

This will open the Wi-Fi configuration file.  Make the file look like the block of code below.  Insert the name of the Wi-Fi module, the SSID (name of the Wi-Fi), and the password.

```
# This file i sgenerated from information provided by the datasource. Changes
# to it will not persist across an instance reboot. To disable could-init's
# network configuration capabilities, write a file
# /etc/cloud/cloud.cfg.d/99-disable-network-config.cfg with the following:
# network: {config: disabled}
network:
#    ethernets:
#        eth0:
#            dhcp4: true
#            optional: true
    version: 2
    wifis:
        <name of wi-fi module>:
            dhcp4: true
            optional: true
            access-points:
                "<SSID>":
                     password: "<password>"
```

**NOTE: The two following URL's should be addressed for any questions:**

https://cloudinit.readthedocs.io/

https://netplan.io/reference

**NOTE: Do not include:** `< >` **in the wifi name and and password.**
**NOTE: The** `#` **is the comment operator.**
**NOTE: The** `.yaml` **file does not support tabbing for indentation; use four spaces instead.**


3.) Restart Ubuntu to let any changes take affect:

    `sudo shutdown -r now`


4.) Test and make sure the Wi-Fi is connected to internet:

    `ping -c 5 8.8.8.8`

When executed, the above line will ping the Google DNS Server five times.



# Setting up the Timezone:

The next step to is set up the time zone.

1.) To list all the timezones run:

    `timedatectl list-timezones'


2.) Find needed time zone from the list.


3.) To set the timezone:

    `sudo timedatectl set-timezone <timezone code>`


4.) Check the time by running:

    `timedatectl`


5.) Restart Ubuntu to let any changes take affect:

    `sudo shutdown -r now`



# Updating the System:

1.) In the terminal, run:

    `sudo apt update`

    `sudo apt upgrade`


2.) Remove any unused dependencies:

    `sudo apt autoremove`


3.) Restart Ubuntu to let any changes take affect:

    `sudo shutdown -r now`



# How to Change the Name of the User Account:

The following article should be read before preceeding:

https://www.linuxuprising.com/2019/04/how-to-change-username-on-ubuntu-debian.html



1.) While logged into the user account named "ubuntu", make a new user account called "temp":

    `sudo adduser temp`


A.) Here it is good to note how to change a password:

    `sudo passwd <username>

Ubuntu will prompt the user to enter a password for the new account, then it will ask for information about the new user, such as name, phone number, etc.


2.) Add the "temp" user to the `sudo` user group.

    `sudo usermod -aG sudo temp`


3.) Log out of the the "ubuntu" user account using:

    `exit`


4.) Login under the user account "temp".


5.) To move the contents of the olde user home directory run the following in the command terminal:

    `sudo usermod -l <newusername> -d /home/<newusername> -m <olderusername>`


6.) To change the user name run the following:

    `sudo groupmod -n <newusername> <olderusername>`


7.) Changing the name of the username folder can cause issues with installed software.  The best way to fix this issue is to create a symbolic link between old user home directory and new user home directory.

    `sudo ln -s /home/<newusername> /home/<olderusername>`


8.) To change the display name use the following command:

    `sudo chfn -f "<firstname> <lastname>" <newusername>`


9.) Sign out of the "temp" user by using the `exit` command.


10.) Sign into the changed user account.


11.) Delete the temporary user accound "temp":

    `sudo userdel -r tmep`


12.) To remove the folder for the old ubuntu user:

    `sudo rm -R /home/ubuntu`



# How to Change the Hostname:

1.) Change the hostname file by replacing the old hostname with the new hostname:

    `sudo nano /etc/hostname`


2.) Open the `hosts` file and change any instance of old hostname to the new one.

    `sudo nano /etc/hosts`


3.) Restart Ubuntu to let any changes take effect:

    `sudo shutdown -r now`


4.) This step is optional but it could be desired to enable OpenSSH.  To turn on OpenSSH service at boot time, run the following in the terminal:

    `sudo systemctl enable ssh`

To disable OpenSSH:

    `sudo systemctl disable ssh`

To start OpenSSH when it is not enabled (enabled starts OpenSSH at boot time):

    `sudo systemctl start ssh`

To stop OpenSSH:

    `sudo systemctl stop ssh`



# How to Install a Desktop Environment:

1.) This tutorial will use Lubuntu since it is extremely light-weight.  There are other desktop environments like Xfce, KDE Plasma, Mate, etc.  To install Lubuntu run the following in the terminal:

    `sudo apt install lubuntu-desktop`


2.) Part way through the Lubuntu installation a purple background will show up asking for which graphical manager to use.  Select `gdm3` if the normal login screen is preferred.



3.) Restart Ubuntu to let any updates take affect:

    `sudo shutdown -r now`




