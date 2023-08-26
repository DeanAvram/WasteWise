from flask_restful import Resource, reqparse
import uuid
from service.user_service import UserService


parser = reqparse.RequestParser()
parser.add_argument('4444')


class UserControllerReadUpdate(Resource):
    def get(self, user_id: str) -> str:
        return UserService().get_user(user_id)

    def put(self, user_id: str) -> str:
        u = uuid.uuid1()
        d = {'key': str(u)}
        return d


class UserControllerCreate(Resource):
    def post(self):
        args = parser.parse_args()
        return args, 201

