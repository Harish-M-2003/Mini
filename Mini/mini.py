from webserver import server

class Mini:

    def __init__(self , host , port):
        
        self.server = server.TCPServer(host , port).start()
        self.__start()
    
    def __start(self):

        while True:
            client , ip_port = self.server.accept()
            request = client.recv(1024)
            response = self.process_request(request)
            client.sendall(response)
            client.close()

    def process_request(self , request):
        
        request = request.decode('utf-8').split('\n')

        request_details = request[0].split()
        if request_details[0] == "GET":
            return self.get(request_details[1])

        return b"HTTP 1/1 200 OK\n\n <html><head><title>learning socket programming</title></head><body>Hello World</body>"
    
    def get(self , path):
        print("Get" , path)
        pass

    def post(self , path):
        pass

    def delete(self , path):
        pass

if __name__ == "__main__":

    api = Mini("0.0.0.0" , 54321)

    api.get("/")
    
