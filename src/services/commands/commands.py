from src.services.commands.command_interface import ICommand
from enum import Enum


class Commands(Enum):
    COMMAND_1 = 0,
    COMMAND_2 = 1,
    PREDICT = 2


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
