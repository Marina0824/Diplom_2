import allure
import requests
from urls import URL, login
from data import incorrect_data, incorrect_email, incorrect_password


class TestLoginUser:
    @allure.title("Логин под существующим пользователем")
    def test_login_exist_user(self, create_user_and_delete):
        email, password, name, token = create_user_and_delete
        body = {"email": email,
                "password": password}
        response = requests.post(f"{URL}{login}", json=body)

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "accessToken" in response.json()

    @allure.title("Логин с неверной почтой")
    def test_login_incorrect_email(self, create_user_and_delete):
        email, password, name, token = create_user_and_delete
        body = {"email": incorrect_email,
                "password": password}
        response = requests.post(f"{URL}{login}", json=body)

        assert response.status_code == 401
        assert response.text == incorrect_data

    @allure.title("Логин с неверным паролем")
    def test_login_incorrect_password(self, create_user_and_delete):
        email, password, name, token = create_user_and_delete
        body = {"email": email,
                "password": incorrect_password}
        response = requests.post(f"{URL}{login}", json=body)

        assert response.status_code == 401
        assert response.text == incorrect_data
