from service.main_service import MainService
from data.command import Command
import json
from http import HTTPStatus
from service.input_validation import InputValidation


class CommandService(MainService):
    def __init__(self):
        super().__init__()
        # get the commands collection
        self.commands = super().get_db().commands

    def create_command(self, args: dict) -> tuple:
        InputValidation('type', 'invoked_by', request_name="POST", body=args)
        command = Command(args['type'], args['invoked_by'])
        command.set_data(args['data'])
        self.commands.insert_one(json.loads(command.toJSON()))
        return json.loads(command.toJSON()), HTTPStatus.CREATED
