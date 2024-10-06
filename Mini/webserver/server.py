
# from Mini.mini import *
from socket import *

class TCPServer:

    def __init__(self , host , port):

        self.host = host
        self.port = port

    def start(self):
        
        print("[Mini] Initializing a webserver .....")
        print("[Mini] Creating a socket for enabling communication.")
        web_server = socket(AF_INET , SOCK_STREAM)
        print("[Mini] Socket created for webserver.")
        print("[Mini] Assigning Host address and a Port number for webserver.")
        web_server.bind((self.host , self.port))
        print("[Mini] Assigned Host address and a Port for webserver.")
        print("[Mini] Server can Listen for 10 active connections at a time.")
        web_server.listen(10)
        print(f"[Mini] Server Started at {self.host}:{self.port}")

        return web_server


