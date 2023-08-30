from flask_restful import Resource, reqparse
import uuid
from service.user_service import UserService
from data.user import User


parser = reqparse.RequestParser()
userService = UserService()
parser.add_argument('name')
parser.add_argument('email')
parser.add_argument('password')
parser.add_argument('role')


class UserControllerReadUpdate(Resource):
    def get(self, user_email: str):
        return userService.get_user(user_email)

    def put(self, user_email: str):
        args = dict(parser.parse_args())
        return userService.update_user(user_email, args)


class UserControllerCreate(Resource):
    def post(self):
        args = dict(parser.parse_args())
        return userService.create_user(args)
