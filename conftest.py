import pytest
import requests
from urls import URL, registration, delete
from helper import new_user


@pytest.fixture
def create_user_and_delete():
    email, password, name = new_user()
    body = {"email": email,
            "password": password,
            "name": name}
    response = requests.post(f"{URL}{registration}", json=body)
    assert response.status_code == 200
    token = response.json()["accessToken"]

    yield email, password, name, token

    response_delete = requests.delete(f"{URL}{delete}", headers={"Authorization": token})
    assert response_delete.status_code == 202
