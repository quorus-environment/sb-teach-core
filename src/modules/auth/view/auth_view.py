import os
from datetime import datetime, timedelta

from flask import Blueprint, jsonify
from flask_cors import cross_origin
from flask_pydantic import validate
import jwt
from peewee import DoesNotExist

from src.modules.auth.model.sign_in_request import SignInRequest
from src.modules.auth.model.sign_up_request import SignUpRequest
from src.modules.auth.model.user_model import User

auth_view = Blueprint('auth', __name__, url_prefix="/auth")


@auth_view.route('/sign-up', methods=["POST"])
@cross_origin(supports_credentials=True)
@validate()
def sign_up(body: SignUpRequest):
    User.create(
        first_name=body.first_name,
        second_name=body.last_name,
        third_name=body.second_name,
        role=body.role,
        mail=body.email,
        username=body.username,
        password=body.password
    )
    user = User.get(User.username == body.username)

    token = create_token(str(user.id), user.username)
    return jsonify({"token": token, "role": user.role, "id": str(user.id), "name": user.first_name + user.second_name,
                    "is_tested": user.is_tested, "spec": user.specializations})


@auth_view.route('/sign-in', methods=["POST"])
@cross_origin(supports_credentials=True)
@validate()
def sign_in(body: SignInRequest):
    try:
        user = User.get(User.username == body.username)
    except DoesNotExist:
        return "Unauthorized", 403
    if body.password != user.password:
        return "Unauthorized", 403

    token = create_token(str(user.id), user.username)
    return jsonify({"token": token, "role": user.role, "id": str(user.id), "name": user.first_name + user.second_name,
                    "is_tested": user.is_tested, "spec": user.specializations})


@auth_view.route("/refresh", methods=["POST"])
@cross_origin(supports_credentials=True)
@validate()
def refresh():
    from flask import request
    try:
        token = request.headers.get("Authorization").split(" ")[1]
    except AttributeError as e:
        return jsonify({"error": "Unauthorized"}), 403
    try:
        data = jwt.decode(token, os.environ.get("JWT_SECRET"), algorithms="HS256")
    except jwt.exceptions.ExpiredSignatureError:
        return jsonify({"error": "Unauthorized"}), 403
    try:
        user = User.get(User.id == data.get("id"))
    except DoesNotExist:
        return jsonify({"error": "Unauthorized"}), 403
    token = create_token(str(user.id), user.username)
    return jsonify({"token": token,
                    "role": user.role,
                    "id": user.id, "name": user.first_name + user.second_name,
                    "is_tested": user.is_tested, "spec": user.specializations})


def create_token(user_id, username):
    token = jwt.encode(
        {
            "id": user_id,
            "username": username,
            "exp": datetime.utcnow() + timedelta(hours=1)
        },
        os.environ.get("JWT_SECRET"),
        algorithm="HS256")

    return token
