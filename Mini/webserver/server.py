
# from Mini.mini import *
from socket import *

class TCPServer:

    def __init__(self , host , port):

        self.host = host
        self.port = port

    def start(self):
        
        print("[Mini] Starting Mini webserver .....")
        web_server = socket(AF_INET , SOCK_STREAM)
        print("[Mini] Socket created for Mini web server.")
        web_server.bind((self.host , self.port))
        print("[Mini] Assigned Host and Port for Mini webserver.")
        print("[Mini] Server can Listen for 10 active connections at a time.")
        web_server.listen(10)
        print(f"[Mini] Server Started at {self.host}:{self.port}")

        return web_server


