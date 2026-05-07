"""User Controller to handle user return to Burguer App"""

from flask import Blueprint, request, render_template, redirect, url_for, flash
from services.user_service import create_user, get_user_by_email, update_user, delete_user

user_bp = Blueprint("user", __name__)

@user_bp.route("/create", methods=["GET", "POST"])
def create():
    """Endpoint de criaçao de usuário"""
    if request.method == "POST":
        data = request.form
        response, status = create_user(
            email=data["email"],
            password=data["password"],
            name=data["name"],
            address=data["address"],
            role=data.get("role", "cliente")
        )
        if status != 201:
            flash(response["error"])
            return redirect(url_for("user.create"))
        flash("Usuário criado com sucesso! Faça login para continuar.")
        # Redirect to auth-service login after successful registration
        return redirect("http://localhost:5000/auth/login")
    return render_template("create.html")

@user_bp.route("/profile/<email>")
def profile(email):
    """Endpoint para procurar de um usuário por email"""
    user = get_user_by_email(email)
    if not user:
        return "Usuário não encontrado", 404
    return render_template("profile.html", user=user)

@user_bp.route("/edit/<email>", methods=["GET", "POST"])
def edit(email):
    """Endpoint de edição de um usuário por email"""
    user = get_user_by_email(email)
    if request.method == "POST":
        name = request.form["name"]
        address = request.form["address"]
        update_user(email, name, address)
        flash("Perfil atualizado com sucesso.")
        return redirect(url_for("user.profile", email=email))
    return render_template("edit.html", user=user)

@user_bp.route("/delete/<email>", methods=["POST"])
def delete(email):
    """Endpoint de deletar de um usuário por email"""
    delete_user(email)
    flash("Usuário excluído com sucesso.")
    return redirect(url_for("user.create"))
