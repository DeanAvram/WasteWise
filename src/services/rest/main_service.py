import os
from pymongo import MongoClient
from flask import abort, make_response, jsonify
from http import HTTPStatus
from src.data.enum_role import EnumRole
from jsonschema import ValidationError, validate
from passlib.hash import pbkdf2_sha256
from src.services.recycle_facilities.load_from_shapefile import LoadFromShapefile


is_places_loaded = False


class MainService:
    def __init__(self):
        # self.client = MongoClient('localhost', 27017)
        username = os.environ.get('mongo_username')
        password = os.environ.get('mongo_password')
        self.client = MongoClient(f'mongodb+srv://{username}:{password}@cluster.p8ymxwu.mongodb.net/?retryWrites=true&w'
                                  '=majority')
        self.db = self.client.wastewise
        # Create a 2dsphere index on the "data.location.coordinates" field
        self.db.objects.create_index([("data.location.coordinates", "2dsphere")])

        global is_places_loaded
        if not is_places_loaded:
            load_from_shapefile = LoadFromShapefile(self.db)
            load_from_shapefile.load()
            is_places_loaded = True
        '''to_load = os.environ.get('Load_Places')
        if to_load == "True" and not is_places_loaded:
            # Delete all places from database
            self.db.objects.delete_many({'type': 'place'})
            # Load places from Excel file
            load_from_excel = LoadFromExcel(self.db)
            load_from_excel.load_places()
            is_places_loaded = True'''

    def get_db(self):
        return self.db

    def check_permissions(self, _type: EnumRole, _mail: str, _password: str):
        user = self.db.users.find_one({'email': _mail})
        if user is None:
            abort(make_response(jsonify(message="There is no user with this email"), HTTPStatus.NOT_FOUND))
        if not pbkdf2_sha256.verify(_password, user['password']):
            abort(make_response(jsonify(message="Wrong Password"), HTTPStatus.UNAUTHORIZED))
        # if self.db.users.find_one({'email': _mail, 'password': _password}) is None:
        #    abort(make_response(jsonify(message="Wrong Password"), HTTPStatus.UNAUTHORIZED))
        # check permissions
        if self.db.users.find_one({'email': _mail, 'role': _type.name}) is None:
            abort(make_response(jsonify(message="User doesn't have permissions"), HTTPStatus.FORBIDDEN))

    @staticmethod
    def validate_schema(args, schema):
        try:
            validate(instance=args, schema=schema)
        except ValidationError as e:
            if e.path.__len__() > 0:
                path = e.path.pop()
                if path == 'email':
                    abort(make_response(jsonify(message="Email is invalid"), HTTPStatus.BAD_REQUEST))
                elif path == 'password':
                    abort(
                        make_response(jsonify(message=str("Password is too short" if "short" in e.message else
                                                          "Invalid password. Make sure it contains at least one digit, "
                                                          "one uppercase letter, one lowercase letter and "
                                                          "one special character")),
                                      HTTPStatus.BAD_REQUEST))
            abort(make_response(jsonify(message=str(e.schema["error_msg"] if "error_msg" in e.schema else e.message)),
                                HTTPStatus.BAD_REQUEST))

        except Exception as e:
            abort(make_response(jsonify(message=str(e)), HTTPStatus.BAD_REQUEST))
