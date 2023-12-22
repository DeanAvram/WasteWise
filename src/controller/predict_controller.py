from PIL import Image
from flask import Blueprint
from flask import request
from src.services.rest.predict_service import PredictService
from src.controller.main_controller import MainController
import io

predict = Blueprint('predict', __name__, url_prefix='/wastewise/predict')
predictService = PredictService()


@predict.post('')
def get_prediction():
    data = request.get_data()  # Get data
    stream = io.BytesIO(data)
    image = Image.open(stream)
    return predictService.get_prediction(MainController.get_user_email(request),
                                         MainController.get_user_password(request), image)
