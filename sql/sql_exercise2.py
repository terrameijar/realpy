import sqlite3

with sqlite3.connect("cars.db") as connection:
    cursor = connection.cursor()
    cursor.execute("UPDATE inventory SET Quantity = 19 WHERE Model = 'Ranger'")
    cursor.execute("UPDATE inventory SET Quantity = 35 WHERE Model = 'CRV'")

    cursor.execute("SELECT * FROM inventory")
    rows = cursor.fetchall()

    for r in rows:
        print r[0], r[1], r[2]