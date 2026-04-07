import pytest
import requests
import allure
from data.urls import Urls
from data.test_data import CourierData


class TestLoginCourier:

    @allure.title('Логин курьера: успешная авторизация возвращает 200 и id')
    def test_login_courier_success(self, create_and_delete_courier):
        courier_data = create_and_delete_courier

        payload = {
            "login": courier_data[0],
            "password": courier_data[1]
        }

        with allure.step('Отправить POST-запрос на авторизацию'):
            response = requests.post(f'{Urls.BASE_URL}{Urls.COURIER_LOGIN}', data=payload)

        with allure.step('Проверить статус-код 200'):
            assert response.status_code == 200

        with allure.step('Проверить наличие id в ответе'):
            assert "id" in response.json()

        with allure.step('Проверить что id - целое число'):
            assert isinstance(response.json()["id"], int)

    @allure.title('Логин курьера: неправильный логин или пароль возвращает 404')
    @pytest.mark.parametrize("wrong_field", ["login", "password"])
    def test_login_wrong_credentials_fails(self, create_and_delete_courier, wrong_field):
        courier_data = create_and_delete_courier

        payload = {
            "login": courier_data[0] if wrong_field == "password" else CourierData.WRONG_LOGIN_PREFIX,
            "password": courier_data[1] if wrong_field == "login" else CourierData.WRONG_PASSWORD_PREFIX
        }

        with allure.step(f'Отправить POST-запрос с неправильным {wrong_field}'):
            response = requests.post(f'{Urls.BASE_URL}{Urls.COURIER_LOGIN}', data=payload)

        with allure.step('Проверить статус-код 404'):
            assert response.status_code == 404

        with allure.step('Проверить сообщение об ошибке'):
            assert response.json()["message"] == CourierData.ERROR_ACCOUNT_NOT_FOUND

    @allure.title('Логин курьера: отсутствие обязательного поля возвращает 400')
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_login_missing_field_fails(self, create_and_delete_courier, missing_field):
        courier_data = create_and_delete_courier

        payload = {
            "login": courier_data[0],
            "password": courier_data[1]
        }
        del payload[missing_field]

        with allure.step(f'Отправить POST-запрос без поля {missing_field}'):
            response = requests.post(f'{Urls.BASE_URL}{Urls.COURIER_LOGIN}', data=payload)

        with allure.step('Проверить статус-код 400'):
            assert response.status_code == 400

        with allure.step('Проверить сообщение об ошибке'):
            assert CourierData.ERROR_INSUFFICIENT_DATA in response.json().get("message", "")

    @allure.title('Логин курьера: несуществующий пользователь возвращает 404')
    def test_login_nonexistent_courier_fails(self):
        payload = {
            "login": CourierData.NONEXISTENT_LOGIN,
            "password": CourierData.NONEXISTENT_PASSWORD
        }

        with allure.step('Отправить POST-запрос с несуществующим логином'):
            response = requests.post(f'{Urls.BASE_URL}{Urls.COURIER_LOGIN}', data=payload)

        with allure.step('Проверить статус-код 404'):
            assert response.status_code == 404

        with allure.step('Проверить сообщение об ошибке'):
            assert response.json()["message"] == CourierData.ERROR_ACCOUNT_NOT_FOUND