from src.application import HttpRequest, HttpResponse
from src.controller.handler_interface import HandlerInterface
from src.use_case import UseCaseInterface


class UsersDetailController(HandlerInterface):
    def __init__(self, service: UseCaseInterface):
        self.service = service

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        response = self.service.detail()
        return HttpResponse(status_code=200, body=response)
