#button: SIG, 5V, GND
import RPi.GPIO as GPIO
import time
import mysql.connector
import face_recognition
import os
from mysql.connector import Error

def write_file(data, filename):
	with open(filename, 'wb') as file:
		file.write(data)


def readBLOB():
	# initialize known picture encodings
	picture_of_me = face_recognition.load_image_file("known_people/Nicolas_Zachariou.jpg")
	my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

	# fetch latest image from db
	print("Reading BLOB data from Images table")
	try:
		connection = mysql.connector.connect(host='40.115.18.125', database='EPL428', user='admin',
											 password='Pass1234!', raw=True)

		sqlSelectQuery = "select image from Images ORDER BY ID DESC LIMIT 1"
		cursor = connection.cursor()
		cursor.execute(sqlSelectQuery)
		records = cursor.fetchone()

		image = records[0]
		write_file(image, "temp.jpg")

		# initialize unknown picture encoding

		unknown_picture = face_recognition.load_image_file("temp.jpg")
		unknown_face_encodings = face_recognition.face_encodings(unknown_picture)

		unknown_face_encoding = None
		if len(unknown_face_encodings) > 0:
			unknown_face_encoding = unknown_face_encodings[0]
		else:
			print("No faces recognized")

		# compare face encodings
		if unknown_face_encodings:
			results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

			if results[0] == True:
				print("Access Granted!")
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
			else:
				print("Access Denied!")
		else:
			print("Access Denied!")

	except Error as e:
		print("Error reading data from MySQL table", e)

	finally:
		if (connection.is_connected()):
			connection.close()
			cursor.close()
		# print("MySQL connection is closed")
		os.remove("temp.jpg")

GPIO.setmode(GPIO.BCM)
GPIO_BUT = 4
GPIO_BUZ = 17
print("KY-004 Module Test (Ctrl-C to exit)")
GPIO.setup(GPIO_BUT, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(GPIO_BUZ, GPIO.OUT)

pwm = GPIO.PWM(GPIO_BUZ, 500)

try:
	while True:
		currState = GPIO.input(GPIO_BUT) 
		if currState == False:
			print("The button was pressed, it will be unavailable for 10 seconds")
			readBLOB()

			time.sleep(3)
			print("Button is available")

except KeyboardInterrupt:
	GPIO.cleanup()
