from flask import Flask
from flask_cors import CORS

from dotenv import load_dotenv

from src.db import db
from src.modules.applicants.view.applicants_view import applicants_view
from src.modules.auth.model.user_model import User
from src.modules.auth.view.auth_view import auth_view
from src.modules.auth.view.user_view import users_view
from src.modules.questions.model.question_model import QuestionModel
from src.modules.questions.view.questions_view import questions_view

from src.modules.technology.model.technology_model import TechnologyModel
from src.modules.technology.view.technology_view import technology_view

load_dotenv()
app = Flask(__name__)
CORS(app, supports_credentials=True)

if __name__ == "__main__":
    User.create_table()
    TechnologyModel.create_table()
    QuestionModel.create_table()

    app.register_blueprint(auth_view, url_prefix="/auth")
    app.register_blueprint(applicants_view, url_prefix="/applicants")
    app.register_blueprint(users_view, url_prefix="/users")
    app.register_blueprint(questions_view, url_prefix="/questions")
    app.register_blueprint(technology_view, url_prefix="/technology")

    app.run(port=8080)
