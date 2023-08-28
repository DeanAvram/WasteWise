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

    def get_user(self, user_email: str) -> User:
        data = self.users.find_one({'email': user_email})
        if data is None:
            return {"Error": "Can't find user with email: " + user_email}, 404
        return json.loads(json_util.dumps(data))

    def update_user(self, user_email: str, new_user: dict):
        user = self.users.find_one({'email': user_email}) # get user from database
        if user is None:
            return {"Error": "Can't find user with email: " + user_email}, 404
        if new_user['role'] is not None:
            return {"Error": "Can't Change User's role"}, 400
        if new_user['name'] is not None:
            user['name'] = new_user['name']
        if new_user['email'] is not None:
            user['email'] = new_user['email']
        if new_user['password'] is not None:
            user['password'] = new_user['password']
        self.users.update_one({'email': user_email}, {'$set': user})  # update user in database
        return '', 204


