class CourierData:
    VALID_LOGIN = "valid_login"
    VALID_PASSWORD = "valid_password"
    VALID_FIRST_NAME = "John"
    INVALID_LOGIN = "nonexistent_login"
    INVALID_PASSWORD = "wrong_password"


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