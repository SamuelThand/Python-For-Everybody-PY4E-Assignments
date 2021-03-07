'''
Write another program that prompts for a list of numbers as above and at the end
prints out both the maximum and minimum of the numbers instead of the average.
'''

maximum=None
minimum=None
count = 0
total = 0.0

while True:
    num = input('Enter a number: ')
    if num == 'done' : break
    else:
        try:
            fnum = float(num)
        except:
            print('Error, only enter numbers')
            continue
    count = count + 1
    total = total + fnum
    if maximum is None : maximum = fnum
    elif fnum > maximum : maximum = fnum
    if minimum is None : minimum = fnum
    elif minimum > fnum : minimum = fnum

print('Total:',total,'Count:',count,'Maximum:',maximum,'Minimum:',minimum)
