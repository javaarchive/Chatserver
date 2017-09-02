#Options
server="fathhomepc1.t-mobile.com"
port=8000
backgroundcolor="#fff7e5"
foregroundcolor="#73ff5e"
import socket
import os
import time

needkey=not os.path.exists("keyfile.key")
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c=clientsocket

clientsocket.connect((server, port))
print(c.recv(8000))
f="UTF-8"
if needkey:
    clientsocket.send(bytes("Createkey",f))
    with open("keyfile.key","w") as f:
        key=c.recv(1000).decode("UTF-8")
        f.write(key)
        print(key)
        try:
            name=input("You need a name: ")
        except:
            name="anoynomous"
        c.send(bytes(name,"UTF-8"))
    f="UTF-8"
else:
    with open("keyfile.key","r") as fi:

        key=int(fi.readline())
print("Loading connection gui")
from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import *
t=Tk()
output=ScrolledText(t,bg=backgroundcolor,fg=foregroundcolor)
output.pack(fill=BOTH,expand=YES)
chatbox=Entry(t,width=120)
def chat(enter=0):
    global key
    c.send(bytes("chatmessage","UTF-8"))
    print(type(key))
    c.send(str(key).encode("UTF-8"))
    time.sleep(1)
    c.send(bytes(chatbox.get(),"UTF-8"))
    chatbox.delete("0",END)
    updatescreen()
btn=Button(t,text="chat",command=chat)
btn.pack()
chatbox.pack()
menu=Menu(t)
chatcontrols=Menu(t)
cache=""
print("loading")
c.send(bytes("update","UTF-8"))
output.insert(END,c.recv(5094).decode())
e=True
chatbox.bind("<Key-Return>",chat)
def updatescreen(x=0):
    global cache,e
    if e:
        e=not e
        return 0
    c.send(bytes("get","UTF-8"))
    #print("Waiting")
    out=c.recv(50000).decode()
    if out!=cache:
        output.insert(END,out)
        cache=out
def exit1(x=0):
    c.send(bytes("exit","UTF-8"))
def stop(x=0):
    c.send(bytes("Shutdown","UTF-8"))
chatcontrols.add_command(label="Update", command=updatescreen)
chatcontrols.add_command(label="terminate server", command=stop)
chatcontrols.add_command(label="Exit program", command=exit1)
menu.add_cascade(label="Chat controls", menu=chatcontrols)
t.config(menu=menu)
print("Debug:Finish")
while True:
    updatescreen()
    t.update_idletasks()
    time.sleep(0.05)
    t.update()
