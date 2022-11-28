from src.application.helpers import HttpRequest, HttpResponse
from src.controllers.handler_interface import HandlerInterface
from src.use_case import UsersUseCasesInterface


class UsersDetailController(HandlerInterface):
    def __init__(self, service: UsersUseCasesInterface):
        self.service = service

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        response = self.service.detail()
        return HttpResponse(status_code=200, body=response)
