# Introduction:

This markdown file (.md) is a step by step tutorial for creating a disk image of a drive.



# **README**

**NOTE: Only use** `sudo` **(administratro privlages) when instructed. Using** `sudo` **could corrupt the the system if not careful.**

**NOTE:** `dd` **is a powerful tool.  Be careful using because data could accidentally be erased.**

**NOTE: The following links should be read throughly before continuing:**

https://wiki.archlinux.org/title/Dd

https://wiki.archlinux.org/title/file_systems

**The above links may be from the Archlinux Wiki page, but Archlinux has very good documentation and some of it can be carried over to other distributions of Linux.**



# Cloning a Drive/Partition:

1.) The first step is to make directory to mount the drive to:

    sudo mkdir /mnt/external


2.) Insert the flash drive if it is not inserted already.  To generate a list of all the drives connected run:

    sudo fdisk -l

Find the drive to be mounted.


3.) Once the drive is identified, mount the drive by executing the follwing:

    sudo mount /dev/sda1 /mnt/external

Note that `sda` is the device, insert the name of the device from the list generated in step 2.


4.) Now that the device is mounted, it is time to create a disk image of the drive:

    sudo dd if=/dev/sda bs=1M status=progress | xz -z | sudo split -b2G - /mnt/external/backup.img.xz

In the command above, `sda` is the name of the drive to create an image of.  This can also be found from the command in step 2.

`bs` is the block size.

`status=progress` will show the status of the execution.

`xz` will put the file in a `.xz` file.

`split` will split the file into multiple parts.  This is necessary for FAT32 file systems because the largest file size for FAT32 is 4GB.

The command above will take sometime to execute, so be patient.


5.) Get the disk info

    sudo fdisk -l /dev/sda > /path/to/list_fdisk.info


6.) Unmount the drive

    umount /mnt/external
