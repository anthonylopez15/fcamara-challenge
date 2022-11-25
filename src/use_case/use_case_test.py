from src.adapter import Repository
from src.use_case import Service


def test_find_users():
    repository = Repository()
    use_case = Service(repository)
    response = use_case.find_all()
    assert response


def test_detail_users():
    repository = Repository()
    use_case = Service(repository)
    response = use_case.detail()
    assert response


def test_find_websites():
    repository = Repository()
    use_case = Service(repository)
    response = use_case.find_websites()
    assert response


def test_search_user():
    repository = Repository()
    use_case = Service(repository)
    response = use_case.search_user(name="Chelsey")
    assert response


def test_search_users_not_found():
    repository = Repository()
    use_case = Service(repository)
    response = use_case.search_user(name="something")
    assert not response
