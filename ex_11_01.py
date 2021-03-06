'''
Exercise 1: Write a simple program to simulate the operation of the grep command on Unix.
#sk the user to enter a regular expression and count the number of lines that matched the regular expression:

   $ python grep.py
   Enter a regular expression: ^Author
   mbox.txt had 1798 lines that matched ^Author

   $ python grep.py
   Enter a regular expression: ^X-
   mbox.txt had 14368 lines that matched ^X-

   $ python grep.py
   Enter a regular expression: java$
   mbox.txt had 4175 lines that matched java$
'''

import re

fhand = open('mbox.txt')
grep = input('Enter a regular expression: ')

count = 0
for line in fhand :
    x = re.findall(grep, line)
    if len(x) < 1 :
        continue
    count = count + 1

print('mbox.txt had',count,'lines that matched',grep)
