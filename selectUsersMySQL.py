import mysql.connector
from mysql.connector import Error

try:
	connection = mysql.connector.connect(host='40.115.18.125',database='EPL428', user='admin', password='Pass1234!')

	sqlSelectQuery= "select * from Test"
	cursor = connection.cursor()
	cursor.execute(sqlSelectQuery)
	records = cursor.fetchall()
	print("Total number of rows in Users is: " + str(cursor.rowcount));

	print("Printing each user record:\n")
	for row in records:
		print "ID: " + str(row[0])
		print "First Name: " + str(row[1])
		print "Last Name: " + str(row[2])

except Error as e:
	print("Error reading data from MySQL table",e)

finally:
	if (connection.is_connected()):
		connection.close()
		cursor.close()
		print("\nMySQL connection is closed")
