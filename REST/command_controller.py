from flask_restful import Resource, reqparse
from data.command import Command
from service.command_service import CommandService

commandService = CommandService()

parser = reqparse.RequestParser()
parser.add_argument('type')
parser.add_argument('invoked_by')
parser.add_argument('data')


class CommandController(Resource):
    def post(self):
        args = parser.parse_args()
        if args['type'] is None:
            return {"Error": "Type is missing"}, 400
        if args['invoked_by'] is None:
            return {"Error": "Invoked by is missing"}, 400
        command = Command(args['type'], args['invoked_by'])
        command.set_data(args['data'])
        return commandService.create_command(command), 201
