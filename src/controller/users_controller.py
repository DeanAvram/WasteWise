from flask import Blueprint
from flask import request

from src.service.object_service import ObjectService
from src.service.user_service import UserService

users = Blueprint('users', __name__, url_prefix='/wastewise/users')

userService = UserService()

@users.post('')
def create_user():
    data = request.get_json()
    return userService.create_user(data)

@users.get('/<object_id>')
def get_user(object_id: str):
    return userService.get_user(object_id)

@users.put('/<object_id>')
def update_user(object_id: str):
    data = request.get_json()
    return userService.update_user(object_id, data)