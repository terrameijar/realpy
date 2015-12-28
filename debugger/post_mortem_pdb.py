''' This script illustrates the use of post morterm debugging using pdb.pm
text below is what I did to crash the script and debug:

Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from post_mortem_pdb import *
>>> add_one_hundred()
Enter a number between 1 and 10: test
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "post_mortem_pdb.py", line 5, in add_one_hundred
    new_number = (int(number) + 100)
ValueError: invalid literal for int() with base 10: 'test'
>>> import pdb; pdb.pm()
> /home/terra/repo/realp/flask/debugger/post_mortem_pdb.py(5)add_one_hundred()
-> new_number = (int(number) + 100)
(Pdb) 
'''

def add_one_hundred():
    again = 'yes'
    while again == 'yes':
        number = raw_input('Enter a number between 1 and 10: ')
        new_number = (int(number) + 100)
        print '{} plus 100 is {}'.format(number, new_number)
        again = raw_input('Another round , my friend? (`Yes` or `no`) ')
        print "goodbye"

if __name__ == '__main__':
    add_one_hundred()