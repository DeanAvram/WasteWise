from src.services.commands.command_invoker import CommandInvoker
from src.services.main_service import MainService
from src.data.command import Command
import json
from http import HTTPStatus


class CommandService(MainService):
    def __init__(self):
        super().__init__()
        # get the commands collection
        self.commands = super().get_db().commands
        self.commandInvoker = None

    def create_command(self, args: dict) -> tuple:
        if args['type'] is None:
            return {"Error": "Type is missing"}, HTTPStatus.BAD_REQUEST
        if args['invoked_by'] is None:
            return {"Error": "Invoked by is missing"}, HTTPStatus.BAD_REQUEST
        command = Command(args['type'], args['invoked_by'])
        # command.set_data(args['data'])
        self.commands.insert_one(json.loads(command.toJSON()))
        
        commandInvoker = CommandInvoker.instance()
        commandInvoker.set_command(args['type'])
        
        return commandInvoker.execute_command(), HTTPStatus.CREATED