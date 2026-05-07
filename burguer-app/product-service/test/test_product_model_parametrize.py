import os
import sys
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.product_model import serialize_product

@pytest.mark.parametrize("produto, esperado", [
    (
        {
            "_id":1,
        "name": "Produto Teste",
        "description": "Esta e a descricao de um produto teste",
        "category": "Teste",
        "price": "10.99",
        "available": "available",
        "ingredients": ["Sal", "Pimenta"]
        },
        {
            "id":"1",
        "name": "Produto Teste",
        "description": "Esta e a descricao de um produto teste",
        "category": "Teste",
        "price": "10.99",
        "available": "available",
        "ingredients": ["Sal", "Pimenta"]
        }
    ),
    (
        {
            "_id":1,
        "name": "Produto Teste",
        "description": "Esta e a descricao de um produto teste",
        "category": "Teste",
        "price": "10.99"
        },
        {
            "id":"1",
        "name": "Produto Teste",
        "description": "Esta e a descricao de um produto teste",
        "category": "Teste",
        "price": "10.99",
        "available": True,
        "ingredients": []
        }
    ),
    (
        {},
        {
            "id": "None",
        "name": None,
        "description": None,
        "category": None,
        "price": None,
        "available": True,
        "ingredients": []
        }
    )
])
def test_serializer_product_parametrizado(produto, esperado):
    resultado = serialize_product(produto)
    assert resultado == esperado

@pytest.mark.parametrize("entrada", [
    None,
    123456,
    "Teste de String",
    []
])
def test_serializer_product_parametrizado_excecao(entrada):
    with pytest.raises(AttributeError):
        serialize_product(entrada)