from __future__ import annotations
from abc import ABC, abstractmethod
from http import HTTPStatus


class ICommand(ABC):
    
    @abstractmethod
    def execute(self, data: dict, email: str) -> None:
        pass


