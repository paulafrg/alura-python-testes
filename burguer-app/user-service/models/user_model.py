"""Serialização para retorno (removendo dados sensíveis)"""
def serialize_user(user):
    """Serializa os dados do usario:
        Returm:
            usuario do db
    """
    return {
        "email": user.get("email"),
        "name": user.get("name"),
        "address": user.get("address"),
        "role": user.get("role", "cliente")
    }
