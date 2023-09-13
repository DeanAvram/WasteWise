from flask import Blueprint
from flask import request
from src.services.rest.admin_service import AdminService


admin = Blueprint('admin', __name__, url_prefix='/wastewise/admin')

adminService = AdminService()


@admin.get('/users')
def get_all_users():
    return adminService.get_all_users(_get_page(request), _get_limit(request))


@admin.delete('/users')
def delete_users():
    return adminService.delete_users()


@admin.get('/objects')
def get_all_objects():
    return adminService.get_all_objects(_get_page(request), _get_limit(request))


@admin.delete('/objects')
def delete_objects():
    return adminService.delete_objects()


@admin.get('/commands')
def get_all_commands():
    return adminService.get_all_commands(_get_page(request), _get_limit(request))


@admin.delete('/commands')
def delete_commands():
    return adminService.delete_commands()


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
