from src.adapter import RepositoryInterface
from src.use_case.use_case_interface import UseCaseInterface


class Service(UseCaseInterface):
    def __init__(self, repository: RepositoryInterface):
        self.repository = repository

    def find_all(self):
        response = self.repository.find_all()
        return response

    def search_user(self, name: str):
        response = None
        validate_entry = isinstance(name, str)
        if validate_entry:
            response = self.repository.search_user(name=name)
        return response

    def detail(self):
        response = self.repository.detail()
        return response

    def find_websites(self):
        response = self.repository.find_websites()
        return response
