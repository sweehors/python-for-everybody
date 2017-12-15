"""
this program didn't work - kept getting 404. Ended up using Firebug to manually examine the headers
"""

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = "www.data.pr4e.org"
PORT = 80
mysock.connect((HOST, PORT))
cmd = "GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n".encode()
#mysock.connect(('www.py4inf.com', 80))
#cmd = 'GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())

mysock.close()