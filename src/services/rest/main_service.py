from pymongo import MongoClient
from flask import abort, make_response, jsonify

from src.data.role import Role


class MainService:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.wastewise
        # Create a 2dsphere index on the "data.location.coordinates" field
        self.db.objects.create_index([("data.location.coordinates", "2dsphere")])

    def get_db(self):
        return self.db

    def check_permissions(self, _type: Role, _mail: str) -> bool:
        if self.db.users.find_one({'email': _mail}) is None:
            abort(make_response(jsonify(message="email is missing"), 400))

        # check permissions
        if self.db.users.find_one({'email': _mail, 'role': _type.name}) is None:
            return False
        return True
