#   Assignment
#
#   Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

#   Solution

shours = input('Enter worked hours: ')
srate = input('Enter hourly pay: ')
fhours = float(shours)
frate = float(srate)
regpay = fhours*frate

if fhours > 40 :
    print('You have worked overtime and earned: ')
    regpay = fhours * frate
    otpay = (fhours - 40) * (frate*0.5)
    print(regpay+otpay)
else:
    print('You have earned: ')
    print(regpay)
