import sqlite3

carsconn = sqlite3.connect("cars.db")

cars_cursor = carsconn.cursor()

cars_cursor.execute(""" CREATE TABLE inventory
	                  (Make TEXT, Model TEXT, Quantity INT)
	                  """)
carsconn.close()