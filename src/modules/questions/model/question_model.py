from peewee import Model, UUIDField, CharField, ForeignKeyField

from src.modules.auth.model.user_model import BaseModel
from src.modules.technology.model.technoloy_model import TechnologyModel


class QuestionModel(BaseModel):
    id = UUIDField(primary_key=True)
    title = CharField(max_length=30)
    image = CharField(max_length=256, null=True)
    answer = CharField(max_length=256)
    technology = ForeignKeyField(TechnologyModel, backref="questions")
