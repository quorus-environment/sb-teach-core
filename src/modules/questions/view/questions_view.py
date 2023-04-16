import uuid

from flask import Blueprint, jsonify
from flask_cors import cross_origin
from flask_pydantic import validate
from random import shuffle
from peewee import fn
from pydantic import BaseModel

from src.modules.auth.model.user_model import User
from src.modules.auth.model.user_token_data import UserTokenData
from src.modules.questions.model.get_questions_request import GetQuestionsRequest, SetQuestionRequest
from src.modules.questions.model.question_model import QuestionModel
from src.utils.tokenized import tokenized, get_data_by_token

questions_view = Blueprint('questions', __name__, url_prefix="/questions")


@questions_view.route('/get_questions', methods=["GET"])
@validate()
@tokenized
def get_questions(data: UserTokenData, body: GetQuestionsRequest):
    questions = QuestionModel.select().where(QuestionModel.technology == body.technology)
    return questions


@questions_view.route('/get_question_set', methods=["POST"])
@cross_origin(supports_credentials=True)
@validate()
def get_question_set(body: GetQuestionsRequest):
    question_set = QuestionModel.select().where(QuestionModel.technology == body.technology).limit(15).dicts()
    arr = [q for q in question_set]
    shuffle(arr)
    return jsonify({"questions": arr})




class QuestionToValid(BaseModel):
    uuid: str
    answer: int


class ValidateRequest(BaseModel):
    answers: list[QuestionToValid]


@questions_view.route('/get_question_by_tech', methods=["POST"])
@cross_origin(supports_credentials=True)
@validate()
def get_question_by_tech(body: GetQuestionsRequest):
    questions = QuestionModel.select().where(QuestionModel.technology == body.technology).dicts()
    return jsonify({"questions": [q for q in questions]})

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


@questions_view.route('/validate_question', methods=["POST"])
@cross_origin(supports_credentials=True)
@validate()
def validate(body: ValidateRequest):
    token_data = get_data_by_token()
    try:
        correct = 0
        for question in body.answers:
            if str(question.answer) == str(QuestionModel.get(QuestionModel.id == question.uuid).answer):
                correct += 1
                continue
            else:
                continue
        User.update(rating=correct / len(body.answers) * 100, is_tested=True).where(User.id == token_data.get("id")).execute()
        return jsonify({"rating": correct / len(body.answers) * 100})
    except Exception as e:
        print(e)
        return "Internal Server Error", 500




