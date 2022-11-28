from typing import List

from . import UserRepositoryInterface
from src.application.helpers import ConnectionHandler
from src.entity import Users, DetailUser, UserSearch, WebSites


class UserRepository(UserRepositoryInterface):
    def __init__(self):
        self.__connection = ConnectionHandler()
        self.source = self.__connection.response

    def find_all(self) -> List[Users]:
        response = self.source
        users = [
            Users(
                id=item["id"],
                name=item["name"],
                email=item["email"],
                phone=item["phone"],
                website=item["website"],
                company=item["company"],
            )
            for item in response
        ]
        return users

    def search_user(self, name: str) -> List[UserSearch]:
        users = self.find_all()
        user_found = [
            UserSearch(id=element.id, name=element.name)
            for element in users
            if name in element.name
        ]
        return user_found

    def detail(self) -> List[DetailUser]:
        response = self.source
        detail = [
            DetailUser(
                name=item["name"], email=item["email"], company=item["company"]["name"]
            )
            for item in response
        ]
        detail.sort(key=lambda item: item.name)
        return detail

    def find_websites(self) -> List[WebSites]:
        response = self.source
        detail = [WebSites(website=item["website"]) for item in response]
        return detail
