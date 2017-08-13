import socket
import os
needkey=not os.path.exists("keyfile.key")
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c=clientsocket

clientsocket.connect(('localhost', 8000))
print(c.recv(8000))
f="UTF-8"
if needkey:
    clientsocket.send(bytes("Createkey",f))
    with open("keyfile.key","w") as f:
        key=c.recv(1000).decode("UTF-8")
        f.write(key)
        print(key)
    f="UTF-8"
        
