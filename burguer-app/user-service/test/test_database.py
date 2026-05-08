import os
import sys
import pytest

from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))



def test_get_db():
    with patch("pymongo.MongoClient") as mock_client:
        mock_db = MagicMock()
        mock_client.return_value.__getitem__.return_value = mock_db

        from config.database import get_db

        with patch("config.database.client", mock_client.return_value):
            db_instance = get_db()
            assert db_instance is not None

@pytest.mark.usefixtures("mongo_client")
def test_get_db_email(mongo_client):
    # mock_db = mongo_client.MagicMock()
    # mock_db.usuarios.find_one.return_value = {"email": "teste@exemplo.com"} 
    # mongo_client.patch("config.database.db", mock_db) 

    # resultado = mock_db.usuarios.find_one({"email": "teste@exemplo.com"})
    # assert resultado["email"] == "teste@exemplo.com"

    user = {
        "email": "test@exemplo.com"
    }

    result = mongo_client["users"].insert_one(user)
    encontrado = mongo_client["users"].find_one({"_id":result.inserted_id})
    assert encontrado["email"] == user["email"]