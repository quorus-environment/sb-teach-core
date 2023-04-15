import uuid

from peewee import Model, UUIDField, CharField

from src.modules.auth.model.user_model import BaseModel


class TechnologyModel(BaseModel):
    class Meta:
        db_table = 'technology'
    id = UUIDField(primary_key=True, default=uuid.uuid4())
    title = CharField(max_length=256)
    color = CharField(max_length=256)

