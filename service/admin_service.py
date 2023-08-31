from service.main_service import MainService
from http import HTTPStatus


class AdminService(MainService):
    def __init__(self):
        super().__init__()
        self.users = super().get_db().users
        self.objects = super().get_db().objects
        self.commands = super().get_db().commands

    def delete_users(self) -> tuple:
        self.users.delete_many({})
        return '', HTTPStatus.NO_CONTENT

    def get_all_users(self) -> tuple:
        return list(self.users.find({})), HTTPStatus.OK

    def delete_objects(self) -> tuple:
        self.objects.delete_many({})
        return '', HTTPStatus.NO_CONTENT

    def get_all_objects(self) -> tuple:
        return list(self.objects.find({})), HTTPStatus.OK

    def delete_commands(self) -> tuple:
        self.commands.delete_many({})
        return '', HTTPStatus.NO_CONTENT

    def get_all_commands(self) -> tuple:
        return list(self.commands.find({})), HTTPStatus.OK
