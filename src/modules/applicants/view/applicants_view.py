from flask import Blueprint, jsonify
from flask_cors import cross_origin
from flask_pydantic import validate

from src.modules.auth.model.user_model import User

applicants_view = Blueprint('applicants', __name__, url_prefix="/applicants")


@applicants_view.route('/', methods=["GET"])
@cross_origin(supports_credentials=True)
@validate()
def get_applicants():
    applicants = User.select().where(User.is_tested)
    return jsonify({"applicants": list(applicants)})
