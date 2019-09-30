#SIG, 5V, GND
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO_PIR = 4
print "KY-004 Module Test (Ctrl-C to exit)"
GPIO.setup(GPIO_PIR, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while True:
	Current_State = GPIO.input(GPIO_PIR)
	if Current_State == False:
		print("The button is being pressed")
		time.sleep(1)

GPIO.cleanup()
