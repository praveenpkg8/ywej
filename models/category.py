import uuid
import datetime
from models import db


class Category(db.Model):

    __tablename__ = 'category'

    id = db.Column(db.String(128), unique=True, primary_key=True, default=lambda: uuid.uuid4().hex)
    name = db.Column(db.String(128))
    material = db.Column(db.String(128))

    def __init__(
            self,
            name,
            material
    ):
        self.name = name
        self.material = material

    @staticmethod
    def create_category(
            name,
            material
    ):
        category = Category(
            name=name,
            material=material
        )
        db.session.add(category)
        db.session.commit()

    @staticmethod
    def get_all_category():
        category = Category.query.all()
        return category

    @staticmethod
    def get_category_by_id(category_id):
        category = Category.query.get(category_id)
        return category

    @staticmethod
    def modify_ornament(
            _id,
            name,
            material
    ):
        ornament = Category.query.get(_id)
        ornament.name = name
        ornament.material = material
        db.session.commit()

    @staticmethod
    def delete_category(_id):
        ornament = Category.query.get(_id)
        db.session.delete(ornament)
        db.session.commit()
