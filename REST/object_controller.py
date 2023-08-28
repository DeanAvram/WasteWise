from flask_restful import Resource, reqparse
from data.object import Object
from service.object_service import ObjectService

parser = reqparse.RequestParser()
objectService = ObjectService()
parser.add_argument('type')
parser.add_argument('created_by')
parser.add_argument('active')
parser.add_argument('data')

class ObjectControllerReadUpdate(Resource):
    def get(self, object_id: str):
        return objectService.get_object(object_id)

    def put(self, object_id: str):
        args = dict(parser.parse_args())

        if args is None:
            return {"Error": "Type is missing"}, 400        

        return objectService.update_object(object_id, args)

class ObjectContollerCreate(Resource):
    def post(self):
        args = parser.parse_args()
        
        if args['type'] is None:
            return {"Error": "Type is missing"}, 400
        if args['created_by'] is None:
            return {"Error": "Created by is missing"}, 400
        
        # create object
        object = Object(args['type'], args['created_by'])
        return objectService.create_object(object), 201

