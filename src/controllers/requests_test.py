from src.repository import UserRepository
from src.application.helpers import HttpRequest
from src.controllers import (
    SearchUsersController,
    FindWebSitesController,
    UsersDetailController,
    FindUsersController,
)
from src.use_case import UserUseCases


def test_search_user_controller():
    repository = UserRepository()
    use_case = UserUseCases(repository)
    controller = SearchUsersController(use_case)

    http_request = HttpRequest(query={"name": "Graham"})
    response = controller.handle(http_request)
    assert response


def test_find_websites_controller():
    repository = UserRepository()
    use_case = UserUseCases(repository)
    controller = FindWebSitesController(use_case)

    http_request = HttpRequest()
    response = controller.handle(http_request)
    assert response


def test_users_detail_controller():
    repository = UserRepository()
    use_case = UserUseCases(repository)
    controller = UsersDetailController(use_case)

    http_request = HttpRequest()
    response = controller.handle(http_request)
    assert response


def test_find_users_controller():
    repository = UserRepository()
    use_case = UserUseCases(repository)
    controller = FindUsersController(use_case)

    http_request = HttpRequest()
    response = controller.handle(http_request)
    assert response
