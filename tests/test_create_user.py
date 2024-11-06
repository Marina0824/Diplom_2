import allure
import requests
from urls import URL, registration
from helper import new_user
from data import user_already_exists, required_field


class TestCreateUser:
    @allure.title("Успешное создание уникального пользователя")
    def test_create_unique_user(self, create_user_and_delete):
        email, password, name, token = create_user_and_delete

        assert token is not None

    @allure.title("Создание уже зарегистрированного пользователя")
    def test_create_same_user(self, create_user_and_delete):
        email, password, name, token = create_user_and_delete
        body = {"email": email,
                "password": password,
                "name": name}
        response = requests.post(f"{URL}{registration}", json=body)

        assert response.status_code == 403
        assert response.text == user_already_exists

    @allure.title("Создание пользователя без почты")
    def test_create_user_without_email(self):
        _, password, name = new_user()
        body = {"email": "",
                "password": password,
                "name": name}
        response = requests.post(f"{URL}{registration}", json=body)

        assert response.status_code == 403
        assert response.text == required_field

    @allure.title("Создание пользователя без пароля")
    def test_create_user_without_password(self):
        email, _, name = new_user()
        body = {"email": email,
                "password": "",
                "name": name}
        response = requests.post(f"{URL}{registration}", json=body)

        assert response.status_code == 403
        assert response.text == required_field

    @allure.title("Создание пользователя без имени")
    def test_create_user_without_name(self):
        email, password, _ = new_user()
        body = {"email": email,
                "password": password,
                "name": ""}
        response = requests.post(f"{URL}{registration}", json=body)

        assert response.status_code == 403
        assert response.text == required_field
