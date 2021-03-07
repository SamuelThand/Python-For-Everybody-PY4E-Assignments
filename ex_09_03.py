'''
Add code to the above program to figure out who has the most messages in the file.
After all the data has been read and the dictionary has been created, look
through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops)
to find who has the most messages and print how many messages the person has.

   Enter a file name: mbox-short.txt
   cwen@iupui.edu 5

   Enter a file name: mbox.txt
   zqian@umich.edu 195
'''

name = input('Enter file name: ')
if len(name) < 1 : name = 'mbox-short.txt'
fhand = open(name)

emails = dict()
for line in fhand :
    if 'From ' not in line :
        continue
    words = line.split()
    for word in words[1:2] :
        emails[word] = emails.get(word,0) + 1

bigcount = None
bigadress = None
for adress,count in emails.items() :
    if bigcount is None or bigcount < count :
        bigcount = count
        bigadress = adress

print('Most active mail user:',bigadress,'For a number of:',bigcount)
