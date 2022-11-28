from abc import ABC, abstractmethod


class UserRepositoryInterface(ABC):
    @abstractmethod
    def find_all(self):
        raise Exception("Should implement method")

    @abstractmethod
    def search_user(self, name: str):
        raise Exception("Should implement method")

    @abstractmethod
    def detail(self):
        raise Exception("Should implement method")

    @abstractmethod
    def find_websites(self):
        raise Exception("Should implement method")
