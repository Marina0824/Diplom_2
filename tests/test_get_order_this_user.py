import allure
import requests
from urls import URL, create_order, get_orders
from data import order, should_be_authorised


class TestGetOrder:
    @allure.title("Получение заказов авторизованного пользователя")
    def test_get_orders_login_user(self, create_user_and_delete):
        email, password, name, token = create_user_and_delete
        body = order
        requests.post(f"{URL}{create_order}", headers={"Authorization": token}, json=body)
        response = requests.get(f"{URL}{get_orders}", headers={"Authorization": token})

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Получение заказов неавторизованного пользователя")
    def test_get_orders_not_login_user(self, create_user_and_delete):
        email, password, name, token = create_user_and_delete
        body = order
        requests.post(f"{URL}{create_order}", headers={"Authorization": token}, json=body)
        response = requests.get(f"{URL}{get_orders}")

        assert response.status_code == 401
        assert response.text == should_be_authorised
