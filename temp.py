#SIG, 5v, GND
import RPi.GPIO as GPIO
import Adafruit_DHT
import time

DHTSensor = Adafruit_DHT.DHT11

GPIO_Pin = 4

while True:
	humid, temper = Adafruit_DHT.read_retry(DHTSensor, GPIO_Pin)
	if temper is None:
		print "Temperature sensor failure"
 	else:
		rint("Temperature:" + str(temper))
	if humid is None:
		print "Humidity sensor failure"
	else:
		print("Humidity:" + str(humid))
	time.sleep(3)