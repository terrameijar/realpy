import sqlite3

with sqlite3.connect("new.db") as connection:
    cursor = connection.cursor()

    cursor.execute("""SELECT DISTINCT population.city,
        population.population,
                 regions.region FROM population, regions WHERE
                 population.city = regions.city ORDER BY 
                     population.city ASC """)
    rows = cursor.fetchall()

    for r in rows:
        print "City:       " + r[0]
        print "Population: " + str(r[1])
        print "Region:     " + r[2] + "\n"