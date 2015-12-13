#ford rander 19
#ford focus  200
#ford fiesta 50

#honda crv 35
# honda fit 27

import sqlite3

with sqlite3.connect("cars.db") as connection:
    cursor = connection.cursor()

    #cursor.execute("CREATE TABLE orders (make TEXT, model TEXT, order_date DATE )")

    cars = [
             ("Ford", "Ranger", "2015-01-30"),
             ("Ford", "Ranger", "2015-09-07"),
             ("Ford", "Ranger", "2015-06-22"),
             ("Ford", "Focus", "2015-11-13"),
             ("Ford", "Focus", "2015-12-05"),
             ("Ford", "Focus", "2015-12-12"),
             ("Ford", "Fiesta", "2015-02-28"),
             ("Ford", "Fiesta", "2015-03-09"),
             ("Ford", "Fiesta", "2015-04-06"),
             ("Honda", "CRV", "2015-05-30"),
             ("Honda", "CRV", "2015-07-30"),
             ("Honda", "CRV", "2015-08-30"),
             ("Honda", "Fit", "2015-10-30"),
             ("Honda", "Fit", "2015-11-30"),
             ("Honda", "Fit", "2015-01-24")
           ]

    cursor.executemany("INSERT INTO orders VALUES(?,?,?)", cars)
    cursor.execute(""" SELECT DISTINCT inventory.Make, inventory.Model, inventory.Quantity,
                    orders.order_date FROM inventory, orders WHERE inventory.Model = orders.model""")
    rows = cursor.fetchall()

    for row in rows:
        print "Make: " + row[0] + " " + row[1]
        print "Quantity: " + str(row[2])
        print "Order Date: " + row[3] + "\n"