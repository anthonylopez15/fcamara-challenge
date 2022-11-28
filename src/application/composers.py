from src.repository import UserRepository
from src.controllers import (
    FindUsersController,
    SearchUsersController,
    FindWebSitesController,
    UsersDetailController,
)
from src.use_case import UserUseCases


def find_users_composer():
    repository = UserRepository()
    service = UserUseCases(repository)
    controller = FindUsersController(service)
    return controller


def search_users_composer():
    repository = UserRepository()
    service = UserUseCases(repository)
    controller = SearchUsersController(service)
    return controller


def find_websites_composer():
    repository = UserRepository()
    service = UserUseCases(repository)
    controller = FindWebSitesController(service)
    return controller


def users_detail_composer():
    repository = UserRepository()
    service = UserUseCases(repository)
    controller = UsersDetailController(service)
    return controller
