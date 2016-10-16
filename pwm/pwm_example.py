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
    fade(7,8,11)

def blink(pin):
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    
    p = GPIO.PWM(pin, 40)
    p.start(10)
    input('Press return to stop:')   # use raw_input for Python 2
    p.stop()
    GPIO.cleanup()

# An example to brighten/dim an LED:

def fade(pin,pin2,pin3):
    import time
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.setup(pin2, GPIO.OUT)
    GPIO.setup(pin3, GPIO.OUT)
    
    p = GPIO.PWM(pin, 50)  # channel=12 frequency=50Hz
    q = GPIO.PWM(pin2, 50)  # channel=12 frequency=50Hz
    r = GPIO.PWM(pin3, 50)  # channel=12 frequency=50Hz
    p.start(1)
    q.start(0)
    r.start(0)
    try:
        while True:
            # P - Q
            for dc in range(0, 101, 5):
                dci = 100 - dc
                p.ChangeDutyCycle(dci)
                q.ChangeDutyCycle(dc)
                time.sleep(0.2)
            # Q - R
            for dc in range(0, 101, 5):
                dci = 100 - dc
                q.ChangeDutyCycle(dci)
                r.ChangeDutyCycle(dc)
                time.sleep(0.2)
            # R - P
            for dc in range(0, 101, 5):
                dci = 100 - dc
                r.ChangeDutyCycle(dci)
                p.ChangeDutyCycle(dc)
                time.sleep(0.2)
    except KeyboardInterrupt:
        p.stop()
        q.stop()
        GPIO.cleanup()

main()
