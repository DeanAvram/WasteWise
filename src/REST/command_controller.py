from flask_restful import Resource, reqparse
from src.data.command import Command
from src.service.command_service import CommandService

commandService = CommandService()

parser = reqparse.RequestParser()
parser.add_argument('type')
parser.add_argument('invoked_by')
parser.add_argument('data')


class CommandController(Resource):
    def post(self):
        args = parser.parse_args()
        return commandService.create_command(args)
