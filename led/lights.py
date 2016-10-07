import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# Setup and stuff
red = 8
green = 7
green2 = 11
#r1 = 11
GPIO.setup(red,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)
GPIO.setup(green2,GPIO.OUT)

# set lights to flash 30 times
for x in range(0,50):
	GPIO.output(red,GPIO.HIGH)
	GPIO.output(green,GPIO.LOW)
	GPIO.output(green2,GPIO.LOW)
	time.sleep(0.05)
	GPIO.output(red,GPIO.LOW)
	GPIO.output(green,GPIO.HIGH)
	GPIO.output(green2,GPIO.LOW)
	time.sleep(0.05)
	GPIO.output(red,GPIO.LOW)
	GPIO.output(green,GPIO.LOW)
	GPIO.output(green2,GPIO.HIGH)
	time.sleep(0.05)
GPIO.cleanup()

# Probing for output led

GPIO = [2,3,4,7,8,9,10,11,14,15,17,18,22,23,24,25]
# setup all GPIO:s
for pin in board:
	GPIO.setup(pin,GPIO.OUT)
	print("\nGPIO %d\n" % pin)
	GPIO.output(pin,GPIO.HIGH)
	GPIO.output(pin,GPIO.LOW)
	time.sleep(1)
