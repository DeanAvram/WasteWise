from src.data.enum_role import EnumRole
from src.services.rest.main_service import MainService
from http import HTTPStatus
import torch
from src.services import Network
from src.data.object import Object
from datetime import datetime
import json


class PredictService(MainService):
    def __init__(self):
        super().__init__()
        self.device = Network.get_default_device()
        self.model = Network.ResNet()
        Network.to_device(self.model, self.device)
        self.model.load_state_dict(torch.load("model_file.pt", map_location=torch.device('cpu')))
        self.model.eval()

    def get_prediction(self, email, image) -> tuple:
        if not super().check_permissions(EnumRole.USER, email):
            return {"Error": "User doesn't have permissions"}, HTTPStatus.UNAUTHORIZED
        current_datetime = datetime.now()
        pred = Network.predict_external_image(self.model, image)
        d = {'prediction': pred}
        prediction_data = {
            'prediction': pred,
            'prediction_time': current_datetime
        }
        prediction_obj = Object("prediction", email)
        prediction_obj.set_data(prediction_data)

        # insert prediction object into database
        MainService().get_db().objects.insert_one(prediction_obj.toDict())
        return d, HTTPStatus.OK
