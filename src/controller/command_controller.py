from flask import Blueprint
from flask import request

from src.services.rest.command_service import CommandService
from src.controller.main_controller import MainController

commands = Blueprint('commands', __name__, url_prefix='/wastewise/commands')

commandService = CommandService()


@commands.post('')
def create_command():
    data = request.get_json()
    return commandService.create_command(MainController.get_user_email(request),
                                         MainController.get_user_password(request), data)
