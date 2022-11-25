from src.adapter import Repository
from src.controller import (
    FindUsersController,
    SearchUsersController,
    FindWebSitesController,
    UsersDetailController,
)
from src.use_case import Service


def find_users_composer():
    repository = Repository()
    service = Service(repository)
    controller = FindUsersController(service)
    return controller


def search_users_composer():
    repository = Repository()
    service = Service(repository)
    controller = SearchUsersController(service)
    return controller


def find_websites_composer():
    repository = Repository()
    service = Service(repository)
    controller = FindWebSitesController(service)
    return controller


def users_detail_composer():
    repository = Repository()
    service = Service(repository)
    controller = UsersDetailController(service)
    return controller
