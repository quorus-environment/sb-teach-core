from flask import Blueprint, jsonify

auth_view = Blueprint('auth', __name__, url_prefix="/auth")

# Регистрация
@auth_view.route('/sign-in', methods=["POST"])
def sign_in():
    # Тут нужно создать нового пользователя с определенной ролью и
    # сгенерить токен и отправить его на фронт
    return jsonify({"token": "token"})

@auth_view.route('/sign-up', methods=["POST"])
def sign_up():
    # Тут проверяем пароль, сравниваем с бд
    # Генерим токен с данными о пользователе и отправляем на фронт вместе с ролью и айди
    return jsonify({"token": "token"})
