import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pin2 = 8

GPIO.setup(pin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(pin2)
    if input_state == False:
        print('Button Pressed')
        time.sleep(0.2)
