import sqlite3

with sqlite3.connect("new2.db") as connection:
    cursor = connection.cursor()

    cursor.execute("UPDATE population SET population = 9000000 WHERE city = 'Chicago'")

    #delete data
    cursor.execute("DELETE FROM population WHERE city='Boston'")

    print "\nNEW DATA: \n"
    cursor.execute("SELECT * FROM population")
    rows = cursor.fetchall()

    for row in rows:
        print row[0], row[1], row[2]