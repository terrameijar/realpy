import sqlite3

with sqlite3.connect("newest.db") as connection:
    cursor = connection.cursor()
    
    cursor.execute("SELECT firstname, lastname from employees")
    rows = cursor.fetchall()

    for row in rows:
        print row[0],row[1]