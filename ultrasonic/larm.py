import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 7
ECHO = 8
led = 11

# Skillnad mellan 
dev = 10

print("Distance Measurement In Progress")
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(led,GPIO.OUT)

GPIO.setup(led,0)

GPIO.output(TRIG, 0)
print("Waiting For Sensor To Settle")
time.sleep(2)

# Medeltal
a = []
for i in range(30):
	# Send signal
	GPIO.output(TRIG, 1)
	time.sleep(0.00001)
	GPIO.output(TRIG, 0)
	
	# Wait for return echo
	while GPIO.input(ECHO)==0:
		pulse_start = time.time()
	while GPIO.input(ECHO)==1:
		pulse_end = time.time()
	
	# Calculation of distance
	pulse_duration = pulse_end - pulse_start
	distance = pulse_duration * 17150
	distance = round(distance, 2)
	print("Distance: %6.2f cm" % distance)
	a.append(distance)
mean = sum(a) / len(a)
print(mean)
time.sleep(2)

print("\n mean value distance %6.2f cm" % mean)

try: 
	while(True):
		# Send signal
		GPIO.output(TRIG, 1)
		time.sleep(0.00001)
		GPIO.output(TRIG, 0)
		
		# Wait for return echo
		while GPIO.input(ECHO)==0:
			pulse_start = time.time()
		while GPIO.input(ECHO)==1:
			pulse_end = time.time()
		
		# Calculation of distance
		pulse_duration = pulse_end - pulse_start
		distance = pulse_duration * 17150
		distance = round(distance, 2)
		diff = abs(distance - mean)
		print("Distance: %6.2f cm, diff %6.2f" % (distance,diff))

		# Light a warning light
		if diff >= dev:
			GPIO.output(led,1)
		else:
			GPIO.output(led,0)
except KeyboardInterrupt:
	GPIO.cleanup()
