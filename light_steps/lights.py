import RPi.GPIO as GPIO
import time

# GPIO-configuration
GPIO.setmode(GPIO.BCM)
# led-configuration
led = 7
GPIO.setup(led,GPIO.OUT)

# Functions - shortcuts
def long():
    # blink LONG
    # lights ON
    GPIO.output(led,1)
    # pause
    time.sleep(0.3)
    # lights OFF
    GPIO.output(led,0)

def short():
    # blink SHORT
    # lights ON
    GPIO.output(led,1)
    # pause
    time.sleep(0.3)
    # lights OFF
    GPIO.output(led,0)

for i in range(3):
    short()

for i in range(3):
    # blink LONG
    # lights ON
    GPIO.output(led,1)
    # pause
    time.sleep(1)
    # lights OFF
    GPIO.output(led,0)

for i in range(3):
    # blink SHORT
    # lights ON
    GPIO.output(led,1)
    # pause
    time.sleep(0.3)
    # lights OFF
    GPIO.output(led,0)

GPIO.cleanup()
