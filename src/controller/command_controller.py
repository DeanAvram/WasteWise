from flask import Blueprint
from flask import request

from src.service.command_service import CommandService

commands = Blueprint('commands', __name__, url_prefix='/wastewise/commands')

userService = CommandService()

@commands.post('')
def create_command():
    data = request.get_json()
    return userService.create_command(data)
