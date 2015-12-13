import sqlite3

with sqlite3.connect("new.db") as connection:
    cursor = connection.cursor()

    cities = [
               ('Boston', 'MA', 600000),
               ('Los Angeles', 'CA', 38000000),
               ('Houston', 'TX', 2100000),
               ('Philadelphia', 'PA', 1500000),
               ('San Antonio', 'TX', 1400000),
               ('San Diego', 'CA', 130000),
               ('Dallas', 'TX', 1200000),
               ('San Jose', 'CA', 900000),
               ('Jacksonville', 'FL', 800000),
               ('Indianapolis', 'IN', 800000),
               ('Austin', 'TX', 800000),
               ('Detroit', 'MI', 700000)
             ]
    cursor.executemany("INSERT INTO population VALUES(?,?,?)", cities)
    cursor.execute("SELECT * FROM population WHERE population > 1000000")
    rows = cursor.fetchall()

    for r in rows:
        print r[0], r[1], r[2]

    cursor.execute("""CREATE TABLE regions (city TEXT, region TEXT)""")
    cities = [
               ('New York City', 'Northeast'),
               ('San Francisco', 'West'),
               ('Chicago', 'Midwest'),
               ('Houston', 'South'),
               ('Phoenix', 'West'),
               ('Boston', 'Northeast'),
               ('Los Angeles', 'West'),
               ('Houston', 'South'),
               ('Philadelphia', 'Northeast'),
               ('San Antonio', 'South'),
               ('San Diego', 'West'),
               ('Dallas', 'South'),
               ('San Jose', 'West'),
               ('Jacksonville', 'South'),
               ('Indianapolis', 'Midwest'),
               ('Austin', 'South'),
               ('Detroit', 'Midwest')
             ]

    cursor.executemany("INSERT INTO regions VALUES(?,?)", cities)
    cursor.execute("SELECT * FROM regions ORDER BY region ASC")
    rows = cursor.fetchall()

        