from flask import Blueprint, request
from flask_cors import cross_origin
from src.controller.main_controller import MainController
from src.services.rest.user_service import UserService

users = Blueprint('users', __name__, url_prefix='/wastewise/users')
userService = UserService()


@users.post('')
@cross_origin()
def create_user():
    """
    Create a new user.
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              description: The name of the user.
            email:
              type: string
              description: The email address of the user.
            password:
              type: string
              description: The password of the user.
            role:
              type: string
              description: The role of the user.
    responses:
      201:
        description: User created successfully.
      400:
        description: Bad request - Invalid input or missing user email or password.
      401:
        description: Unauthorized - Invalid credentials.
      403:
        description: Forbidden - Insufficient permissions.
      404:
        description: Not found - User with given email not found.
    """
    data = request.get_json()
    return userService.create_user(data)


@users.get('/<user_id>')
@cross_origin()
def get_user(user_id: str):
    """
    Get user by ID.
    ---
    parameters:
      - name: user_id
        in: path
        type: string
        required: true
        description: The user identifier.
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
      200:
        description: User returned successfully.
      400:
        description: Bad request - Invalid input or missing user email or password.
      401:
        description: Unauthorized - Invalid credentials.
      403:
        description: Forbidden - Insufficient permissions.
      404:
        description: User not found or no user with given email (requester) found.
    """
    return userService.get_user(MainController.get_user_email(request),
                                MainController.get_user_password(request), user_id)


@users.put('/<user_id>')
@cross_origin()
def update_user(user_id: str):
    """
    Update user by ID.
    ---
    parameters:
      - name: user_id
        in: path
        type: string
        required: true
        description: The user identifier.
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              description: The new username of the user.
            email:
              type: string
              description: The new email address of the user.
            password:
              type: string
              description: The new password of the user.
    responses:
      204:
        description: User updated successfully.
      400:
        description: Bad request - Invalid input.
      401:
        description: Unauthorized - Invalid credentials.
      403:
        description: Forbidden - Insufficient permissions.
      404:
        description: User not found or no user with given email (requester) found.
    """
    data = request.get_json()
    return userService.update_user(MainController.get_user_email(request),
                                   MainController.get_user_password(request), user_id, data)
