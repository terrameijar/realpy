import sys
import sqlite3

def f_average():
    print "\nYou selected the Average Function"
    #average = {'average': "SELECT DISTINCT AVG(model,order_date) FROM orders"}
    average = "SELECT AVG(num) FROM numbers"
    cursor.execute(average)
    result = cursor.fetchone()
    print result[0]
    return

def f_sum():
    print "\nYou selected 2"
    total = "SELECT SUM(num) FROM numbers"
    cursor.execute(total)
    result = cursor.fetchone()
    print "The Sum of all the numbers is: ", str(result[0])

def f_maximum():
    print "\nYou selected Three"
    maximum = "SELECT MAX(num) FROM numbers"
    cursor.execute(maximum)
    result = cursor.fetchone()
    print "The biggest number in the database is: ", str(result[0])

def f_minimum():
    print "\nYou Choice 4"
    minimum = "SELECT MIN(num) FROM numbers"
    cursor.execute(minimum)
    result = cursor.fetchone()
    print "The smallest number in the database is: ", result[0]

def f_exit():
    print "\nGoodbye"
    sys.exit()

with sqlite3.connect("newnum.db") as connection:
    cursor = connection.cursor()

    #prompt the user about what they want to do: AVG, SUM, MAX, MIN or EXIT
    choice = 0
    while choice !=5:
        choice = int(raw_input("""\n\nFunctions\n================\n1:Average \n2:Sum\n3:Maximum \n4:Minimum \n5:Exit\nChoice::__"""))

        if choice == 1:
            f_average()
        elif choice == 2:
            f_sum()
        elif choice == 3:
            f_maximum()
        elif choice == 4:
            f_minimum()
        elif choice == 5:
            f_exit()

        else:
            print "\n\n++++++++Please enter a valid option++++++++"
            print "Let's try this again: "


