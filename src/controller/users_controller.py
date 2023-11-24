from flask import Blueprint
from flask import request
from flask_cors import cross_origin

from src.controller.main_controller import MainController
from src.services.rest.user_service import UserService

users = Blueprint('users', __name__, url_prefix='/wastewise/users')

userService = UserService()


@users.post('')
@cross_origin()
def create_user():
    data = request.get_json()
    return userService.create_user(data)


@users.get('/<user_id>')
@cross_origin()
def get_user(user_id: str):
    return userService.get_user(MainController.get_user_email(request),
                                MainController.get_user_password(request), user_id)


@users.put('/<user_id>')
@cross_origin()
def update_user(user_id: str):
    data = request.get_json()
    return userService.update_user(MainController.get_user_email(request),
                                   MainController.get_user_password(request), user_id, data)
