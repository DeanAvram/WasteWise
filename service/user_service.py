import json
from service.main_service import MainService
from data.user import User
from bson import json_util


class UserService(MainService):
    def __init__(self):
        super().__init__()
        self.users = super().get_db().users

    def create_user(self, user: User) -> dict:
        self.users.insert_one(json.loads(user.toJSON()))
        return json.loads(user.toJSON())

    def get_user(self, email: str) -> dict:
        data = self.users.find_one({'email': email})
        return json.loads(json_util.dumps(data))
