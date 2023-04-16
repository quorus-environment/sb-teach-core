from flask import Blueprint, jsonify
from flask_cors import cross_origin

from src.modules.auth.model.user_model import User

applicants_view = Blueprint('applicants', __name__, url_prefix="/applicants")


@applicants_view.route('/', methods=["POST"])
@cross_origin(supports_credentials=True)
def get_applicants():
    applicants = User.select().where(User.is_tested).dicts()
    return jsonify({"applicants": [app for app in applicants]})
