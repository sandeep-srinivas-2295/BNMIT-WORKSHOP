import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17,GPIO.OUT)

while True:
    GPIO.output(17,GPIO.HIGH)
    print ("LED is on")
    time.sleep(1)
    GPIO.output(17,GPIO.LOW)
    print ("LED is off")
    time.sleep(1)
