from peewee import *

db = SqliteDatabase('data.db')


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    class Meta:
        db_table = 'all_users'

    first_name = CharField(max_length=30)
    second_name = CharField(max_length=30)
    third_name = CharField(max_length=30, null=True)
    specialization = CharField(max_length=30, null=True)
    mail = CharField(max_length=30)
    password = CharField()


User.create_table(db)
