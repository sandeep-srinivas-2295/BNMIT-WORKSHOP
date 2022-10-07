"""
Connect the Button1 one end to GPIO23
Connect the Button1 other end to GND
Connect the Button2 one end to GPIO17
Connect the Button2 other end to GND
Connect the Buzzer Anode to GPIO14
Connect the Buzzer Ground to GND
"""

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()
a=14
b=15
c=18
d=23
e=24
f=25
g=8
dp=4
IR=2
GPIO.setup(IR,GPIO.IN)
GPIO.setup(a,GPIO.OUT)#a
GPIO.setup(b,GPIO.OUT)#b
GPIO.setup(c,GPIO.OUT)#c
GPIO.setup(d,GPIO.OUT)#d
GPIO.setup(e,GPIO.OUT)#e
GPIO.setup(f,GPIO.OUT)#f
GPIO.setup(g,GPIO.OUT)#g
GPIO.setup(dp,GPIO.OUT)#dp

# Put all the leds to off state
def OFF():
    GPIO.output(a,0)#a
    GPIO.output(b,0)#b
    GPIO.output(c,0)#c
    GPIO.output(d,0)#d
    GPIO.output(e,0)#e
    GPIO.output(f,0)#f
    GPIO.output(g,0)#g
    GPIO.output(dp,0)#dp

#define the function to display numbers
def zero():
    OFF()
    GPIO.output(a,1)
    GPIO.output(b,1)
    GPIO.output(c,1)
    GPIO.output(d,1)
    GPIO.output(e,1)
    GPIO.output(f,1)


def one():
    OFF()
    GPIO.output(b,1)
    GPIO.output(c,1)


def two():
    OFF()
    GPIO.output(a,1)
    GPIO.output(b,1)
    GPIO.output(g,1)
    GPIO.output(e,1)
    GPIO.output(d,1)


def three():
    OFF()
    GPIO.output(a,1)
    GPIO.output(b,1)
    GPIO.output(c,1)
    GPIO.output(d,1)
    GPIO.output(g,1)


def four():
    OFF()
    GPIO.output(b,1)
    GPIO.output(c,1)
    GPIO.output(f,1)
    GPIO.output(g,1)


def five():
    OFF()
    GPIO.output(a,1)
    GPIO.output(c,1)
    GPIO.output(d,1)
    GPIO.output(f,1)
    GPIO.output(g,1)


def six():
    OFF()
    GPIO.output(e,1)
    GPIO.output(a,1)
    GPIO.output(c,1)
    GPIO.output(d,1)
    GPIO.output(f,1)
    GPIO.output(g,1)


def seven():
    OFF()
    GPIO.output(a,1)
    GPIO.output(b,1)
    GPIO.output(c,1)


def eight():
    OFF()
    GPIO.output(a,1)
    GPIO.output(b,1)
    GPIO.output(c,1)
    GPIO.output(d,1)
    GPIO.output(e,1)
    GPIO.output(f,1)
    GPIO.output(g,1)


def nine():
    OFF()
    GPIO.output(a,1)
    GPIO.output(b,1)
    GPIO.output(c,1)
    GPIO.output(d,1)
    GPIO.output(f,1)
    GPIO.output(g,1)

count = 0
while True:
    
    if GPIO.input(IR) == 0:
        print("IR detected")
        count = count + 1
        print(count)
        time.sleep(0.5)
        if count==1:
            one()
        elif count==2:
            two()
        elif count==3:
            three()
        elif count==4:
            four()
        elif count==5:
            five()
        elif count==6:
            six()
        elif count==7:
            seven()
        elif count==8:
            eight()
        elif count==9:
            nine()
        else:
            OFF()
    else:
        print("IR not detected")
        time.sleep(0.5)
