class CourierData:
    # Сообщения об ошибках
    ERROR_LOGIN_ALREADY_USED = "Этот логин уже используется. Попробуйте другой."
    ERROR_INSUFFICIENT_DATA = "Недостаточно данных"
    ERROR_ACCOUNT_NOT_FOUND = "Учетная запись не найдена"
    ERROR_GATEWAY_TIMEOUT = "Сервер вернул 504 Gateway Timeout"
    
    # Тестовые данные
    NONEXISTENT_LOGIN = "nonexistent_login_12345"
    NONEXISTENT_PASSWORD = "some_password"
    WRONG_LOGIN_PREFIX = "wrong_login"
    WRONG_PASSWORD_PREFIX = "wrong_password"


class OrderData:
    ORDER_DATA = {
        "firstName": "Иван",
        "lastName": "Петров",
        "address": "Москва, ул. Пушкина, д. 10",
        "metroStation": 1,
        "phone": "+79991234567",
        "rentTime": 5,
        "deliveryDate": "2025-04-10",
        "comment": "Позвонить за 10 минут"
    }

    COLOR_VARIANTS = [
        [],  # без цвета
        ["BLACK"],  # только BLACK
        ["GREY"],  # только GREY
        ["BLACK", "GREY"]  # оба цвета
    ]
    
    # Данные для дополнительных тестов
    TEST_ORDER_1 = {
        "firstName": "Иван",
        "lastName": "Петров",
        "address": "Москва",
        "metroStation": 1,
        "phone": "+79991234567",
        "rentTime": 5,
        "deliveryDate": "2025-04-10",
        "comment": "Тест"
    }
    
    TEST_ORDER_2 = {
        "firstName": "Тест",
        "lastName": "Тестов",
        "address": "Москва",
        "metroStation": 1,
        "phone": "+79991234567",
        "rentTime": 3,
        "deliveryDate": "2025-04-10",
        "comment": "Для теста"
    }