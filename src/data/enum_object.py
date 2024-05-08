from enum import Enum


class EnumObject(Enum):
    OTHER = -1,
    IMAGE = 0,
    PRIVATE_FACILITY = 1,
    PUBLIC_FACILITY = 2,

    def __str__(self):
        return self.name

