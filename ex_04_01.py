# Assignment
#
#   Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
#   Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours.
#   Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation.
#   The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
#   You should use input to read a string and float() to convert the string to a number.
#   Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly.
#   Do not name your variable sum or use the sum() function.
#
#   Solution

def computepay (hours, rate) :
    regpay = hours * rate
    otpay = (hours - 40) * (rate*0.5)
    if hours > 40 :
        return regpay+otpay
    else:
        return regpay

shours = input('Enter worked hours: ')
try:
    fhours = float(shours)
except:
    print('Error, enter numeric input.')
    quit()

srate = input('Enter hourly pay: ')
try:
    frate = float(srate)
except:
    print('Error, enter numeric input.')
    quit()

totpay = computepay(fhours,frate)

print('Total pay: ', totpay)
