import requests


class TestOrdersList:
    
    def test_get_orders_list_returns_list(self, base_url):
        """Тест: в тело ответа возвращается список заказов"""
        response = requests.get(f'{base_url}/api/v1/orders')
        
        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)