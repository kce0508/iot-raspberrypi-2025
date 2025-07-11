#pip install adafruit-circuitpython-dht
#sudo apt install libgpiod2

import RPi.GPIO as GPIO
import time
import adafruit_dht
import board
import mysql.connector

dhtPin = 23

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)

dht = adafruit_dht.DHT11(board.D23)

DB = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "12345",
	database = "test",
	autocommit = True
)

cursor = DB.cursor()

while True:
	try:
		temperature = dht.temperature
		humidity = dht.humidity
		print("Temp: ", temperature)
		print("Humi: ", humidity)
		time.sleep(1)

		cursor.execute(
			"INSERT INTO dht_log (temperature, humidity) VALUES (%s, %s)",
			(temperature, humidity)
		)

	except RuntimeError as error:
		print(error.args[0])

	except KeyboardInterrupt:
		GPIO.cleanup()
		break

dhtPin.exit()
