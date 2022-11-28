from typing import Type

from src.application.helpers import HttpRequest, HttpResponse, HttpErrors
from src.controllers import HandlerInterface


def fastapi_adapter(request: any, api_route: Type[HandlerInterface]) -> any:

    http_request = HttpRequest(
        header=request.headers, body=request.body, query=request.query_params
    )
    try:
        response = api_route.handle(http_request)
    except Exception as exc:
        print(exc)
        http_error = HttpErrors.error_500()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )
    return response
