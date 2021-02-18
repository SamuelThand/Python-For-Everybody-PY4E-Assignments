#Assignment
#Write a program to read through a mail log, build a histogram using a emails
#to count how many messages have come from each email address, and print the dictionary.
#
#   Enter file name: mbox-short.txt
#   {'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
#   'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
#   'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
#   'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
#   'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
#   'ray@media.berkeley.edu': 1}
#
#Solution

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

print(emails)
