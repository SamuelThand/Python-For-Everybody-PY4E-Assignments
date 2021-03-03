#Assignment
#
#(Advanced) Change the socket program so that it only shows data after the headers
#and a blank line have been received. Remember that recv receives characters (newlines and all), not lines.
#
#Solution

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

data = mysock.recv(512)
msg = data.decode()
end_header = msg.find('\r\n\r\n') + 4
print(msg[end_header:], end='')

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
