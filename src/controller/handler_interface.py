from abc import ABC, abstractmethod

from src.application import HttpRequest, HttpResponse


class HandlerInterface(ABC):
    @abstractmethod
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        raise Exception("Should implement method")
