from peewee import *
import uuid

from src.db import db


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    class Meta:
        db_table = 'all_users'
    id = UUIDField(primary_key=True, default=uuid.uuid4())
    first_name = CharField(max_length=30)
    second_name = CharField(max_length=30)
    third_name = CharField(max_length=30, null=True)
    role = CharField(max_length=30, null=True)
    mail = CharField(max_length=30)
    username = CharField(max_length=256)
    password = CharField(max_length=256)


User.create_table(db)
