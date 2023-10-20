from enum import Enum


class EnumPeriod(Enum):
    WEEK = 0
    MONTH = 1
    YEAR = 2
    ALL = 3

    def __str__(self):
        return self.name
