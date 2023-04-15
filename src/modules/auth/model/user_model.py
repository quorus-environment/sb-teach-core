from peewee import *
import uuid

from playhouse.postgres_ext import ArrayField, TextField

from src.db import db


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    class Meta:
        db_table = 'users'

    id = UUIDField(primary_key=True, default=uuid.uuid4())
    first_name = CharField(max_length=30)
    second_name = CharField(max_length=30)
    third_name = CharField(max_length=30, null=True)
    role = CharField(max_length=30, null=True)

    specializations = ArrayField(TextField, default=[])
    is_tested = BooleanField(default=False)

    mail = CharField(max_length=30)
    username = CharField(max_length=256)
    password = CharField(max_length=256)
    avatar = CharField(max_length=256, null=True)


User.create_table()