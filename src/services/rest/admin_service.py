from src.data.enum_role import EnumRole
from src.services.rest.main_service import MainService
from http import HTTPStatus
import pymongo
from pymongo import ASCENDING
from pymongo import DESCENDING


def calc_to_skip(page: int, limit: int) -> int:
    return page * limit


class AdminService(MainService):
    def __init__(self):
        super().__init__()
        self.users = super().get_db().users
        self.objects = super().get_db().objects
        self.commands = super().get_db().commands

    def delete_users(self, email: str) -> tuple:
        if not super().check_permissions(EnumRole.ADMIN, email):
            return {"Error": "User doesn't have permissions"}, HTTPStatus.UNAUTHORIZED

        self.users.delete_many({})
        return '', HTTPStatus.NO_CONTENT

    def get_all_users(self, page: int, limit: int, email: str) -> tuple:
        if not super().check_permissions(EnumRole.ADMIN, email):
            return {"Error": "User doesn't have permissions"}, HTTPStatus.UNAUTHORIZED
        to_skip = calc_to_skip(page, limit)
        return list(self.users.find({}).sort("name", ASCENDING).skip(to_skip).limit(limit)), HTTPStatus.OK

    def delete_objects(self, email: str) -> tuple:
        if not super().check_permissions(EnumRole.ADMIN, email):
            return {"Error": "User doesn't have permissions"}, HTTPStatus.UNAUTHORIZED
        self.objects.delete_many({})
        return '', HTTPStatus.NO_CONTENT

    def get_all_objects(self, page: int, limit: int, email: str) -> tuple:
        if not super().check_permissions(EnumRole.ADMIN, email):
            return {"Error": "User doesn't have permissions"}, HTTPStatus.UNAUTHORIZED
        to_skip = calc_to_skip(page, limit)
        return list(self.objects.find({}).sort("type", ASCENDING).skip(to_skip).limit(limit)), HTTPStatus.OK

    def delete_commands(self, email: str) -> tuple:
        if not super().check_permissions(EnumRole.ADMIN, email):
            return {"Error": "User doesn't have permissions"}, HTTPStatus.UNAUTHORIZED
        self.commands.delete_many({})
        return '', HTTPStatus.NO_CONTENT

    def get_all_commands(self, page: int, limit: int, email: str) -> tuple:
        if not super().check_permissions(EnumRole.ADMIN, email):
            return {"Error": "User doesn't have permissions"}, HTTPStatus.UNAUTHORIZED
        to_skip = calc_to_skip(page, limit)
        return list(self.commands.find({}).sort("type", ASCENDING).skip(to_skip).limit(limit)), HTTPStatus.OK
