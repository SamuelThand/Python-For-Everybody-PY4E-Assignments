'''
Exercise 1: Change the socket program socket1.py to prompt the user for the URL so it can read any web page.
you can use split('/') to break the URL into its component parts so you can extract the host name for the socket connect call.
Add error checking using try and except to handle the condition where the user enters an improperly formatted or non-existent URL.
'''

import socket

website = input('Enter URL: ')
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

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
