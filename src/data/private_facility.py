
from dataclasses import dataclass


@dataclass
class PrivateFacility:
    _id: str
    type: str
    lng: float
    lat: float
    
    def __init__(self, _id: str, type: str, lng: float, lat: float):
        self._id = _id
        self.type = type
        self.lng = lng
        self.lat = lat