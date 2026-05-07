"""Responsável pela lógica de serviços ao usuário"""

from werkzeug.security import generate_password_hash
from config.database import get_db

from models.user_model import serialize_user

db = get_db()
users_col = db["users"]

def create_user(email, password, name, address, role="cliente"):
    """Função para criação de um novo usuário:    
    1- Verifica se email já existe
    2- Cria uma senha hash
    3- Coleta formulario
    4- Cria usuário
        Return: Mensagem de sucesso"""
    if users_col.find_one({"email": email}):
        return {"error": "Usuário já existe"}, 400

    hashed_pw = generate_password_hash(password)
    user = {
        "email": email,
        "password": hashed_pw,
        "name": name,
        "address": address,
        "role": role
    }
    users_col.insert_one(user)
    return {"message": "Usuário criado com sucesso"}, 201

def get_user_by_email(email):
    """Função para procurar de um usuário por email"""
    user = users_col.find_one({"email": email})
    if user:
        return serialize_user(user)
    return None

def update_user(email, name, address):
    """Função para atualizar o email de um usuário"""
    users_col.update_one(
        {"email": email},
        {"$set": {"name": name, "address": address}}
    )

def delete_user(email):
    """Função para deletar o email de um usuário"""
    users_col.delete_one({"email": email})
