from http import HTTPStatus

from pymongo import MongoClient

from src.data.role import Role


class MainService:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.wastewise

    def get_db(self):
        return self.db

    def check_permissions(self, _type: Role, _mail: str) -> bool:
        if self.db.users.find_one({'email': _mail}) is None:
            raise Exception('User not found')

        # check permissions
        if self.db.users.find_one({'email': _mail, 'role': _type.name}) is None:
            return False
        return True
