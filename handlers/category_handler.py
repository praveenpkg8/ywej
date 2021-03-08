import json
from flask import Blueprint, request

from status import Status
from services.category_service import CategoryService

CATEGORY = Blueprint(
    'category',
    __name__,
    url_prefix='/api/V1'
)


@CATEGORY.route('/category', methods=['POST'])
def create_category():
    params = request.get_json()
    CategoryService.add_category(params)
    return json.dumps({'message': 'category created successfully'}), Status.HTTP_201_CREATED


@CATEGORY.route('/category')
def get_all_ornament():
    ornament = CategoryService.get_all_categories()
    return json.dumps({'categories': ornament}), Status.HTTP_200_OK


@CATEGORY.route('/category', methods=['PUT'])
def update_category():
    params = request.get_json()
    CategoryService.update_category(params)
    return json.dumps(({'message': 'category updated successfully'}))


@CATEGORY.route('/category/<ID>', methods=['DELETE'])
def delete_ornament(ID):
    CategoryService.delete_category(ID)
    return json.dumps({'message': 'category deleted successfully'}), Status.HTTP_200_OK

