from peewee import Model, UUIDField, CharField


class TechnologyModel(Model):
    id = UUIDField(primary_key=True)
    title = CharField()
    color = CharField()

