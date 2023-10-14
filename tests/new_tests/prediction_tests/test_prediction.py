from http import HTTPStatus
from pathlib import Path
from tests.conftest import LOGGER, equal_dicts_exclude
import os


resource_path = Path(__file__).parent / 'resources'


def test_prediction(client):
    counter: int = 1
    path = "wastewise/predict"
    arr = os.listdir("tests/test_data/images")

    for i, img in enumerate(arr):
        with open(r"tests/test_data/images/glass.jpg", 'rb') as f:
            data = f.read()
            res = client.post(
                path,
                data=data,
                headers={'Content-Type': 'application/octet-stream'}
            )

        pred = res.json['prediction']
        answer = res.status_code == HTTPStatus.OK and pred == img.split('.')[0]
        assert answer
