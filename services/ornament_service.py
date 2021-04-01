import logging

from models.ornament import Ornament
from models.category import Category

LOG = logging.getLogger(__name__)


class OrnamentService:

    @staticmethod
    def create_ornament(params):
        name = params.get('name')
        weight = params.get('weight')
        wastage = params.get('wastage')
        making_charge = params.get('making_charge')
        category_id = params.get('category_id')
        Ornament.add_stock(
            name=name,
            weight=weight,
            wastage=wastage,
            making_charge=making_charge,
            category_id=category_id
        )

    @staticmethod
    def get_ornament_by_id(_id):
        ornament = Ornament.get_ornament_by_id(_id=_id)
        category = Category.get_category_by_id(category_id=ornament.category_id)
        ornament_dict = dict(
            id=ornament.id,
            name=ornament.name,
            weight=ornament.weight,
            wastage=ornament.wastage,
            making_charge=ornament.making_charge,
            category_id=ornament.category_id,
            category_name=category.name,
            category_material=category.material
        )
        return ornament_dict

    @staticmethod
    def get_all_ornaments():
        ornaments = Ornament.get_all_ornaments()
        data = []
        for ornament in ornaments:
            category = Category.get_category_by_id(category_id=ornament.category_id)
            ornament_dict = dict(
                id=ornament.id,
                name=ornament.name,
                weight=ornament.weight,
                wastage=ornament.wastage,
                making_charge=ornament.making_charge,
                category_id=ornament.category_id,
                category_name=category.name,
                category_material=category.material
            )
            data.append(ornament_dict)
        return data

    @staticmethod
    def update_ornaments(ornament):
        Ornament.modify_ornament(
            _id=ornament.get('id'),
            name=ornament.get('name'),
            weight=ornament.get('weight'),
            wastage=ornament.get('wastage'),
            making_charge=ornament.get('making_charge'),
            category_id=ornament.get('category_id'),
        )

    @staticmethod
    def delete_ornament(_id):
        Ornament.delete_ornament(_id)
