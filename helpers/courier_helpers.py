import requests
import random
import string


def generate_random_string(length=10):
    """Генерирует случайную строку из букв нижнего регистра"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def register_new_courier_and_return_login_password(base_url):
    """Регистрирует нового курьера и возвращает список [login, password, first_name]"""
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(f'{base_url}/api/v1/courier', data=payload)

    if response.status_code == 201:
        return [login, password, first_name]
    return []


def delete_courier(base_url, courier_id):
    """Удаляет курьера по id"""
    return requests.delete(f'{base_url}/api/v1/courier/{courier_id}')