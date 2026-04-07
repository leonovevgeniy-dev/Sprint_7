import requests
import random
import string
from data.urls import Urls


def generate_random_string(length=10):
    """Генерирует случайную строку из букв нижнего регистра"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def register_new_courier_and_return_login_password():
    """Регистрирует нового курьера и возвращает список [login, password, first_name]"""
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(f'{Urls.BASE_URL}{Urls.COURIER_CREATE}', data=payload)

    if response.status_code == 201:
        return [login, password, first_name]
    return []


def delete_courier(courier_id):
    """Удаляет курьера по id"""
    return requests.delete(f'{Urls.BASE_URL}{Urls.COURIER_DELETE}{courier_id}')