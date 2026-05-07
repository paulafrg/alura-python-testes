import os
import sys
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.user_model import serialize_user

@pytest.mark.parametrize("user, esperado",[
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
            "email":"test@exemple.com"
        },
        {
            "email":"test@exemple.com",
            "name":"",
            "address":"",
            "role":"cliente"
        }
    ),
    (
        {},
        {
            "email":None,
            "name":"",
            "address":"",
            "role":"cliente"
        }
    ),
    (
        {
            "email":None,
            "name":None,
            "address":None,
            "role":None
        },
        {
            "email":None,
            "name":None,
            "address":None,
            "role":None
        }
    ),
    (
        {
            "email":13456,
            "name":["Teste", "Usuario"],
            "address":{"rua": "abacaxi", "bairro": "frutas"},
            "role":True
        },
        {
            "email":13456,
            "name":["Teste", "Usuario"],
            "address":{"rua": "abacaxi", "bairro": "frutas"},
            "role":True
        }
    )
])

def test_serialize_user_paremetrizado(user, esperado):
    resuldado = serialize_user(user)
    assert resuldado == esperado

@pytest.mark.parametrize("entrada",[
    None,
    123456,
    "Teste de String",
    []
])

def test_serialize_user_parametrizado_exececao(entrada):
    with pytest.raises(AttributeError):
        serialize_user(entrada)