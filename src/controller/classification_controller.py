from PIL import Image
from flask import Blueprint
from flask import request
from src.services.rest.classification_service import ClassificationService
from src.controller.main_controller import MainController
import io

classification = Blueprint('classify', __name__, url_prefix='/wastewise/classify')
classificationService = ClassificationService()


@classification.post('')
def get_classification():
    data = request.get_data()  # Get data
    stream = io.BytesIO(data)
    image = Image.open(stream)
    return classificationService.get_classification(MainController.get_user_email(request),
                                                    MainController.get_user_password(request), image)
