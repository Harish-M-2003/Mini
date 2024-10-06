
class Response:

    def __init__(self , status_code = 200) -> None:
        self.__status_code = status_code

    def set_status_code(self , status_code):
        self.__status_code = status_code
    
    def get_status_code(self , status_code):
        return self.__status_code

    def send(self , data):

        return f"HTTP 1/1 {self.__status_code} OK\n\n{data}".encode()
    
    def send_file(self , file):
        try:
            with open(file , "r") as data:
                content = data.read()
                return f"HTTP 1/1 {self.__status_code} OK\n\n{content}".encode()
        except:
            return "HTTP 1/1 400 Invalid Resource Request".encode()