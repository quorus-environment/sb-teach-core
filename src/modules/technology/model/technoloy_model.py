from peewee import Model, UUIDField, CharField

from src.modules.auth.model.user_model import BaseModel


class TechnologyModel(BaseModel):
    id = UUIDField(primary_key=True)
    title = CharField(max_length=256)
    color = CharField(max_length=256)

