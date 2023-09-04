from PIL import Image
from flask import Blueprint
from flask import request
from src.services.predict_service import PredictService
import io

predict = Blueprint('predict', __name__, url_prefix='/wastewise/predict')
predictService = PredictService()

@predict.post('')
def get_prediction():
    data = request.get_data()  # Get data
    stream = io.BytesIO(data)
    image = Image.open(stream)
    return predictService.get_prediction(image)
