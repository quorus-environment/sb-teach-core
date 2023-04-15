from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from flask_pydantic import validate
from pydantic import BaseModel

from src.modules.auth.model.user_model import User
from src.modules.auth.model.user_token_data import UserTokenData
from src.utils.tokenized import tokenized, get_data_by_token

users_view = Blueprint('users', __name__, url_prefix="/users")


@users_view.route('/get_profile_info')
@cross_origin(supports_credentials=True)
@tokenized
def get_profile(data: UserTokenData):
    user = User.get(User.id == data.id)

    profile = {
        "id": data.id,
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.third_name,
        "second_name": user.second_name,
        "role": user.role,
        "image": user.avatar
    }

    return jsonify(profile)


class SaveAddInfoRequest(BaseModel):
    category: str
    framework: str
    about: str


@users_view.route('/save_additional_info', methods=["POST"])
@cross_origin(supports_credentials=True)
@validate()
def save_additional_info(body: SaveAddInfoRequest):
    token_data: UserTokenData = get_data_by_token()
    spec = ["frontend", "backend"] if body.category == "fullstack" else [body.category]
    try:
        User.get(User.id == token_data.id)
    except Exception as e:
        print(e)
        return "Unauthorized", 403
    User.update(specializations=spec, framework=body.framework, about=body.about).where(User.id == token_data.id)
    return "Saved successfully"

