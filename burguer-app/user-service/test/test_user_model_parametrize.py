import os
import sys
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.user_model import serialize_user

@pytest.mark.parametrize("user, esperado", [
    (
        {
            "email":"teste@exemple.com",
        "name":"Teste Usuario",
        "address":"Rua Teste",
        "role":"cliente"
        },
        {
            "email":"teste@exemple.com",
        "name":"Teste Usuario",
        "address":"Rua Teste",
        "role":"cliente"
        }
    ),
    (
        {
            "email":"teste@exemple.com"
        },
        {
            "email":"teste@exemple.com",
        "name":None,
        "address":None,
        "role":"cliente"
        }
    ),
    (
        {},
        {
            "email": None,
        "name": None,
        "address": None,
        "role": "cliente"
        }
    )
])
def test_serializado_user_parametrizado(user,esperado):
    resultado = serialize_user(user)
    assert resultado == esperado

@pytest.mark.parametrize("entrada", [
    123456,
    "Teste de String",
    [],
    None
])
def test_serializado_user_parametrizado_excecao(entrada):
    with pytest.raises(AttributeError):
        serialize_user(entrada)