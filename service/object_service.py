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
    
    def get_object(self, object_id: str) -> dict:
        data = self.objects.find_one({'_id': object_id})
        return json.loads(json_util.dumps(data))
    
    def update_object(self, object_id: str, object: Object) -> dict:
        # FIXME: This is not working - it is not updating the object in the database
        self.objects.update_one({'_id': object_id}, {'$set': json.loads(object.toJSON())})
        return json.loads(object.toJSON())
    
    