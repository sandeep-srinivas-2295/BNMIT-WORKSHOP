"""
Connect the LED Anode to GPIO14
Connect the ground to GND
"""

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14,GPIO.OUT)

while True:
    command = input("Type 'ON' to turn On the light and 'OFF' to turn off the light: ")
    if command == "ON":
        GPIO.output(14,GPIO.HIGH)
        print("Light is ON")
    if command == "OFF":
        GPIO.output(14,GPIO.LOW)
        print("Light is OFF")
