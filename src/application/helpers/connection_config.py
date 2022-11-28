import json
from urllib.request import urlopen

from src import env


class ConnectionHandler:
    def __init__(self):
        self.__connection_url = env.URL_SERVER
        self.response = self.__get_source()

    def __get_source(self):
        with urlopen(self.__connection_url) as response:
            source = response.read()
            response.close()
        return json.loads(source)
