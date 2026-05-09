import pytest
import requests
from unittest.mock import patch, Mock
from pymongo import MongoClient
import os
import sys
from dotenv import load_dotenv

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# load_dotenv()

# @pytest.fixture(scope="session")
# def mongo_client():
#     uri = os.getenv("MONGO_URI")
#     client = MongoClient(uri)
#     yield client
#     client.close()

# @pytest.fixture(scope="function")
# def test_db(mongo_client):
#     db = mongo_client["burguer_app_test"]

#     db["users"].delete_many({})  # Limpa a coleção de usuários antes de cada teste
#     db["pedidos"].delete_many({})  # Limpa a coleção de pedidos antes de cada teste
   
#     yield db


@pytest.fixture
def base_url():
    """Retorna a URL base da aplicação para os testes"""
    return {
        "auth_url":"http://localhost:5000/auth",
        "user_url":"http://localhost:5001/user",
        "order_url":"http://localhost:5002/order",
        "product_url":"http://localhost:5003/product"
        }

@pytest.fixture
def sample_user():
    """Retorna um usuário de exemplo para os testes"""
    return {
        "email":"cliente@teste.com",
        "password":"senha123",
        "name":"Cliente Teste",
        "address":"Rua Test, 123",
        "role":"cliente"
    }

@pytest.fixture
def sample_item():
    return {
        "item_name":["Hamburguer Teste", "Refrigerante Teste"],
        "item_price": [10.0, 5.0],
        "quantity": 2
    }

@pytest.fixture
def mock_user_service():
    with patch(requests.get) as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "email": "cliente@teste.com",
            "name":"Cliente Teste",
            "address":"Rua Test, 123",
            "role":"cliente"
        }
        mock_get.return_value = mock_response
        yield mock_get

@pytest.fixture
def mock_order_service():
    with patch(requests.post) as mock_post:
        mock_response = Mock()
        mock_response.status_code = 201
        mock_response.headers = {"Location": '/order/list'}
        mock_post.return_value = mock_response
        yield mock_post


def check_service_health(url):
    try:
        response = requests.get(f"{url}/", timeout=2)
        return response.status_code in [200,302,404]
    except requests.exceptions.ConnectionError:
        return False
    
add = 1