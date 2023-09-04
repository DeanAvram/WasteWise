
from src.services.commands.command_interface import ICommand

class command_1(ICommand):
    def execute(self) -> dict:
        return {
            "message": "Command 1 executed"
        }
        
class command_2(ICommand):
    def execute(self) -> dict:
        return {
            "message": "Command 2 executed"
        }