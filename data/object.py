import uuid
import json


class Object:

    def __init__(self, type: str, created_by: str):
        self._id = str(uuid.uuid1())
        self.type = type
        self.created_by = created_by
        self.active = True
        self.data = {}

    def get_id(self):
        return self._id
    
    def get_type(self):
        return self.type
    
    def get_created_by(self):
        return self.created_by

    def get_active(self):
        return self.active
    
    def get_data(self):
        return self.data
    
    def set_data(self, data: dict):
        self.data = data

    def set_active(self, active: bool):
        self.active = active
    
    def __str__(self) -> str:
        return f'{self._id} {self.type} {self.created_by} {self.active} {self.data}'
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
    
    def fromJSON(self, json_object: dict):
        self._id = json_object['_id']
        self.type = json_object['type']
        self.created_by = json_object['created_by']
        self.active = json_object['active']
        self.data = json_object['data']
        return self
    
    def toDict(self):
        return {
            '_id': self._id,
            'type': self.type,
            'created_by': self.created_by,
            'active': self.active,
            'data': self.data
        }
