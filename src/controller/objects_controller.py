from flask import Blueprint, request
from flask_cors import cross_origin
from src.services.rest.object_service import ObjectService
from src.controller.main_controller import MainController

objects = Blueprint('objects', __name__, url_prefix='/wastewise/objects')
objectService = ObjectService()


@objects.post('')
@cross_origin()
def create_object():
    """
    Create a new object.
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
              description: The name of the object.
            description:
              type: string
              description: The description of the object.
            category:
              type: string
              description: The category of the object.
            # Add more properties as needed
    responses:
      200:
        description: Object created successfully.
      400:
        description: Bad request - Invalid input.
    """
    data = request.get_json()
    return objectService.create_object(MainController.get_user_email(request),
                                       MainController.get_user_password(request), data)


@objects.get('/<object_id>')
@cross_origin()
def get_object(object_id: str):
    """
    Get object by ID.
    ---
    parameters:
      - name: object_id
        in: path
        type: string
        required: true
        description: The object identifier.
    responses:
      200:
        description: Object returned successfully.
      404:
        description: Object not found.
    """
    return objectService.get_object(MainController.get_user_email(request),
                                    MainController.get_user_password(request), object_id)


@objects.put('/<object_id>')
@cross_origin()
def update_object(object_id: str):
    """
    Update object by ID.
    ---
    parameters:
      - name: object_id
        in: path
        type: string
        required: true
        description: The object identifier.
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              description: The new name of the object.
            description:
              type: string
              description: The new description of the object.
            category:
              type: string
              description: The new category of the object.
            # Add more properties as needed
    responses:
      200:
        description: Object updated successfully.
      400:
        description: Bad request - Invalid input.
      404:
        description: Object not found.
    """
    data = request.get_json()
    return objectService.update_object(MainController.get_user_email(request),
                                       MainController.get_user_password(request), object_id, data)
