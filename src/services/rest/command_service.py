from jsonschema import ValidationError, validate
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
        self.commandInvoker = None

    def create_command(self, args: dict) -> tuple:
        try:
            validate(instance=args, schema=command_schema)
        except ValidationError as e:
            return {
                "Error": str(e.schema["error_msg"] if "error_msg" in e.schema else e.message)}, HTTPStatus.BAD_REQUEST
        except Exception as e:
            return {"Error": str(e)}, HTTPStatus.BAD_REQUEST

        command = Command(args['type'], args['invoked_by'])
        # command.set_data(args['data'])
        self.commands.insert_one(json.loads(command.toJSON()))

        commandInvoker = CommandInvoker.instance()
        commandInvoker.set_command(args['type'])

        if isinstance(commandInvoker.command, CommandNotFound):
            return {"Error": "Command not found"}, HTTPStatus.BAD_REQUEST

        return commandInvoker.execute_command(), HTTPStatus.CREATED
