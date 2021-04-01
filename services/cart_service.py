import json

from models.ornament import Ornament
from models.category import Category
from helpers.cache import Cache
from helpers.exceptions import ItemAlreadyExistInCart


class CartService:

    @classmethod
    def fetch_ornament_for_cart(cls, ornament_id):
        cart_item_byte = Cache.get(key='cart_item')
        cart_item = json.loads(cart_item_byte.decode()) if cart_item_byte else {}
        if cart_item.get(ornament_id):
            raise ItemAlreadyExistInCart(message="Item already exist in cart")

        ornament = Ornament.get_ornament_by_id(_id=ornament_id)
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
        cart_item[ornament_id] = ornament_dict
        Cache.set(key="cart_item", value=json.dumps(cart_item))
        return ornament_dict
