import urllib.request as Url
import tkinter as tk
from tkinter import ttk
import time
#import wget
#import requests
def dwn(url):
    file_name = url.split('/')[-1]
    u = urllib2.urlopen(url)
    f = open(file_name, 'wb')
    meta = u.info()
    file_size = len(u.read())
    print("Downloading: %s Bytes: %s" % (file_name, file_size))

    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        print(status,end="")

    f.close()
def d(url,filename="cache.txt"):
    with open(filename,"wb") as f:
        vz=Url.urlopen(url).read()
        #vz=str(vz).replace("\\\\",'''\
#''').replace("'","")[1:]
        #vz=vz.replace("\\n",'''\n''')
        print(vz)
        f.write(vz)
        

    return vz
        
ready=False
    


class SampleApp(tk.Frame):

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        #self.title("Update(press start to start)")
        self.button = ttk.Button(self,text="Start Installation", command=self.start)
        self.button.pack()
        self.progress = ttk.Progressbar(self, orient="horizontal",
                                        length=200, mode="determinate")
        self.progress.pack()
        self.updated=0
        self.bytes = 0
        self.maxbytes = 50000

    def start(self):
        global ready
        if ready==False:
            return 0
        self.l=ttk.Label(self,text="percentage")
        self.l.pack()
        if self.updated==0:
            self.progress["value"] = 0
            self.maxbytes = 5000
            self.progress["maximum"] = 500
            self.read_bytes()
            self.updated=self.updated+1
        else:
            self.progress["value"] = 0
            self.bytes=0
            self.read_bytes()
            self.updated=self.updated+1
            

    def read_bytes(self):
        '''simulate reading 500 bytes; update progress bar'''
        self.bytes += 50
        self.progress["value"] = self.bytes
        if self.bytes==100:
            v=d('https://raw.githubusercontent.com/javaarchive/chatserver/master/client.py', "client.py")
        if self.bytes==150:
            v=d('https://raw.githubusercontent.com/javaarchive/chatserver/master/chat.save', "chat.save")
        
        if self.bytes==200:
            v=d('https://raw.githubusercontent.com/javaarchive/chatserver/master/server.py', "server.py")
        if self.bytes==250:
            print("  press enter to finish")
            input()
        
        
                
        
            
        if self.bytes < self.maxbytes:
            
            self.l["text"]=str(self.bytes/(self.maxbytes/100))+"%"
            # read more bytes after 100 ms
            self.after(100, self.read_bytes)
        else:
            self.bell()
            #self.title("Finished updating")
            self.label=ttk.Label(self,text="Download provoided by Github \nYou may close this window")
            self.label.pack()
def ds():
    ty.destroy()
    global ready
    ready=True
    tr.delete("0.0",tk.END)
    tr.insert(tk.END,"You may now install. Press start to install")
    
t=tk.Tk()
t.title("installation")
tr=tk.Text()
tr.insert(tk.END,'''
The following program will install a chat server\n
Press next to countunie
''')
tr.pack()
ts=SampleApp(master=t)
ts.pack()
ty=ttk.Button(t,text="next",command=ds)
ty.pack()
#urllib.urlretrieve('url_to_file', file_name)
#v=d('https://raw.githubusercontent.com/javaarchive/PIDLE/master/idlelaunch.py', "Updatedidle.py")
t.mainloop()

