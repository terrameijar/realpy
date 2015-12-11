import csv
import sqlite3

with sqlite3.connect("newest.db") as connection:
    # cursor object
    c = connection.cursor()
    employees = csv.reader(open("employees.csv", "rU"))
    # create a new table called employees

    c.execute("CREATE TABLE employees(firstname TEXT, lastname , job_title TEXT)")

    # insert data into the table
    c.executemany("INSERT INTO employees(firstname, lastname, job_title) values (?, ?, ?)", employees)