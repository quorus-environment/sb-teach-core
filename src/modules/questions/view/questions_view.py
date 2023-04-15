from flask import Blueprint
from flask_pydantic import validate

from src.modules.auth.model.user_token_data import UserTokenData
from src.modules.questions.model.get_questions_request import GetQuestionsRequest
from src.modules.questions.model.question_model import QuestionModel
from src.utils.tokenized import tokenized

questions_view = Blueprint('questions', __name__, url_prefix="/questions")


@questions_view.route('/get_questions', methods=["GET"])
@validate()
@tokenized
def get_questions(body: GetQuestionsRequest):
    questions = QuestionModel.select().where(QuestionModel.technology == body.technology)
    return questions
