import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17,GPIO.OUT) #Connect pin GPIO17 to RED LED
GPIO.setup(18,GPIO.OUT) #Connect pin GPIO18 to Yellow LED
GPIO.setup(27,GPIO.OUT) #Connect pin GPIO27 to Green LED

while True:
    #Turn on the Red LED
    GPIO.output(17,GPIO.HIGH)
    print ("Stop")
    time.sleep(10)

    #Turn on the Yellow LED
    GPIO.output(17,GPIO.LOW)
    GPIO.output(18,GPIO.HIGH)
    print ("Get ready")
    time.sleep(3)

    #Turn on the Green LED
    GPIO.output(18,GPIO.LOW)
    GPIO.output(27,GPIO.HIGH)
    print ("Go go")
    time.sleep(10)

    #Turn on the Yellow LED
    GPIO.output(27,GPIO.LOW)
    GPIO.output(18,GPIO.HIGH)
    print ("Slow Down")
    time.sleep(3)
GPIO.output(18,GPIO.LOW)
