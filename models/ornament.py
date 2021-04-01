import uuid
import logging
import datetime
from models import db

LOG = logging.getLogger(__name__)



class Ornament(db.Model):

    __tablename__ = 'ornament'

    id = db.Column(db.String(128), unique=True, primary_key=True, default=lambda: uuid.uuid4().hex)
    name = db.Column(db.String(128))
    weight = db.Column(db.Float())
    wastage = db.Column(db.Float())
    making_charge = db.Column(db.Float())
    category_id = db.Column(db.String(128))

    def __init__(
            self,
            name,
            weight,
            wastage,
            making_charge,
            category_id
    ):
        self.name = name
        self.weight = weight
        self.wastage = wastage
        self.making_charge = making_charge
        self.category_id = category_id

    @staticmethod
    def add_stock(
            name,
            weight,
            wastage,
            making_charge,
            category_id
    ):
        ornament = Ornament(
            name=name,
            weight=weight,
            wastage=wastage,
            making_charge=making_charge,
            category_id=category_id
        )
        db.session.add(ornament)
        db.session.commit()

    @staticmethod
    def get_all_ornaments():
        ornaments = Ornament.query.all()
        return ornaments

    @staticmethod
    def get_ornament_by_id(_id):
        ornaments = Ornament.query.get(_id)
        return ornaments

    @staticmethod
    def modify_ornament(
            _id,
            name,
            weight,
            wastage,
            making_charge,
            category_id
    ):
        ornament = Ornament.query.get(_id)
        ornament.name = name
        ornament.weight = weight
        ornament.wastage = wastage
        ornament.making_charge = making_charge
        ornament.category_id = category_id
        db.session.commit()

    @staticmethod
    def delete_ornament(_id):
        ornament = Ornament.query.get(_id)
        db.session.delete(ornament)
        db.session.commit()

