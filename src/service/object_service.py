from src.service.main_service import MainService
from bson import json_util
import json
from src.data.object import Object
from http import HTTPStatus

class ObjectService(MainService):
    def __init__(self):
        super().__init__()
        self.objects = super().get_db().objects
    
    def create_object(self, args: dict) -> tuple:
        if args['type'] is None:
            return {"Error": "Type is missing"}, HTTPStatus.BAD_REQUEST
        if args['created_by'] is None:
            return {"Error": "Created by is missing"}, HTTPStatus.BAD_REQUEST
        
        # create object
        object = Object(args['type'], args['created_by'])
        self.objects.insert_one(json.loads(object.toJSON()))
        return json.loads(object.toJSON()), HTTPStatus.CREATED
    
    def get_object(self, object_id: str) -> tuple:
        data = self.objects.find_one({'_id': object_id})
        if data is None:
            return {"Error": "Can't find object with id: " + object_id}, HTTPStatus.NOT_FOUND
        return json.loads(json_util.dumps(data)), HTTPStatus.OK
    
    def update_object(self, object_id: str, args: dict) -> tuple:
        # FIXME: Working, but not good, the data is been overwritten
        if args is None:
            return {"Error": "New object is missing"}, HTTPStatus.BAD_REQUEST

        object = self.objects.find_one({'_id': object_id}) # get object from database
        object = json.loads(json_util.dumps(object)) # convert to json

        if args['type'] is not None:
            return {"Error": "Can't Change Object's type"}, HTTPStatus.BAD_REQUEST
    
        if args['created_by'] is not None:
            return {"Error": "Can't Change Object's created_by"}, HTTPStatus.BAD_REQUEST

        if args['active'] is not None:
            object['active'] = args['active']

        if args['data'] is not None:
            object['data'] = args['data']

        self.objects.update_one({'_id': object_id}, {'$set': object}) # update object in database
        return '', HTTPStatus.NO_CONTENT