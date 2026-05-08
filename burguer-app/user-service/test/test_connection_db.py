import pytest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

@pytest.mark.usefixtures("mongo_client")
def test_conexao_com_banco(mongo_client):
    resultado = mongo_client.list_collection_names()
    assert isinstance(resultado, list)