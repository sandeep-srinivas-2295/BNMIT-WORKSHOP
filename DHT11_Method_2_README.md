# BNMIT-WORKSHOP

Software Setup
To start with update your package lists and install a few Python libraries :

**sudo apt-get update**
**sudo apt-get install build-essential python-dev**
Then clone the Adafruit library from their repository :

**git clone https://github.com/adafruit/Adafruit_Python_DHT.git**
**cd Adafruit_Python_DHT**
Then install the library for Python 2 and Python 3 :

**sudo python setup.py install
sudo python3 setup.py install**
Hopefully at this point the library is installed and ready to be used within a Python script.

Adafruit Example Python Script
Adafruit provide an example script that you can use to check your sensor is operating correctly.

**cd ~
cd Adafruit_Python_DHT
cd examples**
Then :

**python3 AdafruitDHT.py 11 4**
The example script takes two parameters. The first is the sensor type so is set to “11” to represent the DHT11. The second is the GPIO number so for my example I am using “04” for GPIO4. You can change this if you are using a different GPIO pin for your data/out wire.

You should see an output similar to this :

Temp=22.0* Humidity=68.0%
