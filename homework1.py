#button: SIG, 5V, GND
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO_BUT = 4
GPIO_BUZ = 17
print "KY-004 Module Test (Ctrl-C to exit)"
GPIO.setup(GPIO_BUT, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(GPIO_BUZ, GPIO.OUT)

pwm = GPIO.PWM(GPIO_BUZ, 500)

try:
	while True:
		currState = GPIO.input(GPIO_BUT) 
		if currState == False:
			print("The button was pressed, it will be unavailable for 10 seconds")

			print("Emitting sound...")
			pwm.start(50)			
			time.sleep(0.5)
			pwm.stop()

			pwm.ChangeFrequency(300)		
			pwm.start(50)
			time.sleep(0.5)
			pwm.stop()


			pwm.ChangeFrequency(500)
			pwm.start(20)			
			time.sleep(1)
			pwm.stop()

			time.sleep(3)
			print("Button is available")

except KeyboardInterrupt:
	GPIO.cleanup()
