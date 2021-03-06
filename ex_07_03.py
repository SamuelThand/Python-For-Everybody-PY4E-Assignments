'''
Sometimes when programmers get bored or want to have a bit of fun, they add a harmless Easter Egg to their program.
Modify the program that prompts the user for the file name so that it prints a funny message when the user types in the exact file name “na na boo boo”.
The program should behave normally for all other files which exist and don’t exist. Here is a sample execution of the program:

    python egg.py
    Enter the file name: mbox.txt
    There were 1797 subject lines in mbox.txt

    python egg.py
    Enter the file name: missing.tyxt
    File cannot be opened: missing.tyxt

    python egg.py
    Enter the file name: na na boo boo
    NA NA BOO BOO TO YOU - You have been punk'd!
'''

fname = input('Enter the file name: ')
if len(fname) < 1 : fname = 'mbox-short.txt'
if fname == 'na na boo boo' :
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    quit()

try : fhand = open(fname)
except :
    print('Error, bad file name')
    quit()
count=0
DSPAM=0
for line in fhand :
    line=line.rstrip()
    if line.startswith("X-DSPAM-Confidence:") :
        DSPAM = DSPAM + float(line[20:])
        count = count + 1
print('Average spam confidence:', DSPAM/count)
