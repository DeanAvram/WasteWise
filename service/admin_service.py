from service.main_service import MainService
from data.user import User
from data.object import Object
from data.command import Command
from bson import json_util


class AdminService(MainService):
    def __init__(self):
        super().__init__()
        self.users = super().get_db().users
        self.objects = super().get_db().objects
        self.commands = super().get_db().commands
    def delete_users(self) -> tuple:
        self.users.delete_many({})
        return '', 204

    def get_all_users(self) -> tuple:
        return list(self.users.find({})), '200'

    def delete_objects(self) -> tuple:
        self.objects.delete_many({})
        return '', 204

    def get_all_objects(self) -> tuple:
        return list(self.objects.find({})), '200'

    def delete_commands(self) -> tuple:
        self.commands.delete_many({})
        return '', 204

    def get_all_commands(self) -> tuple:
        return list(self.commands.find({})), '200'
