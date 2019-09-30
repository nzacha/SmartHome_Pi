#YELLOW(GREEN), RED, GND
import RPi.GPIO as GPIO
import time

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)

LED_RED=17
LED_GREEN=4
GPIO.setup(LED_RED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_GREEN, GPIO.OUT, initial=GPIO.LOW)

print "LED-Test [press ctrl+c to end]"


try:
	while True:
		print("LED Red is on for 2 seconds")
		GPIO.output(LED_RED, GPIO.HIGH)
		GPIO.output(LED_GREEN, GPIO.LOW)
		time.sleep(2)
		print("LED GREEN is on for 3 seconds")
		GPIO.output(LED_RED, GPIO.LOW)
		GPIO.output(LED_GREEN, GPIO.HIGH)
		time.sleep(3)

except KeyboardInterrupt:
	GPIO.cleanup()