#SQLite3 database and table

import sqlite3

#new database if the database doesn't already exist
#conn = sqlite3.connect("new.db")

with sqlite3.connect("new2.db") as connection:
	c = connection.cursor()
	c.execute(""" CREATE TABLE population
		        (city TEXT, state TEXT, population INT)""")
	#c.execute("INSERT INTO population VALUES('New York City', 'NY', 8200000)")
	#c.execute("INSERT INTO population VALUES('San Francisco', 'CA', 800000)")

	# inserting multiple records using a tuple
	cities = [
	        ('Boston', 'MA', 600000),
	        ('Chicago','IL', 27000000),
	        ('Houston', 'TX', 2100000),
	        ('Phoenix', 'AZ', 1500000)
	        ]

	#insert into table
	c.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)


