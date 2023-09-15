from http import HTTPStatus
from pathlib import Path
from tests.conftest import LOGGER, equal_dicts_exclude
from PIL import Image


resource_path = Path(__file__).parent / 'resources'


def test_prediction(client):
    counter: int = 1
    path = "wastewise/predict"
    LOGGER.info('Starting test_prediction')
    with open(r"tests/test_data/images/glass_test.jpg", 'rb') as f:
        data = f.read()
    # im = Image.open(r"tests/test_data/images/glass_test.jpg")
    LOGGER.info('1) Got first image')
    res = client.post(
        path,
        data=data,
        headers={'Content-Type': 'application/octet-stream'}
    )
    LOGGER.info(f'3.3) Got response {res}')
    LOGGER.info(f'3.4) Got response {res.json}')
