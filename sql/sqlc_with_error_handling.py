import csv
import sqlite3

connection = sqlite3.connect("new.db")

cursor = connection.cursor()

try:
    cursor.execute("INSERT INTO populations VALUES('New York City', 'NY', 8200000)")
    cursor.execute("INSERT INTO populations VALUES ('San Fran', 'CA', 800000)")
    connection.commit()
except sqlite3.OperationalError, error_msg:
    print "uh oh.. Something has gone wrong. Try again. . .Error: \n", error_msg

connection.close()        