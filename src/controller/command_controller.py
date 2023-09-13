from flask import Blueprint
from flask import request

from src.services.rest.command_service import CommandService

commands = Blueprint('commands', __name__, url_prefix='/wastewise/commands')

userService = CommandService()

@commands.post('')
def create_command():
    data = request.get_json()
    return userService.create_command(_get_user_email(request), data)


def _get_user_email(req):
    # get query param user_id
    if req.args.get('email') is None:
        return {}, 400
    else:
        user_id = req.args.get('email')
    return user_id
