from enum import Enum


class EnumObject(Enum):
    OTHER = -1, # USER
    IMAGE = 0, # USER
    PRIVATE_FACILITY = 1, # USER
    PUBLIC_FACILITY = 2, # ADMIN

    def __str__(self):
        return self.name

