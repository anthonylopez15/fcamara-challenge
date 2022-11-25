from typing import Type

from src.application import HttpErrors, HttpResponse, HttpRequest
from src.controller import HandlerInterface


def fastapi_adapter(request: any, api_route: Type[HandlerInterface]) -> any:
    try:
        query_string_params = request.query_params
    except Exception as exc:
        print(exc)
        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

    http_request = HttpRequest(
        header=request.headers, body=request.body, query=query_string_params
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
