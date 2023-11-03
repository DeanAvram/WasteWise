from pymongo import MongoClient
from flask import abort, make_response, jsonify
from http import HTTPStatus
from src.data.enum_role import EnumRole
from jsonschema import ValidationError, validate


class MainService:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.wastewise
        # Create a 2dsphere index on the "data.location.coordinates" field
        self.db.objects.create_index([("data.location.coordinates", "2dsphere")])

    def get_db(self):
        return self.db

    def check_permissions(self, _type: EnumRole, _mail: str, _password: str):
        if self.db.users.find_one({'email': _mail}) is None:
            abort(make_response(jsonify(message="There is no user with this email"), HTTPStatus.BAD_REQUEST))
        if self.db.users.find_one({'email': _mail, 'password': _password}) is None:
            abort(make_response(jsonify(message="Wrong Password"), HTTPStatus.UNAUTHORIZED))
        # check permissions
        if self.db.users.find_one({'email': _mail, 'role': _type.name}) is None:
            abort(make_response(jsonify(message="User doesn't have permissions"), HTTPStatus.FORBIDDEN))

    @staticmethod
    def validate_schema(args, schema):
        try:
            validate(instance=args, schema=schema)
        except ValidationError as e:
            abort(make_response(jsonify(message=str(e.schema["error_msg"] if "error_msg" in e.schema else e.message)),
                                HTTPStatus.BAD_REQUEST))
        except Exception as e:
            abort(make_response(jsonify(message=str(e)), HTTPStatus.BAD_REQUEST))

