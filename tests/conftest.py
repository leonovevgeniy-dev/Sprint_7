import pytest
import requests
import allure
from helpers.courier_helpers import register_new_courier_and_return_login_password, delete_courier
from data.urls import Urls


@pytest.fixture
def create_and_delete_courier():
    """Создаёт курьера перед тестом и удаляет после"""
    with allure.step('Создать нового курьера'):
        courier_data = register_new_courier_and_return_login_password()
    
    if not courier_data:
        pytest.skip("Не удалось создать курьера")
    
    yield courier_data

    with allure.step('Удалить курьера после теста'):
        if courier_data:
            login_response = requests.post(
                f'{Urls.BASE_URL}{Urls.COURIER_LOGIN}',
                data={"login": courier_data[0], "password": courier_data[1]}
            )
            if login_response.status_code == 200:
                courier_id = login_response.json().get("id")
                if courier_id:
                    delete_courier(courier_id)


@pytest.fixture
def random_courier_data():
    """Генерирует случайные данные для курьера"""
    from helpers.courier_helpers import generate_random_string

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    return {
        "login": login,
        "password": password,
        "firstName": first_name
    }