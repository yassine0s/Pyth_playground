from http.server import HTTPServer
import json


class SimpleHTTPServer:

    def __init__(self) -> None:
        pass

    def start_server(self,host,handler,port):
        self.httpd = HTTPServer(host,handler,port)