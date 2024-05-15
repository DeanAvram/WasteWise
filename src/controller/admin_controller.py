from flask import Blueprint, request
from flask_cors import cross_origin
from src.services.rest.admin_service import AdminService
from src.controller.main_controller import MainController

admin = Blueprint('admin', __name__, url_prefix='/wastewise/admin')
adminService = AdminService()


@admin.get('/users')
@cross_origin()
def get_all_users():
    """
    Get all users.
    ---
    parameters:
      - in: query
        name: email
        type: string
        required: true
        description: The email of the logged in user.
      - in: query
        name: password
        type: string
        required: true
        description: The password of the logged in user.
      - in: query
        name: limit
        type: integer
        description: The number of users to retrieve per page.
      - in: query
        name: page
        type: integer
        description: The page number to retrieve.
    responses:
      200:
        description: Users retrieved successfully.
      400:
        description: Bad request - User email or password is missing.
      401:
        description: Unauthorized - Invalid credentials.
      403:
        description: Forbidden - Insufficient permissions.
      404:
        description: Not found - User with given email not found.
    """
    return adminService.get_all_users(_get_page(request), _get_limit(request),
                                      MainController.get_user_email(request), MainController.get_user_password(request))


@admin.delete('/users')
@cross_origin()
def delete_users():
    """
    Delete all users.
    ---
    parameters:
      - in: query
        name: email
        type: string
        required: true
        description: The email of the logged in user.
      - in: query
        name: password
        type: string
        required: true
        description: The password of the logged in user.
    responses:
      400:
        description: Bad request - User email or password is missing.
      204:
        description: Users deleted successfully.
      401:
        description: Unauthorized - Invalid credentials.
      403:
        description: Forbidden - Insufficient permissions.
      404:
        description: Not found - User with given email not found.
    """
    return adminService.delete_users(MainController.get_user_email(request), MainController.get_user_password(request))


@admin.get('/objects')
@cross_origin()
def get_all_objects():
    """
    Get all objects.
    ---
    parameters:
      - in: query
        name: email
        type: string
        required: true
        description: The email of the logged in user.
      - in: query
        name: password
        type: string
        required: true
        description: The password of the logged in user.
      - in: query
        name: limit
        type: integer
        description: The number of objects to retrieve per page.
      - in: query
        name: page
        type: integer
        description: The page number to retrieve.
    responses:
      200:
        description: Objects retrieved successfully.
      400:
        description: Bad request - User email or password is missing.
      401:
        description: Unauthorized - Invalid credentials.
      403:
        description: Forbidden - Insufficient permissions.
      404:
        description: Not found - User with given email not found.
    """
    return adminService.get_all_objects(_get_page(request), _get_limit(request),
                                        MainController.get_user_email(request), MainController.get_user_password(request))


@admin.delete('/objects')
def delete_objects():
    """
    Delete all objects.
    ---
    parameters:
      - in: query
        name: email
        type: string
        required: true
        description: The email of the logged in user.
      - in: query
        name: password
        type: string
        required: true
        description: The password of the logged in user.
    responses:
      400:
        description: Bad request - User email or password is missing.
      204:
        description: Objects deleted successfully.
      401:
        description: Unauthorized - Invalid credentials.
      403:
        description: Forbidden - Insufficient permissions.
      404:
        description: Not found - User with given email not found.
    """
    return adminService.delete_objects(MainController.get_user_email(request), MainController.get_user_password(request))


@admin.get('/commands')
@cross_origin()
def get_all_commands():
    """
    Get all commands.
    ---
    parameters:
      - in: query
        name: email
        type: string
        required: true
        description: The email of the logged in user.
      - in: query
        name: password
        type: string
        required: true
        description: The password of the logged in user.
      - in: query
        name: limit
        type: integer
        description: The number of commands to retrieve per page.
      - in: query
        name: page
        type: integer
        description: The page number to retrieve.
    responses:
      400:
        description: Bad request - User email or password is missing.
      200:
        description: Commands retrieved successfully.
      401:
        description: Unauthorized - Invalid credentials.
      403:
        description: Forbidden - Insufficient permissions.
      404:
        description: Not found - User with given email not found.
    """
    return adminService.get_all_commands(_get_page(request), _get_limit(request),
                                         MainController.get_user_email(request), MainController.get_user_password(request))


@admin.delete('/commands')
@cross_origin()
def delete_commands():
    """
    Delete all commands.
    ---
    parameters:
      - in: query
        name: email
        type: string
        required: true
        description: The email of the logged in user.
      - in: query
        name: password
        type: string
        required: true
        description: The password of the logged in user.
    responses:
      204:
        description: Commands deleted successfully.
      400:
        description: Bad request - User email or password is missing.
      401:
        description: Unauthorized - Invalid credentials.
      403:
        description: Forbidden - Insufficient permissions.
      404:
        description: Not found - User with given email not found.
    """
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
        page = 1
    else:
        page = int(req.args.get('page'))
    return page
