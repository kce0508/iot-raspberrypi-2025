import RPi.GPIO as GPIO
import time

RED = 14
GREEN = 18
BLUE = 15

buttonPin = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def led_off():
	GPIO.output(RED, GPIO.HIGH)
	GPIO.output(GREEN, GPIO.HIGH)
	GPIO.output(BLUE, GPIO.HIGH)
	print("LED OFF")

def led_red():
	GPIO.output(RED, GPIO.LOW)
	GPIO.output(GREEN, GPIO.HIGH)
	GPIO.output(BLUE, GPIO.HIGH)
	print("LED RED")

def led_green():
	GPIO.output(RED, GPIO.HIGH)
	GPIO.output(GREEN, GPIO.LOW)
	GPIO.output(BLUE, GPIO.HIGH)
	print("LED GREEN")

def led_blue():
	GPIO.output(RED, GPIO.HIGH)
	GPIO.output(GREEN, GPIO.HIGH)
	GPIO.output(BLUE, GPIO.LOW)
	print("LED BLUE")

press_count = 0
prev_input = 0
last_press_time = 0
timeout_sec = 2
action_done = False

try:
	while True:
		input_state = GPIO.input(buttonPin)
		current_time = time.time()

		if input_state == GPIO.HIGH and prev_input == GPIO.LOW:
			press_count += 1
			last_press_time = current_time
			action_done = False
			print(f"누른 횟수: {press_count}")
			time.sleep(0.05)

		if press_count > 0 and not action_done and (current_time - last_press_time > timeout_sec):
			mode = press_count

			print(f"최종 누른 횟수: {press_count} -> LED 제어시작")

			if mode == 1:
				led_off()
			elif mode == 2:
				led_red()
			elif mode == 3:
				led_green()
			elif mode == 4:
				led_blue()

			press_count = 0
			action_done = True
			
		prev_input = input_state
		time.sleep(0.01)

except KeyboardInterrupt:
	GPIO.cleanup()
			
				

