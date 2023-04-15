from datetime import datetime, timedelta

from flask import Blueprint, jsonify
from flask_pydantic import validate
import jwt

from src.modules.auth.model.sign_in_request import SignInRequest
from src.modules.auth.model.sign_up_request import SignUpRequest
from src.modules.auth.model.user_model import User

auth_view = Blueprint('auth', __name__, url_prefix="/auth")


# Регистрация
@auth_view.route('/sign-up', methods=["POST"])
@validate()
def sign_up(body: SignUpRequest):
    # Тут нужно создать нового пользователя с определенной ролью и
    # сгенерить токен и отправить его на фронт

    User.create(
        first_name=body.first_name,
        second_name=body.second_name,
        third_name=body.second_name,
        role=body.role,
        mail=body.email,
        username=body.username,
        password=body.password
    ),

    token = create_token(User.id, User.username)
    return jsonify({"token": token, "role": User.role, "id": User.id})


@auth_view.route('/sign-in', methods=["POST"])
@validate()
def sign_in(body: SignInRequest):
    # Тут проверяем пароль, сравниваем с бд
    User.get().where(User.username == body.username)
    if body.password == User.password:
        return User.id

    # Генерим токен с данными о пользователе и отправляем на фронт вместе с ролью и айди

    token = create_token(User.id, User.username)
    return jsonify({"token": token, "role": User.role, "id": User.id})


@auth_view.route("/refresh", methods=["POST"])
@validate()
def refresh():
    from flask import request
    token = request.headers.get("Authorization").split(" ")[1]
    data = jwt.decode(token, "qwerty", algorithms="HS256")
    user = User.get(User.id == data.get("id"))
    token = create_token(user.id, user.username)
    return jsonify({"token": token, "role": user.role, "id": user.id, "exp": datetime.now() + timedelta(minutes=30)})


def create_token(user_id, username):
    token = jwt.encode(
        {
            "id": user_id,
            "username": username
        },
        "qwerty",
        algorithm="HS256")

    return token
