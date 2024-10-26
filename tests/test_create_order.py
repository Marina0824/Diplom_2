import allure
import requests
from urls import URL, create_order
from data import order, empty_order, provide_id, incorrect_hash


class TestCreateOrder:
    @allure.title("Успешное создание заказа с авторизацией")
    def test_create_order_with_login(self, create_user_and_delete):
        email, password, name, token = create_user_and_delete
        body = order
        response = requests.post(f"{URL}{create_order}", headers={"Authorization": token}, json=body)

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Успешное создание заказа без авторизации")
    def test_create_order_without_login(self, create_user_and_delete):
        body = order
        response = requests.post(f"{URL}{create_order}", json=body)

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredient(self, create_user_and_delete):
        body = empty_order
        response = requests.post(f"{URL}{create_order}", json=body)

        assert response.status_code == 400
        assert response.text == provide_id

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_with_incorrect_hash(self, create_user_and_delete):
        body = incorrect_hash
        response = requests.post(f"{URL}{create_order}", json=body)

        assert response.status_code == 500
