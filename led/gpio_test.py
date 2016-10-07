import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
pin = 7
GPIO.setwarnings(False)
GPIO.setup(pin,GPIO.OUT)
GPIO.output(pin,1)
time.sleep(1)
GPIO.output(pin,0)
GPIO.cleanup()
