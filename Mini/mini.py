from webserver import server
from webserver.Response import Response


class Mini:

    def __init__(self, host="0.0.0.0", port=54321):

        self.server = server.TCPServer(host, port).start()
        self.end_points = {}

    def run(self):

        while True:
            client, ip_port = self.server.accept()
            request = client.recv(1024)
            response = self.process_request(request)
            client.sendall(response)
            client.close()

    def process_request(self, request):

        request = request.decode("utf-8").split("\n")
        response = Response()
        request_details = request[0].split()

        if request_details[0] == "GET":
            end_point = self.end_points.get(request_details[1], None)
            if end_point:
                return end_point["GET"](request, response)
            else:
                response.set_status_code(400)
                return response.send("Method Not Allowed")
        else:
            response.set_status_code(400)
            return response.send("Method Not Allowed")

    def get(self, path=None):

        def wrapper(handler):

            if path not in self.end_points:
                self.end_points[path] = {}

            self.end_points[path]["GET"] = handler

        return wrapper

    def post(self, path):
        pass

    def delete(self, path):
        pass


if __name__ == "__main__":

    api = Mini()

    @api.get("/users")
    def login_page(req, res):
        return res.send("harish")

    @api.get("/login")
    def example_login(req, res):
        return res.send_file(r"C:\Users\Harish\harish\Projects\Mini\Mini\login.html")

    api.run()
