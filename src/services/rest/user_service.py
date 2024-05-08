import json
from src.data.enum_role import EnumRole
from src.services.rest.main_service import MainService
from src.data.user import User
from bson import json_util
from http import HTTPStatus
from passlib.hash import pbkdf2_sha256
from src.services.input_validation import user_schema, user_schema_update


class UserService(MainService):
    def __init__(self):
        super().__init__()
        self.users = super().get_db().users

    def create_user(self, user: dict) -> tuple:
        MainService.validate_schema(user, user_schema)
        # check if mail is already exists
        if self.users.find_one({'email': user['email']}) is not None:
            return {"Error": "User with this email already exists"}, HTTPStatus.BAD_REQUEST

        # check if name is already exists
        # if self.users.find_one({'name': user['name']}) is not None:
        #     return {"Error": "User name already exists"}, HTTPStatus.BAD_REQUEST

        new_user = User(user['name'], user['email'], user['password'], user['role'])
        new_user.set_password(pbkdf2_sha256.encrypt(new_user.get_password()))
        self.users.insert_one(json.loads(new_user.toJSON()))
        return json.loads(json_util.dumps(user)), HTTPStatus.CREATED

    def get_user(self, email: str, password: str, user_email: str) -> tuple:
        """
        Get user by email

        Params:
            user_email: str -> The email of the user to get
        """
        super().check_permissions(EnumRole.USER, email, password)
        if email.lower() != user_email.lower():
            return {"Error": "User can't display data of other user!"}, HTTPStatus.FORBIDDEN
        data = self.users.find_one({'email': user_email})
        if data is None:
            return {"Error": "Can't find user with email: " + user_email}, HTTPStatus.NOT_FOUND
        return json.loads(json_util.dumps(data)), HTTPStatus.OK

    def update_user(self,  email: str, password: str, user_email_to_update: str, new_user: dict) -> tuple:
        """
        Update user by email
        
        Params:
            user_email: str -> The email of the user to update
            new_user: dict  -> The new user data
        """
        super().check_permissions(EnumRole.USER, email, password)
        MainService.validate_schema(new_user, user_schema_update)
        if new_user is None:
            return {"Error": "New user is missing"}, HTTPStatus.BAD_REQUEST
        
        user = self.users.find_one({'email': user_email_to_update})  # get user from database
        if user is None:
            return {"Error": "There is no user with email: " + user_email_to_update}, HTTPStatus.NOT_FOUND
        if new_user.get('role') is not None and new_user.get('role') != '' and new_user.get('role') != user['role']:
            return {"Error": "Can't change user role"}, HTTPStatus.BAD_REQUEST
        # user = json.loads(json_util.dumps(user))  # convert to json
        # user_obj = User(user['name'], user['email'], user['password'], user['role'])
        # user_obj .update(new_user)  # update user with new_user
        # new_user_to_json = json.loads(json_util.dumps(user_obj.toJSON()))
        if new_user.get('password') is not None and new_user.get('password') != '':
            if pbkdf2_sha256.verify(str(new_user.get('password')),user['password']):
                return {"Error": "Can't change password to the same password"}, HTTPStatus.BAD_REQUEST
            new_user['password'] = pbkdf2_sha256.encrypt(new_user['password'])
        self.users.update_one({'email': user_email_to_update}, {'$set': new_user})  # update user in database
        return '', HTTPStatus.NO_CONTENT
