from dataclasses import dataclass
from time import time
import uuid
import json


@dataclass
class Command:
    _id: str
    type: str
    invoked_by: str
    data: dict
    created_at: int

    def __init__(self, _type: str, invoked_by: str, data: dict):
        self._id = str(uuid.uuid1())
        self.type = _type
        self.invoked_by = invoked_by
        self.data = data
        self.created_at = int(round(time() * 1000))

    def get_id(self):
        return self._id

    def get_type(self):
        return self.type

    def get_invoked_by(self):
        return self.invoked_by

    def get_data(self):
        return self.data

    def get_created_at(self):
        return self.created_at

    def set_data(self, data: dict):
        self.data = data

    def __str__(self) -> str:
        return f'{self._id} {self.type} {self.invoked_by} {self.data} {self.created_at}'

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def fromJSON(self, json_object: dict):
        self._id = json_object['_id']
        self.type = json_object['type']
        self.invoked_by = json_object['invoked_by']
        self.data = json_object['data']
        self.created_at = json_object['created_at']
        return self
