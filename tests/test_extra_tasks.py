import pytest
import requests
import allure
from data.urls import Urls
from data.test_data import OrderData, CourierData


class TestExtraTasks:

    @allure.title('Удаление курьера: успешное удаление возвращает 200 и ok true')
    def test_delete_courier_success(self, create_and_delete_courier):
        courier_data = create_and_delete_courier

        with allure.step('Получить id курьера через авторизацию'):
            login_response = requests.post(
                f'{Urls.BASE_URL}{Urls.COURIER_LOGIN}',
                data={"login": courier_data[0], "password": courier_data[1]}
            )
            courier_id = login_response.json().get("id")

        with allure.step(f'Отправить DELETE-запрос на удаление курьера с id {courier_id}'):
            response = requests.delete(f'{Urls.BASE_URL}{Urls.COURIER_DELETE}{courier_id}')

        with allure.step('Проверить статус-код 200'):
            assert response.status_code == 200

        with allure.step('Проверить тело ответа ok true'):
            assert response.json() == {"ok": True}

    @allure.title('Удаление курьера: без id возвращает 404')
    def test_delete_courier_without_id_fails(self):
        with allure.step('Отправить DELETE-запрос без id курьера'):
            response = requests.delete(f'{Urls.BASE_URL}{Urls.COURIER_DELETE}')

        with allure.step('Проверить статус-код 404'):
            assert response.status_code == 404

    @allure.title('Принятие заказа: успешное принятие возвращает 200 и ok true')
    def test_accept_order_success(self, create_and_delete_courier):
        courier_data = create_and_delete_courier

        with allure.step('Создать заказ'):
            order_response = requests.post(f'{Urls.BASE_URL}{Urls.ORDERS_CREATE}', json=OrderData.TEST_ORDER_1)
            track = order_response.json().get("track")

        with allure.step(f'Получить id заказа по треку {track}'):
            orders_response = requests.get(f'{Urls.BASE_URL}{Urls.ORDERS_TRACK}?t={track}')
            order_id = orders_response.json().get("order", {}).get("id")

        with allure.step('Получить id курьера'):
            login_response = requests.post(
                f'{Urls.BASE_URL}{Urls.COURIER_LOGIN}',
                data={"login": courier_data[0], "password": courier_data[1]}
            )
            courier_id = login_response.json().get("id")

        with allure.step(f'Отправить PUT-запрос на принятие заказа {order_id} курьером {courier_id}'):
            response = requests.put(
                f'{Urls.BASE_URL}{Urls.ORDERS_ACCEPT}{order_id}',
                params={"courierId": courier_id}
            )

        with allure.step('Проверить статус-код 200'):
            assert response.status_code == 200

        with allure.step('Проверить тело ответа ok true'):
            assert response.json() == {"ok": True}

    @allure.title('Получение заказа по треку: успешный запрос возвращает 200 и объект заказа')
    def test_get_order_by_track_success(self):
        with allure.step('Создать заказ'):
            create_response = requests.post(f'{Urls.BASE_URL}{Urls.ORDERS_CREATE}', json=OrderData.TEST_ORDER_2)
            track = create_response.json().get("track")

        with allure.step(f'Отправить GET-запрос на получение заказа по треку {track}'):
            response = requests.get(f'{Urls.BASE_URL}{Urls.ORDERS_TRACK}?t={track}')

        with allure.step('Проверить статус-код 200'):
            assert response.status_code == 200

        with allure.step('Проверить наличие поля order в ответе'):
            assert "order" in response.json()