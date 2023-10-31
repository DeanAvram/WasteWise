from jsonschema import ValidationError, validate
from src.data.enum_role import EnumRole
from src.services.commands.command_invoker import CommandInvoker
from src.services.rest.main_service import MainService
from src.data.command import Command
import json
from http import HTTPStatus
from src.services.input_validation import command_schema
from src.services.commands.commands_exec import CommandNotFound


class CommandService(MainService):
    def __init__(self):
        super().__init__()
        # get the commands collection
        self.commands = super().get_db().commands
        self.users = super().get_db().users
        self.commandInvoker = None

    def create_command(self, email: str, password: str, args: dict) -> tuple:
        super().check_permissions(EnumRole.USER, email, password)
        MainService.validate_schema(args)
        command = Command(args['type'], email, args['data'])
        # command.set_data(args['data'])
        self.commands.insert_one(json.loads(command.toJSON()))

        command_invoker = CommandInvoker.instance()
        command_invoker.set_command(args['type'])

        if isinstance(command_invoker.command, CommandNotFound):
            return {"Error": "Command not found"}, HTTPStatus.BAD_REQUEST
        return command_invoker.execute_command(args, email)
