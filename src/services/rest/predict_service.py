from src.data.role import Role
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
        if not super().check_permissions(Role.USER, email):
            return {"Error": "User doesn't have permissions"}, HTTPStatus.UNAUTHORIZED
        pred = Network.predict_external_image(self.model, image)
        d = {'prediction': pred}
        prediction_data = {
            'prediction': pred,
            'prediction_time': str(datetime.now())
        }

        prediction_obj = Object("prediction", email)
        prediction_obj.data = prediction_data
        print(prediction_obj.toJSON())

        # insert prediction object into database
        MainService().get_db().objects.insert_one(json.loads(prediction_obj.toJSON()))
        return d, HTTPStatus.OK
