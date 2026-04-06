import pytest
import requests


class TestExtraTasks:
    
    def test_delete_courier_success(self, base_url, create_and_delete_courier):
        """Тест: успешное удаление курьера"""
        courier_data = create_and_delete_courier
        if not courier_data:
            pytest.skip("Не удалось создать курьера")
        
        # Получаем id курьера
        login_response = requests.post(
            f'{base_url}/api/v1/courier/login',
            data={"login": courier_data[0], "password": courier_data[1]}
        )
        courier_id = login_response.json().get("id")
        
        response = requests.delete(f'{base_url}/api/v1/courier/{courier_id}')
        
        assert response.status_code == 200
        assert response.json() == {"ok": True}
    
    def test_delete_courier_without_id_fails(self, base_url):
        """Тест: удаление курьера без id возвращает ошибку"""
        response = requests.delete(f'{base_url}/api/v1/courier/')
        
        assert response.status_code == 404
    
    def test_accept_order_success(self, base_url, create_and_delete_courier):
        """Тест: успешное принятие заказа"""
        # Сначала создаём заказ
        order_data = {
            "firstName": "Иван",
            "lastName": "Петров",
            "address": "Москва",
            "metroStation": 1,
            "phone": "+79991234567",
            "rentTime": 5,
            "deliveryDate": "2025-04-10",
            "comment": "Тест"
        }
        
        order_response = requests.post(f'{base_url}/api/v1/orders', json=order_data)
        track = order_response.json().get("track")
        
        # Получаем id заказа по track
        orders_response = requests.get(f'{base_url}/api/v1/orders/track?t={track}')
        order_id = orders_response.json().get("order", {}).get("id")
        
        # Получаем id курьера
        courier_data = create_and_delete_courier
        login_response = requests.post(
            f'{base_url}/api/v1/courier/login',
            data={"login": courier_data[0], "password": courier_data[1]}
        )
        courier_id = login_response.json().get("id")
        
        response = requests.put(
            f'{base_url}/api/v1/orders/accept/{order_id}',
            params={"courierId": courier_id}
        )
        
        assert response.status_code == 200
        assert response.json() == {"ok": True}
    
    def test_get_order_by_track_success(self, base_url):
        """Тест: получение заказа по его номеру (track)"""
        # Создаём заказ
        order_data = {
            "firstName": "Тест",
            "lastName": "Тестов",
            "address": "Москва",
            "metroStation": 1,
            "phone": "+79991234567",
            "rentTime": 3,
            "deliveryDate": "2025-04-10",
            "comment": "Для теста"
        }
        
        create_response = requests.post(f'{base_url}/api/v1/orders', json=order_data)
        track = create_response.json().get("track")
        
        response = requests.get(f'{base_url}/api/v1/orders/track?t={track}')
        
        assert response.status_code == 200
        assert "order" in response.json()