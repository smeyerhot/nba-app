from .db import db

class Player(db.Document):
    name = db.StringField(required=True)
    teams = db.ListField(required=True)
    positions = db.ListField(required=True)
    championships = db.IntField(required=True)

    