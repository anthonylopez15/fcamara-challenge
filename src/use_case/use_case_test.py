from src.repository import UserRepository
from src.use_case import UserUseCases


def test_find_users():
    repository = UserRepository()
    use_case = UserUseCases(repository)
    response = use_case.find_all()
    assert response


def test_detail_users():
    repository = UserRepository()
    use_case = UserUseCases(repository)
    response = use_case.detail()
    assert response


def test_find_websites():
    repository = UserRepository()
    use_case = UserUseCases(repository)
    response = use_case.find_websites()
    assert response


def test_search_user():
    repository = UserRepository()
    use_case = UserUseCases(repository)
    response = use_case.search_user(name="Chelsey")
    assert response


def test_search_users_not_found():
    repository = UserRepository()
    use_case = UserUseCases(repository)
    response = use_case.search_user(name="something")
    assert not response
