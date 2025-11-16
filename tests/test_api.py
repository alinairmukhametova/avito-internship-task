import requests
import pytest
import random

BASE_URL = "https://qa-internship.avito.com"

class TestAvitoAPI:
    
    def setup_method(self):
        self.seller_id = random.randint(111111, 999999)
        self.item_data = {
            "sellerID": self.seller_id,
            "name": "Тестовое объявление",
            "price": 1000,
            "statistics": {
                "likes": 5,
                "viewCount": 100,
                "contacts": 3
            }
        }
        self.created_item_id = None
    
    def test_create_item_success(self):
        response = requests.post(f"{BASE_URL}/api/1/item", json=self.item_data)
        assert response.status_code == 200
        response_data = response.json()
        assert "id" in response_data
        assert response_data["sellerId"] == self.item_data["sellerID"]
        assert response_data["name"] == self.item_data["name"]
        self.created_item_id = response_data["id"]
    
    def test_get_item_by_id(self):
        create_response = requests.post(f"{BASE_URL}/api/1/item", json=self.item_data)
        item_id = create_response.json()["id"]
        response = requests.get(f"{BASE_URL}/api/1/item/{item_id}")
        assert response.status_code == 200
        item_data = response.json()
        assert isinstance(item_data, list)
        assert len(item_data) > 0
        assert item_data[0]["id"] == item_id
    
    def test_get_nonexistent_item(self):
        response = requests.get(f"{BASE_URL}/api/1/item/nonexistent_id_12345")
        assert response.status_code == 404
    
    def test_get_seller_items(self):
        requests.post(f"{BASE_URL}/api/1/item", json=self.item_data)
        response = requests.get(f"{BASE_URL}/api/1/{self.seller_id}/item")
        assert response.status_code == 200
        items = response.json()
        assert isinstance(items, list)
        seller_items = [item for item in items if item["sellerId"] == self.seller_id]
        assert len(seller_items) > 0
    
    def test_create_item_missing_required_fields(self):
        invalid_data = {
            "sellerID": self.seller_id,
            "price": 1000,
            "statistics": {
                "likes": 5,
                "viewCount": 100,
                "contacts": 3
            }
        }
        response = requests.post(f"{BASE_URL}/api/1/item", json=invalid_data)
        assert response.status_code == 400

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
