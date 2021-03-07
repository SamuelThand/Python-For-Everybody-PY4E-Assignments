'''
Exercise 2: Change your socket program so that it counts the number of characters it has received
and stops displaying any text after it has shown 3000 characters. The program should retrieve the entire document
and count the total number of characters and display the count of the number of characters at the end of the document.
'''

import socket

website = input('Enter URL: ')
if len(website) < 1 : website = 'http://data.pr4e.org'
hostname = website.split('/')

try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((hostname[2], 80))
except:
    print('Bad URL format, please enter URL with format "http://xxxx.xxxx.xxx"')
    quit()

cmd = 'GET ' + website + ' HTTP/1.0\r\n\r\n'
cmd = cmd.encode()
mysock.send(cmd)

charcount = 0
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    charcount = charcount + 512
    if charcount < 3000 : print(data.decode(),end='')
    
print('')
print('Character count of document:',charcount)
mysock.close()
