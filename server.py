import socket
import threading
import shelve as sh
sfile=sh.open("Ids.save")
s=socket.socket()
s.bind(("", 8000))
s.listen(100)

class serve (threading.Thread):
   def __init__(self, client):
      threading.Thread.__init__(self)
      self.c=client
   def run(self):
        global stop
        f="UTF-8"
        conn=self.c
        try:
           conn.send(bytes("Connected","UTF-8"))
           while True:
               
               data = conn.recv(1024)
               if data.decode("UTF-8")=="Createkey":
                   newid=str(len(sfile)+1)
                   sfile[newid]={"name":""}
                   conn.sendall(bytes(newid,f))
               else:
                   conn.sendall(bytes("still in progress",f))
        finally:
            print("Connection exited")
try:
    while True:
        c,a=s.accept()
        x=serve(c)
        x.start()
finally:
    print("Status program quit")
        
    
