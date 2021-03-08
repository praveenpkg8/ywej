import json
from flask import Blueprint, request

from status import Status
from services.ornament_service import OrnamentService

ORNAMENT = Blueprint(
    'ornament',
    __name__,
    url_prefix='/api/V1'
)


@ORNAMENT.route('/ornament', methods=['POST'])
def add_ornament():
    params = request.get_json()
    OrnamentService.create_ornament(params)
    return json.dumps({'message': 'ornament created successfully'}), Status.HTTP_200_OK


@ORNAMENT.route('/ornaments')
def get_all_ornament():
    ornament = OrnamentService.get_all_ornaments()
    return json.dumps({'ornaments': ornament}), Status.HTTP_200_OK


@ORNAMENT.route('/ornament', methods=['PUT'])
def update_ornament():
    params = request.get_json()
    OrnamentService.update_ornaments(params)
    return json.dumps(({'message': 'ornament updated successfully'}))


@ORNAMENT.route('/ornament/<ID>', methods=['DELETE'])
def delete_ornament(ID):
    OrnamentService.delete_ornament(ID)
    return json.dumps({'message': 'ornament deleted successfully'}), Status.HTTP_200_OK
