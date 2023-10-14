from enum import Enum


class Role(Enum):
    USER = 0,
    ADMIN = 1

    def __str__(self):
        return self.name
