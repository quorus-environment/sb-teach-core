from flask import Blueprint, jsonify
from flask_cors import cross_origin

from src.modules.auth.model.user_model import User
from src.modules.auth.model.user_token_data import UserTokenData
from src.utils.tokenized import tokenized

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
