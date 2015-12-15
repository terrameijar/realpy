import sqlite3

with sqlite3.connect("new.db") as connection:
    cursor = connection.cursor()
# create a dictionary of sql queries
    sql = { 'average': "SELECT avg(population) FROM population",
            'maximum': "SELECT max(population) FROM population",
            'minimum': "SELECT min(population) FROM population",
            'sum': "SELECT sum(population) FROM population",
            'count': "SELECT count(city) FROM population"}
    # run each sql query in the dictionary
    for keys, values in sql.iteritems():
        cursor.execute(values)

        # fetch one record
        result = cursor.fetchone()

        # output the result to the screen
        print keys + ":", result[0]