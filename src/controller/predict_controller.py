from PIL import Image
from flask import Blueprint
from flask import request
from src.services.rest.predict_service import PredictService
import io

predict = Blueprint('predict', __name__, url_prefix='/wastewise/predict')
predictService = PredictService()

@predict.post('')
def get_prediction():
    data = request.get_data()  # Get data
    stream = io.BytesIO(data)
    image = Image.open(stream)
    return predictService.get_prediction(_get_user_email(data), image)


def _get_user_email(req):
    # get query param user_id
    if req.args.get('email') is None:
        return {}, 400
    else:
        user_id = req.args.get('email')
    return user_id
