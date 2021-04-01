import json
from flask import Blueprint

from status import Status

from services.cart_service import CartService

from helpers.exceptions import ItemAlreadyExistInCart

CART = Blueprint(
    'cart',
    __name__,
    url_prefix='/api/V1'
)


@CART.route('/cart/ornament/<_id>')
def get_ornament_for_cart(_id):
    try:
        cart_item = CartService.fetch_ornament_for_cart(ornament_id=_id)
        return json.dumps({'ornament': cart_item}), Status.HTTP_200_OK
    except ItemAlreadyExistInCart as e:
        return json.dumps({'message': e.message}), Status.HTTP_400_BAD_REQUEST


