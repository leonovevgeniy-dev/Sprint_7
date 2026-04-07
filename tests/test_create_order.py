import pytest
import requests
import allure
from data.urls import Urls
from data.test_data import OrderData


class TestCreateOrder:

    @allure.title('Создание заказа: с разными вариантами цветов возвращает 201 и track')
    @pytest.mark.parametrize("color", OrderData.COLOR_VARIANTS)
    def test_create_order_with_different_colors(self, color):
        order_data = OrderData.ORDER_DATA.copy()
        order_data["color"] = color

        with allure.step(f'Отправить POST-запрос на создание заказа с цветом {color}'):
            response = requests.post(f'{Urls.BASE_URL}{Urls.ORDERS_CREATE}', json=order_data)

        with allure.step('Проверить статус-код 201'):
            assert response.status_code == 201

        with allure.step('Проверить наличие track в ответе'):
            assert "track" in response.json()

        with allure.step('Проверить что track - целое число'):
            assert isinstance(response.json()["track"], int)

    @allure.title('Создание заказа: без указания цвета возвращает 201 и track')
    def test_create_order_without_color_success(self):
        order_data = OrderData.ORDER_DATA.copy()
        order_data["color"] = []

        with allure.step('Отправить POST-запрос на создание заказа без цвета'):
            response = requests.post(f'{Urls.BASE_URL}{Urls.ORDERS_CREATE}', json=order_data)

        with allure.step('Проверить статус-код 201'):
            assert response.status_code == 201

        with allure.step('Проверить наличие track в ответе'):
            assert "track" in response.json()