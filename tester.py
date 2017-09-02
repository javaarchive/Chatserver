class test:
    def do(self):
        raise RuntimeError("BVad thing")
import urllib.request as urllib
import urllib.parse as urlk
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
from sys import argv
class S(BaseHTTPRequestHandler):
        def _set_headers(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

        def do_GET(self):
            self._set_headers()
            self.wfile.write("<html><body><h1>hi!</h1></body></html>")

        def do_HEAD(self):
            self._set_headers()
            
        def do_POST(self):
            # Doesn't do anything with posted data
            self._set_headers()
            self.wfile.write("<html><body><h1>POST!</h1></body></html>")
class t(test):
    def do(self):
        url = 'http://httpbin.org/post'
        data = urlk.urlencode({'name' : 'joe',
                                 'age'  : '10'})
        content = urllib.urlopen(url=url, data=data).read().decode()
        print(content)
    
    

    
            
        
            
k=t()


def run(server_class=HTTPServer, handler_class=S, port=80):
            server_address = ('', port)
            httpd = server_class(server_address, handler_class)
            print('Starting httpd...')
            httpd.serve_forever()

            
            

            if len(argv) == 2:
                run(port=int(argv[1]))
            else:
                run()
