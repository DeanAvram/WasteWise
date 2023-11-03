from src.data.enum_role import EnumRole
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

    def create_object(self, email: str, password: str, args: dict) -> tuple:

        super().check_permissions(EnumRole.USER, email, password)
        MainService.validate_schema(args, object_schema)

        # create object
        _object = Object(args['type'], email)

        # check if args['data'] exists
        if 'data' in args:
            _object.data = args['data']

        # insert object into database
        self.objects.insert_one(json.loads(_object.toJSON()))

        # return object as json
        return json.loads(_object.toJSON()), HTTPStatus.CREATED

    def get_object(self, email: str, password: str, object_id: str) -> tuple:

        super().check_permissions(EnumRole.USER, email, password)

        data = self.objects.find_one({'_id': object_id})
        if data is None:
            return {"Error": "Can't find object with id: " + object_id}, HTTPStatus.NOT_FOUND
        return json.loads(json_util.dumps(data)), HTTPStatus.OK

    def update_object(self, email: str, password: str, object_id: str, args: dict) -> tuple:
        # FIXME: Working, but not good, the data is been overwritten

        super().check_permissions(EnumRole.USER, email, password)
        MainService.validate_schema(args, object_schema_update)

        _object = self.objects.find_one({'_id': object_id})  # get object from database
        if _object is None:
            return {"Error": "Can't find object with id: " + object_id}, HTTPStatus.NOT_FOUND
        _object = json.loads(json_util.dumps(_object))  # convert to json

        _object.update(args)  # update object with args

        self.objects.update_one({'_id': object_id}, {'$set': _object})  # update object in database
        return '', HTTPStatus.NO_CONTENT
