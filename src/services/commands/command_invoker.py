from dataclasses import dataclass
from src.services.commands.command_interface import ICommand
from src.services.commands.commands import Direct, History, Places, AddPlace, CommandNotFound


class CommandInvoker:
    _instance = None

    def __init__(self) -> None:
        raise RuntimeError("Call instance() instead")

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance

    command = None

    def set_command(self, _type: str) -> None:
        if _type == "DIRECT":
            self.command = Direct()
        elif _type == "HISTORY":
            self.command = History()
        elif _type == "PLACES":
            self.command = Places()
        elif _type == "ADD_PLACE":
            self.command = AddPlace()
        else:
            self.command = CommandNotFound()

    def execute_command(self, data: dict):
        if isinstance(self.command, ICommand):
            return self.command.execute(data)
