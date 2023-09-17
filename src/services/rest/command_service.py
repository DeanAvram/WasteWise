from jsonschema import ValidationError, validate

from src.data.role import Role
from src.services.commands.command_invoker import CommandInvoker
from src.services.rest.main_service import MainService
from src.data.command import Command
import json
from http import HTTPStatus
from src.services.input_validation import command_schema
from src.services.commands.commands import CommandNotFound


class CommandService(MainService):
    def __init__(self):
        super().__init__()
        # get the commands collection
        self.commands = super().get_db().commands
        self.users = super().get_db().users
        self.commandInvoker = None

    def create_command(self, email: str, args: dict) -> tuple:

        if not super().check_permissions(Role.USER, email):
            return {"Error": "User doesn't have permissions"}, HTTPStatus.UNAUTHORIZED

        try:
            validate(instance=args, schema=command_schema)
        except ValidationError as e:
            return {
                "Error": str(e.schema["error_msg"] if "error_msg" in e.schema else e.message)}, HTTPStatus.BAD_REQUEST
        except Exception as e:
            return {"Error": str(e)}, HTTPStatus.BAD_REQUEST

        command = Command(args['type'], email, args['data'])
        # command.set_data(args['data'])
        self.commands.insert_one(json.loads(command.toJSON()))

        commandInvoker = CommandInvoker.instance()
        commandInvoker.set_command(args['type'])

        if isinstance(commandInvoker.command, CommandNotFound):
            return {"Error": "Command not found"}, HTTPStatus.BAD_REQUEST

        return commandInvoker.execute_command(command.data)
