#instructions:

#insert 5 records into the table. make sure three of the vehicles are fords while the other two are Hondas

import sqlite3

with sqlite3.connect("cars.db") as connection:
    cursor = connection.cursor()
    cars = [('Ford', 'Ranger', 20),
            ('Ford','Focus', 200),
            ('Ford', 'Fiesta', 50),
            ('Honda', 'CRV', 36),
            ('Honda', 'Fit', 27)
           ]

    cursor.executemany('INSERT INTO inventory VALUES(?,?,?)', cars)
   