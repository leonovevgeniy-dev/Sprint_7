# Проект Sprint_7: Тестирование API Яндекс Самокат

## Описание
Автотесты для API сервиса "Яндекс Самокат".  
Проверяются ручки:
- Создание курьера (`/api/v1/courier`)
- Логин курьера (`/api/v1/courier/login`)
- Создание заказа (`/api/v1/orders`)
- Получение списка заказов (`/api/v1/orders`)
- (Дополнительно) Удаление курьера, принятие заказа, получение заказа по номеру

## Технологии
- Python 3.14
- pytest 8.3.3
- requests
- allure-pytest 2.13.5

# Установите зависимости
pip install -r requirements.txt

# Установите Allure

# Запуск тестов

# Все тесты
pytest -v

# С Allure отчетом
pytest --alluredir=allure-results
allure serve allure-results
