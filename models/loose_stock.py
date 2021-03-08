import uuid
from models import db


class LooseStock(db.Model):
    __tablename__ = 'loosestock'

    id = db.Column(db.String(128), unique=True, primary_key=True, default=lambda: uuid.uuid4().hex)
    name = db.Column(db.String(128))
    weight = db.Column(db.Float())
    wastage = db.Column(db.Float())
    making_charge = db.Column(db.Float())
