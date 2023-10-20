from enum import Enum


class EnumCommands(Enum):
    DIRECT = 0,
    HISTORY = 1,
    PLACES = 2,
    ADD_PLACE = 3,
    GENERAL = 4

    def __str__(self):
        return self.name
