from flask import Blueprint
from flask import request

from src.service.admin_service import AdminService



admin = Blueprint('admin', __name__, url_prefix='/wastewise/admin')

adminService = AdminService()

@admin.get('/users')
def get_all_users():
    return adminService.get_all_users()

@admin.delete('/users')
def delete_users():
    return adminService.delete_users()

@admin.get('/objects')
def get_all_objects():
    return adminService.get_all_objects()

@admin.delete('/objects')
def delete_objects():
    return adminService.delete_objects()

@admin.get('/commands')
def get_all_commands():
    return adminService.get_all_commands()



