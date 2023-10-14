from enum import Enum


class Commands(Enum):
    DIRECT = 0,
    HISTORY = 1,
    PLACES = 2,
    ADD_PLACE = 3


class Period(Enum):
    WEEK = 0
    MONTH = 1
    YEAR = 2
    ALL = 3
