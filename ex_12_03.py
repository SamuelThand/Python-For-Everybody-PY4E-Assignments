#Assignment
#
#Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving the document from a URL,
#(2) displaying up to 3000 characters, and (3) counting the overall number of characters in the document.
#Don’t worry about the headers for this exercise, simply show the first 3000 characters
#of the document contents.import urllib.request, urllib.parse, urllib.error
#
#Assignment

import urllib.request, urllib.parse, urllib.error

website = input('Enter URL: ')
if len(website) < 1 : website = 'http://data.pr4e.org'

try:
    fhand = urllib.request.urlopen(website)
except:
    print('Bad URL format, please enter URL with format "http://xxxx.xxxx.xxx"')
    quit()

charcount = 0
for line in fhand:
    charcount = charcount + len(line)
    if charcount < 3000 : print(line.decode().strip())

print('Character count of document:',charcount)
