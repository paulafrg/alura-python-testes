import pytest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.product_model import serialize_product

def test_serializer_product_completo():
    produto = {
        "_id":1,
        "name": "Produto Teste",
        "description": "Esta e a descricao de um produto teste",
        "category": "Teste",
        "price": "10.99",
        "available": "available",
        "ingredients": ["Sal", "Pimenta"]
    }
    resultado = serialize_product(produto)
    esperado = {
        "id":"1",
        "name": "Produto Teste",
        "description": "Esta e a descricao de um produto teste",
        "category": "Teste",
        "price": "10.99",
        "available": "available",
        "ingredients": ["Sal", "Pimenta"]
    }

    assert resultado == esperado

def test_serializer_product_aplicar_valores_padrao():
    produto = {
        "_id":1,
        "name": "Produto Teste",
        "description": "Esta e a descricao de um produto teste",
        "category": "Teste",
        "price": "10.99"
    }
    resultado = serialize_product(produto)
    esperado = {
        "id":"1",
        "name": "Produto Teste",
        "description": "Esta e a descricao de um produto teste",
        "category": "Teste",
        "price": "10.99",
        "available": True,
        "ingredients": []
    }

    assert resultado == esperado

def test_serialize_produto_vazio():
    produto = {}
    resultado = serialize_product(produto)
    esperado = {
        "id": "None",
        "name": None,
        "description": None,
        "category": None,
        "price": None,
        "available": True,
        "ingredients": []
    }

    assert resultado == esperado

def test_serialize_produto_inteiro():
    with pytest.raises(AttributeError):
        serialize_product(13456)