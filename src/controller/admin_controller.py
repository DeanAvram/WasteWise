from flask import Blueprint
from flask import request
from flask_cors import cross_origin

from src.services.rest.admin_service import AdminService
from src.controller.main_controller import MainController


admin = Blueprint('admin', __name__, url_prefix='/wastewise/admin')

adminService = AdminService()


@admin.get('/users')
@cross_origin()
def get_all_users():
    return adminService.get_all_users(_get_page(request), _get_limit(request),
                                      MainController.get_user_email(request), MainController.get_user_password(request))


@admin.delete('/users')
@cross_origin()
def delete_users():
    return adminService.delete_users(MainController.get_user_email(request), MainController.get_user_password(request))


@admin.get('/objects')
@cross_origin()
def get_all_objects():
    return adminService.get_all_objects(_get_page(request), _get_limit(request),
                                        MainController.get_user_email(request), MainController.get_user_password(request))


@admin.delete('/objects')
def delete_objects():
    return adminService.delete_objects(MainController.get_user_email(request), MainController.get_user_password(request))


@admin.get('/commands')
@cross_origin()
def get_all_commands():
    return adminService.get_all_commands(_get_page(request), _get_limit(request), MainController.get_user_email(request), MainController.get_user_password(request))


@admin.delete('/commands')
@cross_origin()
def delete_commands():
    return adminService.delete_commands(MainController.get_user_email(request), MainController.get_user_password(request))


def _get_limit(req):
    # get query param limit, if not present, default to 10
    if req.args.get('limit') is None:
        limit = 10
    else:
        limit = int(req.args.get('limit'))
    return limit


def _get_page(req):
    # get query param page, if not present, default to 1
    if req.args.get('page') is None:
        page = 0
    else:
        page = int(req.args.get('page'))
    return page
