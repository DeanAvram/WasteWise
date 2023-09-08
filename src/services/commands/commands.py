from src.services.commands.command_interface import ICommand


class Command1(ICommand):
    def execute(self) -> dict:
        return {
            "message": "Command 1 executed"
        }


class Command2(ICommand):
    def execute(self) -> dict:
        return {
            "message": "Command 2 executed"
        }


class Predict(ICommand):
    def execute(self, data: dict) -> dict:
        return {
            "message": "Predict executed"
        }


class CommandNotFound(ICommand):
    def execute(self) -> dict:
        return {
            "message": "Command not found"
        }
