from src.application.helpers import HttpRequest, HttpResponse, HttpErrors
from src.controllers.handler_interface import HandlerInterface
from src.use_case import UsersUseCasesInterface


class SearchUsersController(HandlerInterface):
    def __init__(self, service: UsersUseCasesInterface):
        self.service = service

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        if http_request.query:
            query_params = http_request.query.keys()
            if "name" in query_params:
                name = http_request.query["name"]
                response = self.service.search_user(name=name)
            else:
                http_error = HttpErrors.error_400()
                return HttpResponse(
                    status_code=http_error["status_code"], body=http_error["body"]
                )
            return HttpResponse(status_code=200, body=response)

        http_error = HttpErrors.error_422()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )
