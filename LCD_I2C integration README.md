# BNMIT-WORKSHOP

**LCD with I2C display uisng Raspberry Pi**
Steps to install and run the code to get the display

- Install git

**sudo apt install git**

- Clone the repo in your pi home directory

**cd /home/pi/**
**git clone https://github.com/the-raspberry-pi-guy/lcd.git**
**cd lcd/**

- Run the automatic installation script with sudo permission

**sudo ./install.sh**

-During the installation, pay attention to any messages about python and python3 usage, as they inform which version you should use to interface with the LCD driver. For example:

[LCD] [INFO] You may use either 'python' or 'python3' to interface with the lcd.
or alternatively,

[LCD] [INFO] Use 'python3' to interface with the lcd.
At the end of the installation script, you'll be prompted to reboot the RPi to apply the changes made to /boot/config.txt and /etc/modules.

After rebooting, try one of the demos:

**./home/pi/lcd/demo_clock.py**
or

**python /home/pi/lcd/demo_clock.py**
or

**python3 /home/pi/lcd/demo_clock.py**
