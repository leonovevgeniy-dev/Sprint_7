import pytest
import requests
from data.test_data import OrderData


class TestCreateOrder:
    
    @pytest.mark.parametrize("color", OrderData.COLOR_VARIANTS)
    def test_create_order_with_different_colors(self, base_url, color):
        """Тест: создание заказа с разными вариантами цветов"""
        order_data = OrderData.ORDER_DATA.copy()
        order_data["color"] = color
        
        response = requests.post(f'{base_url}/api/v1/orders', json=order_data)
        
        assert response.status_code == 201
        assert "track" in response.json()
        assert isinstance(response.json()["track"], int)
    
    def test_create_order_without_color_success(self, base_url):
        """Тест: можно создать заказ без указания цвета"""
        order_data = OrderData.ORDER_DATA.copy()
        order_data["color"] = []
        
        response = requests.post(f'{base_url}/api/v1/orders', json=order_data)
        
        assert response.status_code == 201
        assert "track" in response.json()