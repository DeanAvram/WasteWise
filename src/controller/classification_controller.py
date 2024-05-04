from PIL import Image
from flask import Blueprint, request
from src.services.rest.classification_service import ClassificationService
from src.controller.main_controller import MainController
import io

classification = Blueprint('classify', __name__, url_prefix='/wastewise/classify')
classificationService = ClassificationService()


@classification.post('')
def get_classification():
    """
    Get classification for an image.
    ---
    consumes:
      - application/octet-stream
    parameters:
      - in: query
        name: email
        type: string
        description: The email of the logged in user.
      - in: query
        name: password
        type: string
        description: The password of the logged in user.
      - in: body
        name: image
        description: The image file to be classified.
        required: true
        schema:
          type: string
          format: binary
    responses:
      201:
        description: Classification retrieved successfully.
      400:
        description: Bad request - User email or password is missing.
      401:
        description: Unauthorized - Invalid credentials.
      403:
        description: Forbidden - Insufficient permissions.
      404:
        description: Not found - User with given email not found.
      415:
        description: Unsupported Media Type - Only image files are supported.
    """
    data = request.get_data()  # Get data
    stream = io.BytesIO(data)
    image = Image.open(stream)
    return classificationService.get_classification(MainController.get_user_email(request),
                                                    MainController.get_user_password(request), image)
