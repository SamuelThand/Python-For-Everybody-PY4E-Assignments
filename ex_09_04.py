'''
This program records the domain name (instead of the address) where the
message was sent from instead of who the mail came from (i.e., the whole email address).
At the end of the program, print out the contents of your dictionary.

   python schoolcount.py
   Enter a file name: mbox-short.txt
   {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
   'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
'''

name = input('Enter file name: ')
if len(name) < 1 : name = 'mbox-short.txt'
fhand = open(name)

doms = dict()
for line in fhand :
    if 'From ' not in line :
        continue
    words = line.split()
    email = words[1].split('@')
    domain = email[1]
    doms[domain] = doms.get(domain,0) + 1

print(doms)
