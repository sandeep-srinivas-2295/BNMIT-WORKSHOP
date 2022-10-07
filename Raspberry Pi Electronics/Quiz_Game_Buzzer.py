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
Button1 = 23
Button2 = 17
GPIO.setup(14,GPIO.OUT)
GPIO.setup(Button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        input_state1 = GPIO.input(Button1)
        input_state2 = GPIO.input(Button2)
        state = " "
        if input_state1 == 0 or input_state2 == 0:
            if input_state1 == 0:
                state = "Player 1"
                print(state)
            elif input_state2 == 0:
                state = "Player 2"
                print(state)
            GPIO.output(14,GPIO.HIGH)
            time.sleep(0.2)
        else:
            GPIO.output(14,GPIO.LOW)
            time.sleep(0.2)

except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()
