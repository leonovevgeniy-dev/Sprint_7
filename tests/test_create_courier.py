import pytest
import requests


class TestCreateCourier:
    
    def test_create_courier_success(self, base_url, random_courier_data):
        """Тест: курьера можно создать"""
        response = requests.post(
            f'{base_url}/api/v1/courier',
            data=random_courier_data
        )
        
        assert response.status_code == 201
        assert response.json() == {"ok": True}
    
    def test_create_duplicate_courier_fails(self, base_url, create_and_delete_courier):
        """Тест: нельзя создать двух одинаковых курьеров"""
        courier_data = create_and_delete_courier
        if not courier_data:
            pytest.skip("Не удалось создать курьера")
        
        payload = {
            "login": courier_data[0],
            "password": courier_data[1],
            "firstName": courier_data[2]
        }
        
        # Первый запрос уже создал курьера через фикстуру
        response = requests.post(f'{base_url}/api/v1/courier', data=payload)
        
        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."
    
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_missing_field_fails(self, base_url, random_courier_data, missing_field):
        """Тест: при отсутствии обязательного поля возвращается ошибка"""
        payload = random_courier_data.copy()
        del payload[missing_field]
        
        response = requests.post(f'{base_url}/api/v1/courier', data=payload)
        
        assert response.status_code == 400
        assert "Недостаточно данных" in response.json().get("message", "")
    
    def test_create_courier_without_firstname_success(self, base_url, random_courier_data):
        """Тест: можно создать курьера без firstName"""
        payload = {
            "login": random_courier_data["login"],
            "password": random_courier_data["password"]
        }
        
        response = requests.post(f'{base_url}/api/v1/courier', data=payload)
        
        assert response.status_code == 201
        assert response.json() == {"ok": True}