from http import HTTPStatus
from pathlib import Path
from tests.conftest import LOGGER, equal_dicts_exclude
import os


resource_path = Path(__file__).parent / 'resources'


def test_prediction(client):
    counter: int = 1
    path = "wastewise/predict"
    LOGGER.info('Starting test_prediction')
    arr = os.listdir("tests/test_data/images")
    LOGGER.info('1) Got images folder')
    LOGGER.info('2) Starting loop\n')
    for i, img in enumerate(arr):
        LOGGER.info("2.1) Test img " + str(i+1) + ": " + img)
        with open(r"tests/test_data/images/glass.jpg", 'rb') as f:
            data = f.read()
            res = client.post(
                path,
                data=data,
                headers={'Content-Type': 'application/octet-stream'}
            )
        LOGGER.info(f'2.2) Got response {res}')
        LOGGER.info(f'2.3) Got response {res.json}')
        pred = res.json['prediction']
        answer = res.status_code == HTTPStatus.OK and pred == img.split('.')[0]
        LOGGER.info(f'2.4) comparison is {answer}')
        assert answer
        LOGGER.info('3) Done test_prediction\n\n')
