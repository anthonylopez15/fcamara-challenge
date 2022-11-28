from fastapi.testclient import TestClient

from main import app
from src import env

client = TestClient(app)

endpoints = {
    "FIND_WEBSITES": "/api/users/websites",
    "USER_DETAILS": "/api/users/detail",
    "SEARCH_USERS": "/api/users",
    "FIND_ALL": "/api/users/all",
}
token_fake = env.TOKEN_FAKE


def authorization_bearer():
    return {"Authorization": f"Bearer {token_fake}"}


def test_find_websites():
    response = client.get(endpoints["FIND_WEBSITES"], headers=authorization_bearer())
    assert response.status_code == 200


def test_users_detail():
    response = client.get(endpoints["USER_DETAILS"], headers=authorization_bearer())
    assert response.status_code == 200


def test_search_users():
    response = client.get(
        endpoints["SEARCH_USERS"],
        params={"name": "Patricia"},
        headers=authorization_bearer(),
    )
    assert response.status_code == 200


def test_search_users_not_found():
    response = client.get(
        endpoints["SEARCH_USERS"],
        params={"name": "something"},
        headers=authorization_bearer(),
    )
    assert not response.json().get("users")


def test_find_user():
    response = client.get(endpoints["FIND_ALL"], headers=authorization_bearer())
    assert response.status_code == 200
