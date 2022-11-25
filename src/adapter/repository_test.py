from . import Repository


def test_find_all():
    repository = Repository()
    response = repository.find_all()
    assert response


def test_detail_users():
    repository = Repository()
    response = repository.detail()
    assert response


def test_search_users():
    repository = Repository()
    response = repository.search_user(name="Howell")
    assert response


def test_search_users_not_found():
    repository = Repository()
    response = repository.search_user(name="something")
    assert not response


def test_find_websites():
    repository = Repository()
    response = repository.find_websites()
    assert response
