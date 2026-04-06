import pytest
import requests
from helpers.courier_helpers import register_new_courier_and_return_login_password, delete_courier


class Config:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'


@pytest.fixture
def base_url():
    return Config.BASE_URL


@pytest.fixture
def create_and_delete_courier(base_url):
    """Создаёт курьера перед тестом и удаляет после"""
    courier_data = register_new_courier_and_return_login_password(base_url)
    yield courier_data
    
    # Удаление курьера после теста (для доп. задания)
    if courier_data:
        # Получаем id курьера через логин
        login_response = requests.post(
            f'{base_url}/api/v1/courier/login',
            data={"login": courier_data[0], "password": courier_data[1]}
        )
        if login_response.status_code == 200:
            courier_id = login_response.json().get("id")
            if courier_id:
                delete_courier(base_url, courier_id)


@pytest.fixture
def random_courier_data(base_url):
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