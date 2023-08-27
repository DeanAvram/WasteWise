from service.main_service import MainService
from bson import json_util
import json
from data.object import Object

class ObjectService(MainService):
    def __init__(self):
        super().__init__()
        self.objects = super().get_db().objects
    
    def create_object(self, object: Object) -> dict:
        self.objects.insert_one(json.loads(object.toJSON()))
        return json.loads(object.toJSON())
    
    def get_object(self, object_id: str) -> Object:
        data = self.objects.find_one({'_id': object_id})
        return json.loads(json_util.dumps(data))
    
    def update_object(self, object_id: str, d: dict):
        # FIXME: Working, but not good, the data is been overwritten

        object = self.objects.find_one({'_id': object_id}) # get object from database
        object = json.loads(json_util.dumps(object)) # convert to json

        if d['type'] is not None:
            return {"Error": "Can't Change Object's type"}, 400
    
        if d['created_by'] is not None:
            return {"Error": "Can't Change Object's created_by"}, 400

        if d['active'] is not None:
            object['active'] = d['active']

        if d['data'] is not None:
            object['data'] = d['data']

        self.objects.update_one({'_id': object_id}, {'$set': object}) # update object in database
        return 200