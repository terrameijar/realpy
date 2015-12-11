import sqlite3

with sqlite3.connect("cars.db") as connection:
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM inventory WHERE Make = 'Ford'")
    rows = cursor.fetchall()

    for row in rows:
        print row[0],row[1], row[2]