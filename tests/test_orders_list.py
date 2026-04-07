import requests
import allure
from data.urls import Urls


class TestOrdersList:

    @allure.title('Получение списка заказов: возвращается 200 и список заказов')
    def test_get_orders_list_returns_list(self):
        with allure.step('Отправить GET-запрос на получение списка заказов'):
            response = requests.get(f'{Urls.BASE_URL}{Urls.ORDERS_LIST}')

        with allure.step('Проверить статус-код 200'):
            assert response.status_code == 200

        with allure.step('Проверить наличие поля orders в ответе'):
            assert "orders" in response.json()

        with allure.step('Проверить что orders - это список'):
            assert isinstance(response.json()["orders"], list)