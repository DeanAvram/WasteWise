from dataclasses import dataclass
from src.services.commands.command_interface import ICommand
from src.services.commands.commands import command_1, command_2

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
    
    def set_command(self, type: str) -> None:
        if type == "command_1":
            self.command = command_1()
            
        elif type == "command_2":
            self.command = command_2()

        elif type == "predict":
            pass
        
    def execute_command(self):
        if isinstance(self.command, ICommand):
            return self.command.execute()
