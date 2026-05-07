import pytest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.user_model import serialize_user

def test_serializer_user():
    user = {
        "email":"teste@exemple.com",
        "name":"Teste Usuario",
        "address":"Rua Teste",
        "role":"cliente"
    }
    resultado = serialize_user(user)
    esperado = {
        "email":"teste@exemple.com",
        "name":"Teste Usuario",
        "address":"Rua Teste",
        "role":"cliente"
    }
    assert resultado == esperado

def test_serializer_user_incompleto():
    user = {
        "email":"teste@exemple.com"
    }
    resultado = serialize_user(user)
    esperado = {
        "email":"teste@exemple.com",
        "name":"",
        "address":"",
        "role":"cliente"
    }

    assert resultado == esperado

def test_serializer_user_vazio():
    user = {}
    resultado = serialize_user(user)
    esperado = {
        "email": None,
        "name": "",
        "address": "",
        "role": "cliente"
    }

    assert resultado == esperado

def test_serializer_user_integer():
    with pytest.raises(AttributeError):
        serialize_user(12345)

def test_serializer_user_string():
    with pytest.raises(AttributeError):
        serialize_user("Teste de string")