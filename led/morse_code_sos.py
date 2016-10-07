import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
# Alphabet
pin = 7
GPIO.setup(pin,GPIO.OUT)


CODE = {' ': ' ', 
        "'": '.----.', 
        '(': '-.--.-', 
        ')': '-.--.-', 
        ',': '--..--', 
        '-': '-....-', 
        '.': '.-.-.-', 
        '/': '-..-.', 
        '0': '-----', 
        '1': '.----', 
        '2': '..---', 
        '3': '...--', 
        '4': '....-', 
        '5': '.....', 
        '6': '-....', 
        '7': '--...', 
        '8': '---..', 
        '9': '----.', 
        ':': '---...', 
        ';': '-.-.-.', 
        '?': '..--..', 
        'A': '.-', 
        'B': '-...', 
        'C': '-.-.', 
        'D': '-..', 
        'E': '.', 
        'F': '..-.', 
        'G': '--.', 
        'H': '....', 
        'I': '..', 
        'J': '.---', 
        'K': '-.-', 
        'L': '.-..', 
        'M': '--', 
        'N': '-.', 
        'O': '---', 
        'P': '.--.', 
        'Q': '--.-', 
        'R': '.-.', 
        'S': '...', 
        'T': '-', 
        'U': '..-', 
        'V': '...-', 
        'W': '.--', 
        'X': '-..-', 
        'Y': '-.--', 
        'Z': '--..', 
        '_': '..--.-'}


message = 'SOS'
# message = message.upper()

GPIO.setmode(GPIO.BCM)
pin2 = 8

GPIO.setup(pin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(pin2)
    if input_state == False:
	for letter in message:
		print letter
		string = CODE[letter]
		for letter2 in string:
			if letter2 == '-':
				time.sleep(0.2)
				GPIO.output(pin,GPIO.HIGH)
				time.sleep(0.6)
				GPIO.output(pin,GPIO.LOW)
			if letter2 == '.':
				time.sleep(0.2)
				GPIO.output(pin,GPIO.HIGH)
				time.sleep(0.1)
				GPIO.output(pin,GPIO.LOW)
			if letter2 == ' ':
				time.sleep(0.2)
		time.sleep(0.6)
GPIO.cleanup()

