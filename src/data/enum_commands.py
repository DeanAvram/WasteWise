from enum import Enum


class EnumCommands(Enum):
    DIRECT = 0,
    HISTORY = 1,
    PLACES = 2,
    GENERAL = 3

    def __str__(self):
        return self.name
