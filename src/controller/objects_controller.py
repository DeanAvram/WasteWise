from flask import Blueprint
from flask import request

from src.services.rest.object_service import ObjectService

objects = Blueprint('objects', __name__, url_prefix='/wastewise/objects')

objectService = ObjectService()


@objects.post('')
def create_object():
    data = request.get_json()
    return objectService.create_object(_get_user_email(request), data)


@objects.get('/<object_id>')
def get_object(object_id: str):
    return objectService.get_object(_get_user_email(request), object_id)



@objects.put('/<object_id>')
def update_object(object_id: str):
    data = request.get_json()
    return objectService.update_object(_get_user_email(request), object_id, data)


def _get_user_email(req):
    # get query param user_id
    if req.args.get('email') is None:
        return {}, 400
    else:
        user_id = req.args.get('email')
    return user_id
