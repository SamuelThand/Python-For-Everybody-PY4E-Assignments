'''
Rewrite your pay program using try and except so that your program handles non-numeric input gracefully
by printing a message and exiting the program. The following shows two executions of the program:

    Enter Hours: 20
    Enter Rate: nine
    Error, please enter numeric input
    Enter Hours: forty
    Error, please enter numeric input
'''

shours = input('Enter worked hours: ')

try:
    fhours = float(shours)
except:
    print('Error, please enter numeric input')
    quit()

srate = input('Enter hourly pay: ')

try:
    frate = float(srate)
except:
    print('Error, please enter numeric input')
    quit()

regpay = fhours*frate

if fhours > 40 :
    print('You have worked overtime and earned: ')
    regpay = fhours * frate
    otpay = (fhours - 40) * (frate*0.5)
    print(regpay+otpay)
else:
    print('You have earned: ')
    print(regpay)
