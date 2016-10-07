import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
# Light connected GPIO:s
RGB = [7,8,11]
for pin in RGB:
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,1)

try:
	while(True):
		## Code continues
		request = raw_input("RGB-->")
		if (len(request) == 3):
			GPIO.output(7,int(request[0]))
			GPIO.output(8,int(request[1]))
			GPIO.output(11,int(request[2]))
except KeyboardInterrupt:
	GPIO.cleanup()
