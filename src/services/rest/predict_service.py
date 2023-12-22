from src.data.enum_role import EnumRole
from src.services.rest.main_service import MainService
from http import HTTPStatus
from src.data.object import Object
from datetime import datetime
from src.services.neural_netwrok.neural_network import NeuralNetwork


class PredictService(MainService):
    def __init__(self):
        super().__init__()
        self.neural_network = NeuralNetwork()

    def get_prediction(self, email: str, password: str, image) -> tuple:
        super().check_permissions(EnumRole.USER, email, password)
        current_datetime = datetime.now()
        pred = self.neural_network.predict_external_image(self.neural_network.model, image)
        d = {'prediction': pred}
        prediction_data = {
            'prediction': pred,
            'prediction_time': current_datetime
        }
        prediction_obj = Object("prediction", email)
        prediction_obj.set_data(prediction_data)

        # insert prediction object into database
        MainService().get_db().objects.insert_one(prediction_obj.toDict())
        return d, HTTPStatus.CREATED
