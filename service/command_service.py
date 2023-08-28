from service.main_service import MainService
from data.command import Command
import json

class CommandService(MainService):
    def __init__(self):
        super().__init__()
        # get the commands collection
        self.commands = super().get_db().commands

    def create_command(self, command: Command) -> dict:
        self.commands.insert_one(json.loads(command.toJSON()))
        return json.loads(command.toJSON())