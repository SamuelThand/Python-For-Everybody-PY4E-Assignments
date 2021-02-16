#   Assignment
#
#   Write a program to prompt the user for
#   hours and rate per hour to compute gross pay.

#   Solution

hours = input('Enter worked hours: ')
pay = input('Enter hourly pay: ')

try:
    print('Gross pay: ',float(pay)*float(hours))
except:
    print('Error, bad input')
    quit()
