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
    def get(self, user_email: str) -> dict:
        return userService.get_user(user_email)

    def put(self, user_email: str) -> dict:
        u = uuid.uuid1()
        d = {'key': str(u)}
        return d


class UserControllerCreate(Resource):
    def post(self):
        args = parser.parse_args()
        if args['name'] is None:
            return {"Error": "Name is missing"}, 400
        if args['email'] is None:
            return {"Error": "Email is missing"}, 400
        if args['password'] is None:
            return {"Error": "Password is missing"}, 400
        if args['role'] is None:
            return {"Error": "Role is missing"}, 400
        if UserControllerReadUpdate().get(args['email']) is not None:
            return {"Error": "User already exists"}, 400
        user = User(args['name'], args['email'], args['password'], args['role'])
        return userService.create_user(user), 201
