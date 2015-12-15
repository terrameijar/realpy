# build database

import sqlite3
import random

# step 1 create database
# step 2: create table
# step 3: create random sequence
# insert sequence into table
# close

with sqlite3.connect("newnum.db") as connection:
    cursor = connection.cursor()

    cursor.execute("DROP TABLE if exists numbers")
    cursor.execute("CREATE TABLE numbers(num INT)")

    random_numbers = []
    for number in range(0,101):
        #random_numbers.append(random.randint(0,101))
        cursor.execute("INSERT INTO numbers VALUES(?)", (random.randint(0,100),))