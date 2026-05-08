import pytest
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session")
def mongo_client():
    uri = os.getenv("MONGO_URI")
    client = MongoClient(uri)

    db = client["user_service_test"]
    yield db
    client.drop_database("user_service_test")
    client.close()
