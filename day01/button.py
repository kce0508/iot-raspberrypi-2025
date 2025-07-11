import RPi.GPIO as GPIO
import time

buttonPin = 17

GPIO.setmode(GPIO.BCM)

# pull_up_down = GPIO.PUD_up 내부풀업풀다운설정
GPIO.setup(buttonPin, GPIO.IN)

try:
	while True:
		if(GPIO.input(buttonPin)):
			print("button released")
		else:
			print("button pressed")
		time.sleep(0.5)
except KeyboardInterrupt:
	GPIO.cleanup()
