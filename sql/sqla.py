#SQLite3 database and table

import sqlite3

#new database if the database doesn't already exist
conn = sqlite3.connect("new.db")
carsconn = sqlite3.connect("cars.db")


#cursor object to execute SQL commands
cursor = conn.cursor()
cars_cursor = carsconn.cursor()
#create table
cursor.execute("""CREATE TABLE population
	              (city TEXT, state TEXT, population INT)
	              """)

cars_cursor.execute(""" CREATE TABLE inventory
	                  (Make TEXT, Model TEXT, Quantity INT)
	                  """)

# close database connection
conn.close()
carsconn.close()