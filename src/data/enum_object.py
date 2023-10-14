from enum import Enum


class EnumObject(Enum):
    OTHER = -1,
    IMAGE = 0

    def __str__(self):
        return self.name

