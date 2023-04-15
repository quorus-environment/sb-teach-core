import uuid

from peewee import Model, UUIDField, CharField
from pydantic import BaseModel

from src.db import db


class TechnologyModel(Model):
    class Meta:
        database = db
        db_table = 'technology'
    id = UUIDField(primary_key=True, default=uuid.uuid4())
    title = CharField(max_length=256)
    category = CharField(max_length=256)
    color = CharField(max_length=256)


class SetTechnologyRequest(BaseModel):
    title: str
    color: str
    category: str
