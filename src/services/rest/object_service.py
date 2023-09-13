from jsonschema import ValidationError, validate

from src.data.role import Role
from src.services.rest.main_service import MainService
from bson import json_util
import json
from src.data.object import Object
from http import HTTPStatus
from src.services.input_validation import object_schema, object_schema_update


class ObjectService(MainService):
    def __init__(self):
        super().__init__()
        self.objects = super().get_db().objects

    def create_object(self, mail: str, args: dict) -> tuple:

        if not super().check_permissions(Role.USER, mail):
            return {"Error": "User doesn't have permissions"}, HTTPStatus.UNAUTHORIZED

        try:
            validate(instance=args, schema=object_schema)
        except ValidationError as e:
            return {
                "Error": str(e.schema["error_msg"] if "error_msg" in e.schema else e.message)}, HTTPStatus.BAD_REQUEST
        except Exception as e:
            return {"Error": str(e)}, HTTPStatus.BAD_REQUEST

        # create object
        _object = Object(args['type'], args['created_by'])

        # check if args['data'] exists
        if 'data' in args:
            _object.data = args['data']

        # insert object into database
        self.objects.insert_one(json.loads(_object.toJSON()))

        # return object as json
        return json.loads(_object.toJSON()), HTTPStatus.CREATED

    def get_object(self, mail: str, object_id: str) -> tuple:

        if not super().check_permissions(Role.USER, mail):
            return {"Error": "User doesn't have permissions"}, HTTPStatus.UNAUTHORIZED

        data = self.objects.find_one({'_id': object_id})
        if data is None:
            return {"Error": "Can't find object with id: " + object_id}, HTTPStatus.NOT_FOUND
        return json.loads(json_util.dumps(data)), HTTPStatus.OK

    def update_object(self, mail: str, object_id: str, args: dict) -> tuple:
        # FIXME: Working, but not good, the data is been overwritten

        if not super().check_permissions(Role.USER, mail):
            return {"Error": "User doesn't have permissions"}, HTTPStatus.UNAUTHORIZED

        try:
            validate(instance=args, schema=object_schema_update)
        except ValidationError as e:
            return {
                "Error": str(e.schema["error_msg"] if "error_msg" in e.schema else e.message)}, HTTPStatus.BAD_REQUEST
        except Exception as e:
            return {"Error": str(e)}, HTTPStatus.BAD_REQUEST

        _object = self.objects.find_one({'_id': object_id})  # get object from database
        _object = json.loads(json_util.dumps(_object))  # convert to json

        _object.update(args)  # update object with args

        self.objects.update_one({'_id': object_id}, {'$set': _object})  # update object in database
        return '', HTTPStatus.NO_CONTENT
