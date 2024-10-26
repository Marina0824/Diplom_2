import allure
import requests
from urls import URL, change_data
from helper import new_user
from data import should_be_authorised


class TestChangeUserData:
    @allure.title("Изменение почты пользователя с авторизацией")
    def test_change_email_with_login(self, create_user_and_delete):
        email, password, name, token = create_user_and_delete
        new_email, new_password, new_name = new_user()
        body = {"email": new_email}
        response = requests.patch(f"{URL}{change_data}", headers={"Authorization": token}, json=body)

        assert response.status_code == 200
        assert response.text == f'{{"success":true,"user":{{"email":"{new_email}","name":"{name}"}}}}'

    @allure.title("Изменение пароля пользователя с авторизацией")
    def test_change_password_with_login(self, create_user_and_delete):
        email, password, name, token = create_user_and_delete
        new_email, new_password, new_name = new_user()
        body = {"password": new_password}
        response = requests.patch(f"{URL}{change_data}", headers={"Authorization": token}, json=body)

        assert response.status_code == 200
        assert response.text == f'{{"success":true,"user":{{"email":"{email}","name":"{name}"}}}}'

    @allure.title("Изменение имени пользователя с авторизацией")
    def test_change_name_with_login(self, create_user_and_delete):
        email, password, name, token = create_user_and_delete
        new_email, new_password, new_name = new_user()
        body = {"name": new_name}
        response = requests.patch(f"{URL}{change_data}", headers={"Authorization": token}, json=body)

        assert response.status_code == 200
        assert response.text == f'{{"success":true,"user":{{"email":"{email}","name":"{new_name}"}}}}'

    @allure.title("Изменение почты пользователя без авторизации")
    def test_change_email_without_login(self, create_user_and_delete):
        new_email, new_password, new_name = new_user()
        body = {"email": new_email}
        response = requests.patch(f"{URL}{change_data}", json=body)

        assert response.status_code == 401
        assert response.text == should_be_authorised

    @allure.title("Изменение пароля пользователя без авторизации")
    def test_change_password_without_login(self, create_user_and_delete):
        new_email, new_password, new_name = new_user()
        body = {"password": new_password}
        response = requests.patch(f"{URL}{change_data}", json=body)

        assert response.status_code == 401
        assert response.text == should_be_authorised

    @allure.title("Изменение имени пользователя без авторизации")
    def test_change_name_without_login(self, create_user_and_delete):
        new_email, new_password, new_name = new_user()
        body = {"name": new_name}
        response = requests.patch(f"{URL}{change_data}", json=body)

        assert response.status_code == 401
        assert response.text == should_be_authorised
