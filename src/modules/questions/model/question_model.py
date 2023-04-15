import uuid

from peewee import Model, UUIDField, CharField, ForeignKeyField
from playhouse.postgres_ext import ArrayField

from src.modules.auth.model.user_model import BaseModel
from src.modules.technology.model.technology_model import TechnologyModel


class QuestionModel(BaseModel):
    class Meta:
        db_table = 'questions'

    id = UUIDField(primary_key=True, default=uuid.uuid4())
    title = CharField(max_length=512)
    image = CharField(max_length=256, null=True)
    answer = CharField(max_length=256)
    answers = ArrayField(CharField, default=[])
    technology = ForeignKeyField(TechnologyModel, backref="questions")
