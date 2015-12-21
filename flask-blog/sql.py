# blog app database

import sqlite3

with sqlite3.connect("blog.db") as connection:
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE posts(title TEXT, post TEXT)""")

    #insert dummy data into the TABLE
    cursor.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
    cursor.execute('INSERT INTO posts VALUES("Well", "I\'m well.")')
    cursor.execute('INSERT INTO posts VALUES("Excellent", "I\'m Excellent")')
    cursor.execute('INSERT INTO posts VALUES("Okay", "I\'m Okay")')