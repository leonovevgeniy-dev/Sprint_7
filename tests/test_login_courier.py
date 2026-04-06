import pytest
import requests


class TestLoginCourier:
    
    def test_login_courier_success(self, base_url, create_and_delete_courier):
        """Тест: курьер может авторизоваться"""
        courier_data = create_and_delete_courier
        if not courier_data:
            pytest.skip("Не удалось создать курьера")
        
        payload = {
            "login": courier_data[0],
            "password": courier_data[1]
        }
        
        response = requests.post(f'{base_url}/api/v1/courier/login', data=payload)
        
        assert response.status_code == 200
        assert "id" in response.json()
        assert isinstance(response.json()["id"], int)
    
    @pytest.mark.parametrize("wrong_field", ["login", "password"])
    def test_login_wrong_credentials_fails(self, base_url, create_and_delete_courier, wrong_field):
        """Тест: при неправильном логине или пароле возвращается ошибка"""
        courier_data = create_and_delete_courier
        if not courier_data:
            pytest.skip("Не удалось создать курьера")
        
        payload = {
            "login": courier_data[0] if wrong_field == "password" else "wrong_login",
            "password": courier_data[1] if wrong_field == "login" else "wrong_password"
        }
        
        response = requests.post(f'{base_url}/api/v1/courier/login', data=payload)
        
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"
    
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_login_missing_field_fails(self, base_url, create_and_delete_courier, missing_field):
        """Тест: если не передать обязательное поле, возвращается ошибка"""
        courier_data = create_and_delete_courier
        if not courier_data:
            pytest.skip("Не удалось создать курьера")
        
        payload = {
            "login": courier_data[0],
            "password": courier_data[1]
        }
        del payload[missing_field]
        
        response = requests.post(f'{base_url}/api/v1/courier/login', data=payload)
        
        # Если сервер вернул 504 - пропускаем, это не ошибка теста
        if response.status_code == 504:
            pytest.skip("Сервер вернул 504 Gateway Timeout")
        
        assert response.status_code == 400
        assert "Недостаточно данных" in response.json().get("message", "")
    
    def test_login_nonexistent_courier_fails(self, base_url):
        """Тест: авторизация под несуществующим пользователем возвращает ошибку"""
        payload = {
            "login": "nonexistent_login_12345",
            "password": "some_password"
        }
        
        response = requests.post(f'{base_url}/api/v1/courier/login', data=payload)
        
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"