from flask import Blueprint, jsonify
from flask_pydantic import validate
import sqlite3
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
                third_name=body.third_name,
                role=body.role,
                mail=body.mail,
                username=body.username,
                password=body.password
            ),

    token = jwt.encode(
        {
            "id": User.id,
            "username": User.username
        },
        "qwerty",
        algorithm="HS256")
    return jsonify({"token": token})


@auth_view.route('/sign-in', methods=["POST"])
@validate()
def sign_in(body: SignInRequest):

    # Тут проверяем пароль, сравниваем с бд
    User.get().where(User.username == body.username)
    if body.password == User.password:
        return User.id

    # Генерим токен с данными о пользователе и отправляем на фронт вместе с ролью и айди
    token = jwt.encode(
        {
            "id": User.id,
            "username": User.username
        },
        "qwerty",
        algorithm="HS256")

    return jsonify({"token": token})
