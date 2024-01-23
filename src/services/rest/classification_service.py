from src.data.enum_role import EnumRole
from src.services.rest.main_service import MainService
from http import HTTPStatus
from src.data.object import Object
from datetime import datetime
from src.services.neural_netwrok.neural_network import NeuralNetwork


class ClassificationService(MainService):
    def __init__(self):
        super().__init__()
        self.neural_network = NeuralNetwork()

    def get_classification(self, email: str, password: str, image) -> tuple:
        super().check_permissions(EnumRole.USER, email, password)
        current_datetime = datetime.now()
        classification = self.neural_network.classify_external_image(self.neural_network.model, image)
        d = {'classification': classification}
        classification_data = {
            'classification': classification,
            'classification_time': current_datetime
        }
        classification_obj = Object("classification", email)
        classification_obj.set_data(classification_data)

        # insert classification object into database
        MainService().get_db().objects.insert_one(classification_obj.toDict())
        return d, HTTPStatus.CREATED
