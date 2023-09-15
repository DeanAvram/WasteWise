from src.services.rest.main_service import MainService
from http import HTTPStatus
import torch
from src.services import Network


class PredictService(MainService):
    def __init__(self):
        super().__init__()
        self.device = Network.get_default_device()
        self.model = Network.ResNet()
        Network.to_device(self.model, self.device)
        self.model.load_state_dict(torch.load("model_file.pt", map_location=torch.device('cpu')))
        self.model.eval()

    def get_prediction(self, image) -> tuple:
        pred = Network.predict_external_image(self.model, image)
        d = {'prediction': pred}
        return d, HTTPStatus.OK
