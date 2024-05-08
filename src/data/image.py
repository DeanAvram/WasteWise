from dataclasses import dataclass


@dataclass
class Image:
    _id: str
    path: str
    creation_date: str
    
    def __init__(self, _id: str, path: str, creation_date: str):
        self._id = _id
        self.path = path
        self.creation_date = creation_date