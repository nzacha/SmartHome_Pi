#SIG, 5v, GND
import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import mysql.connector
from mysql.connector import Error

DHTSensor = Adafruit_DHT.DHT11

GPIO_Pin = 14

try:
    connection = mysql.connector.connect(host='40.115.18.125', database='EPL428', user='admin',
                                         password='Pass1234!', raw=True)

    cursor = connection.cursor()
    sqlSelectQuery = """INSERT INTO Data(Temperature,Humidity) VALUES (%s,%s)"""

    while True:
        humid, temper = Adafruit_DHT.read_retry(DHTSensor, GPIO_Pin)
	if(not((humid is None)or(temper is None))):
		args = (temper, humid)
	        cursor.execute(sqlSelectQuery, args)
		connection.commit()
	else:
		print("Temperature or Humidity value is Null")
        time.sleep(5)

except Error as error:
        print(error)

finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()