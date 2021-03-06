'''
Write a program which prompts the user for a Celsius temperature,
convert the temperature to Fahrenheit, and print out the converted temperature.
'''

ctemp = input('Enter Celsius temperature: ')
ctemp = float(ctemp)
ftemp = ctemp * 1.8 + 32
print('Farenheit temp:',ftemp)
