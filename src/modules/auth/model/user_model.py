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
    framework = CharField(max_length=128, null=True)
    about = CharField(max_length=256, null=True)
    is_tested = BooleanField(default=False)

    education = CharField(max_length=256, null=True)
    vuz = CharField(max_length=256, null=True)
    experience = CharField(max_length=256, null=True)
    github_link = CharField(max_length=256, null=True)
    birthday = CharField(max_length=256, null=True)
    city = CharField(max_length=256, null=True)

    invitations = ArrayField(CharField, default=[], null=True)
    rating = IntegerField(default=0, null=True)

    mail = CharField(max_length=64, null=True)
    username = CharField(max_length=256)
    password = CharField(max_length=256)
    avatar = CharField(max_length=256, null=True)
