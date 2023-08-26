import json

from pymongo import MongoClient
from service.main_service import MainService
from bson import json_util


class UserService(MainService):
    def __init__(self):
        super().__init__()
        self.users = super().get_db().users

    '''def create_user(self, user):
        self.users.insert_one(user)
        return user'''

    def get_user(self, user_id):
        data = self.users.find_one({'id': user_id})
        return json.loads(json_util.dumps(data))
