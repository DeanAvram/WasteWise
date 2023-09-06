from flask import Blueprint
from flask import request

from src.services.rest.object_service import ObjectService

objects = Blueprint('objects', __name__, url_prefix='/wastewise/objects')

objectService = ObjectService()


@objects.post('')
def create_object():
    data = request.get_json()
    return objectService.create_object(data)


@objects.get('/<object_id>')
def get_object(object_id: str):
    return objectService.get_object(object_id)


@objects.put('/<object_id>')
def update_object(object_id: str):
    data = request.get_json()
    return objectService.update_object(object_id, data)
