import os
import socket
import threading
import shelve as sh
import signal
sfile=sh.open("Ids.save")
s=socket.socket()
s.bind((socket.gethostname(), 8000))#"" for local use, use socket.gethostname() for internat acess
s.listen(100)
stop=False
with open("chat.save","r") as r:
   chat=r.read()
class ExitCommand(Exception):
    pass


def signal_handler(signal, frame):
    raise ExitCommand()


def thread_job():
    global stop
    while not stop:
       pass
    os.kill(os.getpid(), signal.SIGINT)
signal.signal(signal.SIGINT, signal_handler)
threading.Thread(target=thread_job).start()
class serve (threading.Thread):
   def __init__(self, client):
      threading.Thread.__init__(self)
      self.c=client
   def run(self):
        global stop,chat
        f="UTF-8"
        conn=self.c
        try:
           conn.send(bytes("Connected","UTF-8"))
           while True:
               
               data = conn.recv(1024)
               if data.decode("UTF-8")=="Createkey":
                   newid=str(len(sfile)+1)
                   
                   conn.sendall(bytes(newid,f))
                   name=conn.recv(2094).decode()
                   sfile[newid]={"name":name}
                   chat=chat+"[Server]"+name+"joined the server      \n"
               
               #conn.sendall(bytes("still in progress",f))
               if data.decode("UTF-8")=="Shutdown":
                  stop=True
               if data.decode("UTF-8")=="update":
                  conn.send(bytes(chat,"UTF-8"))
               if data.decode("UTF-8")=="chatmessage":
                  sup=conn.recv(50)
                  print(type(sup))
                  print(sup)
                  print(dir(sup))
                  sup=sup.decode()
                  print(type(sup))
                  print(sup)
                  sup=int(sup)
                  dict1=sfile[str(sup)]
                  
       
                  
                  print("Incoming message"+str(dict1))
                  chat=chat+"["+dict1["name"]+"]"+conn.recv(1092).decode("UTF-8")+"\n"
                  with open("chat.save","w") as q:
                      q.write(chat)
               if data.decode("UTF-8")=="exit":
                  
                  break
               
        finally:
            print("Connection exited")
try:
    while not stop:
        c,a=s.accept()
        x=serve(c)
        x.start()
finally:
    print("Status program quit")
    with open("chat.save","w") as q:
       q.write(chat)
       
       
        
    
