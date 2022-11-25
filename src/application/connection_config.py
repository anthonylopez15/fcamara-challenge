import json
from urllib.request import urlopen


class ConnectionHandler:
    def __init__(self):
        self.__connection_url = "https://jsonplaceholder.typicode.com/users"
        self.response = self.__get_source()

    def __get_source(self):
        with urlopen(self.__connection_url) as response:
            source = response.read()
            response.close()
        return json.loads(source)
