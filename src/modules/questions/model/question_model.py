import uuid

from peewee import Model, UUIDField, CharField, ForeignKeyField

from src.modules.auth.model.user_model import BaseModel
from src.modules.technology.model.technology_model import TechnologyModel


class QuestionModel(BaseModel):
    class Meta:
        db_table = 'questions'

    id = UUIDField(primary_key=True, default=uuid.uuid4())
    title = CharField(max_length=30)
    image = CharField(max_length=256, null=True)
    answer = CharField(max_length=256)
    technology = ForeignKeyField(TechnologyModel, backref="questions")
