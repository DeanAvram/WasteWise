import json
from service.main_service import MainService
from data.user import User
from bson import json_util


class UserService(MainService):
    def __init__(self):
        super().__init__()
        self.users = super().get_db().users

    def create_user(self, user: dict) -> tuple:
        if user['name'] is None:
            return {"Error": "Name is missing"}, 400
        if user['email'] is None:
            return {"Error": "Email is missing"}, 400
        if user['password'] is None:
            return {"Error": "Password is missing"}, 400
        if user['role'] is None:
            return {"Error": "Role is missing"}, 400
        if self.users.find_one({'email': user['email']}) is not None:
            return {"Error": "User already exists"}, 400
        new_user = User(user['name'], user['email'], user['password'], user['role'])
        self.users.insert_one(json.loads(new_user.toJSON()))
        return json.loads(json_util.dumps(user)), 201

    def get_user(self, user_email: str) -> tuple:
        data = self.users.find_one({'email': user_email})
        if data is None:
            return {"Error": "Can't find user with email: " + user_email}, 404
        return json.loads(json_util.dumps(data)), 200

    def update_user(self, user_email: str, new_user: dict) -> tuple:
        if new_user is None:
            return {"Error": "New user is missing"}, 400
        user = self.users.find_one({'email': user_email})  # get user from database
        if (new_user is None) or (new_user['role'] is None and new_user['name'] is None and new_user['email'] is None):
            return {"Error": "New user is missing"}, 400
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
