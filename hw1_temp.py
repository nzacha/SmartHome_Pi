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

    sqlSelectQuery = "INSERT INTO Data(Temperature,Humidity) VALUES (%s,%s)"
    cursor = connection.cursor()

    while True:
        humid, temper = Adafruit_DHT.read_retry(DHTSensor, GPIO_Pin)
        args = (temper, humid)
        cursor.execute(sqlSelectQuery, args)
        cursor.execute(sqlSelectQuery)
        time.sleep(5)

except Error as error:
        print(error)

finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()