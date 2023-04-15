import uuid

from flask import Blueprint, jsonify
from flask_cors import cross_origin
from flask_pydantic import validate

from src.modules.questions.model.question_model import QuestionModel
from src.modules.technology.model.technology_model import SetTechnologyRequest, TechnologyModel

technology_view = Blueprint('technology', __name__, url_prefix="/technology")


@technology_view.route('/', methods=["POST"])
@cross_origin(supports_credentials=True)
@validate()
def set_technology(body: SetTechnologyRequest):
    try:
        tech_model = TechnologyModel(
            id=uuid.uuid4(),
            title=body.title,
            color=body.color,
            category=body.category
        )
        tech_model.save(force_insert=True)

    except Exception as e:
        print(e)
        return "Internal Server Error", 500
    return jsonify({"status": "done"})


@technology_view.route('/get_technologies', methods=["GET"])
@cross_origin(supports_credentials=True)
def get_technology():
    return jsonify({"technologies": [tech for tech in TechnologyModel.select().dicts()]})
