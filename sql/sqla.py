#SQLite3 database and table

import sqlite3

#new database if the database doesn't already exist
conn = sqlite3.connect("new.db")

#cursor object to execute SQL commands
cursor = conn.cursor()

#create table
cursor.execute("""CREATE TABLE population
	              (city TEXT, state TEXT, population INT)
	              """)

# close database connection
conn.close()