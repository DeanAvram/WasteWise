from flask import Blueprint, request
from flask_cors import cross_origin
from src.services.rest.command_service import CommandService
from src.controller.main_controller import MainController

commands = Blueprint('commands', __name__, url_prefix='/wastewise/commands')
commandService = CommandService()


@commands.post('')
@cross_origin()
def create_command():
    """
    Create a new command.
    ---
    parameters:
      - in: query
        name: email
        type: string
        description: The email of the logged in user.
      - in: query
        name: password
        type: string
        description: The password of the logged in user.
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            type:
              type: string
              description: The name of the command.
            data:
              type: object
              description: The data of the command.
    responses:
      201:
        description: Command created successfully.
      400:
        description: Bad request - Invalid command name or data.
      401:
        description: Unauthorized - Invalid credentials.
      403:
        description: Forbidden - Insufficient permissions.
      404:
        description: Not found - User with given email not found.
    """
    data = request.get_json()
    return commandService.create_command(MainController.get_user_email(request),
                                         MainController.get_user_password(request), data)
