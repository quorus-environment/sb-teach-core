import uuid

from flask import Blueprint, jsonify
from flask_cors import cross_origin
from flask_pydantic import validate
from peewee import fn

from src.modules.auth.model.user_token_data import UserTokenData
from src.modules.questions.model.get_questions_request import GetQuestionsRequest, SetQuestionRequest
from src.modules.questions.model.question_model import QuestionModel
from src.utils.tokenized import tokenized

questions_view = Blueprint('questions', __name__, url_prefix="/questions")


@questions_view.route('/get_questions', methods=["GET"])
@validate()
@tokenized
def get_questions(data: UserTokenData, body: GetQuestionsRequest):
    questions = QuestionModel.select().where(QuestionModel.technology == body.technology)
    return questions


@questions_view.route('/get_question_set', methods=["GET"])
@validate()
@tokenized
def get_question_set(data: UserTokenData, body: GetQuestionsRequest):
    question_set = QuestionModel.select().where(QuestionModel.technology == body.technology).order_by(fn.Rand()).limit(15)
    return question_set


@questions_view.route('/set_question', methods=["POST"])
@cross_origin(supports_credentials=True)
@validate()
def set_question(body: SetQuestionRequest):
    try:
        question_model = QuestionModel(
            id=uuid.uuid4(),
            title=body.title,
            answer=body.answer,
            answers=body.answers,
            technology=body.technology
        )
        question_model.save(force_insert=True)

    except Exception as e:
        print(e)
        return "Internal Server Error", 500
    return jsonify({"status": "done"})
