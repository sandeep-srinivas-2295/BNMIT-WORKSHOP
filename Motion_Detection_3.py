#Importing the GPIO libraries
import RPi.GPIO as GPIO

#Import time libraries
import time

#Enable the BCM mode
GPIO.setmode(GPIO.BCM)

#Define variable and assign the GPIO pins
#Here GPIO4 is connected to Motion sensor OUT pin
Motion_Sensor = 4

#Here GPIO17 is connected to Buzzer pin
Buzzer = 17

#Setting the GPIO4 as input pin to send recieve the value from
MotionSensor
GPIO.setup(Motion_Sensor, GPIO.IN)

#Setting the GPIO17 as output pin to turn on the buzzer
GPIO.setup(Buzzer, GPIO.OUT)

try:
    #delay for 2 seconds
    time.sleep(1)
    print ("Motion Sensor is ON")
    #While loop to continously detect the motion
    while True:
        if GPIO.input(Motion_Sensor):
            print ("####### Motion Detected! ########")
            GPIO.output(Buzzer, GPIO.HIGH)
            print ("Buzzer is ON")
            time.sleep(1)
        else:
            print ("Nothing Detected!")
            GPIO.output(Buzzer, GPIO.LOW)
            time.sleep(1)
except KeyboardInterrupt:
    print ("Quit")
    GPIO.cleanup()



GPIO.cleanup()
