import unittest
import os
import sys
from pymongo import MongoClient
from dotenv import load_dotenv

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.database import DatabaseConfig, get_db

class TestDatabaseConfig(unittest.TestCase):

    def setUp(self):
        """Configura o ambiente de test"""
        load_dotenv()

        self.client_data = MongoClient(os.getenv("MONGO_URI"))
        self.db = self.client_data["user_service_test"]

    def test_get_db(self):
        """Teste de retorno da instancia do banco de dados"""
        self.assertIsNotNone(self.db)

    def test_get_client(self):
        self.assertIsNotNone(self.client_data)

    def test_close_connection(self):
        self.assertIsNone(self.client_data.close())


# """Função para retornar a instancia do banco de dados"""
# def test_get_db():
#     db_config = TestDatabaseConfig()
#     db_instancia = db_config.test_get_db()
#     assert db_instancia is not None