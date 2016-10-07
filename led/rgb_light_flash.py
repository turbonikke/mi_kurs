import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
# Light connected GPIO:s
RGB = [7,8,11]
for pin in RGB:
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,0)

for pin in RGB:
	for value in [0,1,0]:
		print("GPIO %d val %d" % (pin,value))
		GPIO.output(pin,value)
		time.sleep(1)
	
GPIO.cleanup()
