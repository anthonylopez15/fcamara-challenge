from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

endpoints = {
    "FIND_WEBSITES": "/api/users/websites",
    "USER_DETAILS": "/api/users/detail",
    "SEARCH_USERS": "/api/users",
    "FIND_ALL": "/api/users/all",
}


def test_find_websites():
    response = client.get(endpoints["FIND_WEBSITES"])
    assert response.status_code == 200


def test_users_detail():
    response = client.get(endpoints["USER_DETAILS"])
    assert response.status_code == 200


def test_search_users():
    response = client.get(endpoints["SEARCH_USERS"], params={"name": "Patricia"})
    assert response.status_code == 200


def test_search_users_not_found():
    response = client.get(endpoints["SEARCH_USERS"], params={"name": "something"})
    assert not response.json()


def test_find_user():
    response = client.get(endpoints["FIND_ALL"])
    assert response.status_code == 200
