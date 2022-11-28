from fastapi import APIRouter, Request, Response

from src.application.helpers.api_adapter import fastapi_adapter
from src.application.composers import (
    find_users_composer,
    find_websites_composer,
    users_detail_composer,
    search_users_composer,
)
from src.application.helpers.token_verifier import token_verify
from src.application.util import convert_to_dict

router = APIRouter()


@router.get("/users/all")
@token_verify
def find_all(request: Request, response: Response):
    route_response = fastapi_adapter(request=request, api_route=find_users_composer())
    if route_response.status_code < 300:
        data = convert_to_dict(route_response.body)
        data = {"users": data}
        response.status_code = route_response.status_code
        return data

    error = {
        "status": route_response.status_code,
        "title": route_response.body["error"],
    }
    response.status_code = route_response.status_code
    return error


@router.get("/users/websites")
@token_verify
def find_websites(request: Request, response: Response):
    route_response = fastapi_adapter(
        request=request, api_route=find_websites_composer()
    )
    if route_response.status_code < 300:
        data = convert_to_dict(route_response.body)
        data = {"websites": data}
        response.status_code = route_response.status_code
        return data

    error = {
        "status": route_response.status_code,
        "title": route_response.body["error"],
    }
    response.status_code = route_response.status_code
    return error


@router.get("/users/detail")
@token_verify
def detail(request: Request, response: Response):
    route_response = fastapi_adapter(request=request, api_route=users_detail_composer())
    if route_response.status_code < 300:
        data = convert_to_dict(route_response.body)
        data = {"users": data}
        response.status_code = route_response.status_code
        return data

    error = {
        "status": route_response.status_code,
        "title": route_response.body["error"],
    }
    response.status_code = route_response.status_code
    return error


@router.get("/users")
@token_verify
def search_users(request: Request, response: Response):
    route_response = fastapi_adapter(request=request, api_route=search_users_composer())
    if route_response.status_code < 300:
        data = convert_to_dict(route_response.body)
        data = {"users": data}
        response.status_code = route_response.status_code
        return data

    error = {
        "status": route_response.status_code,
        "title": route_response.body["error"],
    }
    response.status_code = route_response.status_code
    return error
