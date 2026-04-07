import pytest
import requests
import allure
from data.urls import Urls
from data.test_data import CourierData


class TestCreateCourier:

    @allure.title('Создание курьера: успешный запрос возвращает 201 и ok true')
    def test_create_courier_success(self, random_courier_data):
        with allure.step('Отправить POST-запрос на создание курьера'):
            response = requests.post(
                f'{Urls.BASE_URL}{Urls.COURIER_CREATE}',
                data=random_courier_data
            )

        with allure.step('Проверить статус-код 201'):
            assert response.status_code == 201

        with allure.step('Проверить тело ответа ok true'):
            assert response.json() == {"ok": True}

    @allure.title('Создание курьера: нельзя создать двух одинаковых курьеров, возвращается 409')
    def test_create_duplicate_courier_fails(self, create_and_delete_courier):
        courier_data = create_and_delete_courier
        payload = {
            "login": courier_data[0],
            "password": courier_data[1],
            "firstName": courier_data[2]
        }

        with allure.step('Отправить повторный POST-запрос с теми же данными'):
            response = requests.post(f'{Urls.BASE_URL}{Urls.COURIER_CREATE}', data=payload)

        with allure.step('Проверить статус-код 409'):
            assert response.status_code == 409

        with allure.step('Проверить сообщение об ошибке'):
            assert response.json()["message"] == CourierData.ERROR_LOGIN_ALREADY_USED

    @allure.title('Создание курьера: при отсутствии обязательного поля возвращается 400')
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_missing_field_fails(self, random_courier_data, missing_field):
        payload = random_courier_data.copy()
        del payload[missing_field]

        with allure.step(f'Отправить POST-запрос без поля {missing_field}'):
            response = requests.post(f'{Urls.BASE_URL}{Urls.COURIER_CREATE}', data=payload)

        with allure.step('Проверить статус-код 400'):
            assert response.status_code == 400

        with allure.step('Проверить сообщение об ошибке'):
            assert CourierData.ERROR_INSUFFICIENT_DATA in response.json().get("message", "")

    @allure.title('Создание курьера: можно создать курьера без firstName, возвращается 201')
    def test_create_courier_without_firstname_success(self, random_courier_data):
        payload = {
            "login": random_courier_data["login"],
            "password": random_courier_data["password"]
        }

        with allure.step('Отправить POST-запрос без поля firstName'):
            response = requests.post(f'{Urls.BASE_URL}{Urls.COURIER_CREATE}', data=payload)

        with allure.step('Проверить статус-код 201'):
            assert response.status_code == 201

        with allure.step('Проверить тело ответа ok true'):
            assert response.json() == {"ok": True}