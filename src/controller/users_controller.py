from flask import Blueprint
from flask import request

from src.services.rest.user_service import UserService

users = Blueprint('users', __name__, url_prefix='/wastewise/users')

userService = UserService()


@users.post('')
def create_user():
    data = request.get_json()
    return userService.create_user(data)


@users.get('/<object_id>')
def get_user(object_id: str):
    return userService.get_user(_get_user_email(request), object_id)


@users.put('/<object_id>')
def update_user(object_id: str):
    data = request.get_json()
    return userService.update_user(_get_user_email(request), object_id, data)


def _get_user_email(req):
    # get query param user_id
    if req.args.get('email') is None:
        return {}, 400
    else:
        user_id = req.args.get('email')
    return user_id
