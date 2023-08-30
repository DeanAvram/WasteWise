from flask_restful import Resource
from service.admin_service import AdminService


adminService = AdminService()


class AdminControllerUsers(Resource):
    def delete(self) -> tuple:
        return adminService.delete_users()

    def get(self) -> tuple:
        return adminService.get_all_users()


class AdminControllerObjects(Resource):
    def delete(self) -> tuple:
        return adminService.delete_objects()

    def get(self) -> tuple:
        return adminService.get_all_objects()


class AdminControllerCommands(Resource):
    def delete(self) -> tuple:
        return adminService.delete_commands()

    def get(self) -> tuple:
        return adminService.get_all_commands()
