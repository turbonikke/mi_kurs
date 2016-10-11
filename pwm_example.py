## To create a PWM instance:
#
#p = GPIO.PWM(channel, frequency)
#
## To start PWM:
#
#p.start(dc)   # where dc is the duty cycle (0.0 <= dc <= 100.0)
#
## To change the frequency:
#
#p.ChangeFrequency(freq)   # where freq is the new frequency in Hz
#
## To change the duty cycle:
#
#p.ChangeDutyCycle(dc)  # where 0.0 <= dc <= 100.0
#
## To stop PWM:
#
#p.stop()
#
#Note that PWM will also stop if the instance variable 'p' goes out of scope.
#
#An example to blink an LED once every two seconds:

def main():
    #blink(7)
    fade(7)

def blink(pin):
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    
    p = GPIO.PWM(pin, 0.5)
    p.start(1)
    input('Press return to stop:')   # use raw_input for Python 2
    p.stop()
    GPIO.cleanup()

# An example to brighten/dim an LED:

def fade(pin):
    import time
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    
    p = GPIO.PWM(pin, 50)  # channel=12 frequency=50Hz
    p.start(0)
    try:
        while True:
            for dc in range(0, 101, 5):
                p.ChangeDutyCycle(dc)
                time.sleep(0.1)
            for dc in range(100, -1, -5):
                p.ChangeDutyCycle(dc)
                time.sleep(0.1)
    except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()

main()
