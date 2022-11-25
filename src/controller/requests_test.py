from src.adapter import Repository
from src.application import HttpRequest
from src.controller import (
    SearchUsersController,
    FindWebSitesController,
    UsersDetailController,
    FindUsersController,
)
from src.use_case import Service


def test_search_user_controller():
    repository = Repository()
    use_case = Service(repository)
    controller = SearchUsersController(use_case)

    http_request = HttpRequest(query={"name": "Graham"})
    response = controller.handle(http_request)
    assert response


def test_find_websites_controller():
    repository = Repository()
    use_case = Service(repository)
    controller = FindWebSitesController(use_case)

    http_request = HttpRequest()
    response = controller.handle(http_request)
    assert response


def test_users_detail_controller():
    repository = Repository()
    use_case = Service(repository)
    controller = UsersDetailController(use_case)

    http_request = HttpRequest()
    response = controller.handle(http_request)
    assert response


def test_find_users_controller():
    repository = Repository()
    use_case = Service(repository)
    controller = FindUsersController(use_case)

    http_request = HttpRequest()
    response = controller.handle(http_request)
    assert response
