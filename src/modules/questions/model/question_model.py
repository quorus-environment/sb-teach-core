from peewee import Model, UUIDField, CharField, ForeignKeyField

from src.modules.technology.model.technoloy_model import TechnologyModel


class QuestionModel(Model):
    id = UUIDField(primary_key=True)
    title = CharField(max_length=30)
    image = CharField(null=True)
    answer = CharField()
    technology = ForeignKeyField(TechnologyModel, backref="questions")
