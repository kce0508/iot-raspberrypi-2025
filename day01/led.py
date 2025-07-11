import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)				# BCM mode 설정

RED = 14							# LED pin 설정
GREEN = 18
BLUE = 15

GPIO.setup(RED, GPIO.OUT)			# pin mode 설정
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

for i in range(3):					# 1초마다 RGB 반복(3번만)
	GPIO.output(RED, GPIO.LOW)		# 출력값 설정
	GPIO.output(GREEN, GPIO.HIGH)
	GPIO.output(BLUE, GPIO.HIGH)
	time.sleep(1)

	GPIO.output(RED, GPIO.HIGH)
	GPIO.output(GREEN, GPIO.LOW)
	GPIO.output(BLUE, GPIO.HIGH)
	time.sleep(1)

	GPIO.output(RED, GPIO.HIGH)
	GPIO.output(GREEN, GPIO.HIGH)
	GPIO.output(BLUE, GPIO.LOW)
	time.sleep(1)

GPIO.cleanup()
