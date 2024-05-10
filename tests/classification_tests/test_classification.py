from http import HTTPStatus
from pathlib import Path

import os
import io
from tests.conftest import LOGGER, create_user


resource_path = Path(__file__).parent / 'resources'


def test_classification_1(client):
    LOGGER.info('Test Classification 1')
    LOGGER.info('glass')
    
    LOGGER.info('Creating User')
    user: dict = create_user("User", "user@gmail.com", "Testing193!", "USER")
    LOGGER.info("User created")
    
    LOGGER.info("Add Classifications")
    
    image = open('tests/test_data/images/glass.jpg', 'rb')
    assert image is not None
    LOGGER.info("Image opened")
    
    path = f'/wastewise/classify?email={user["email"]}&password={user["password"]}'
    LOGGER.info(f"Path: {path}")    
    
    LOGGER.info("Sending request")
    response = client.post(
            path,
            data=image,
            content_type='image/jpeg'
        )
    LOGGER.info(f'Response: {response.json}')
    LOGGER.info(f'Status code: {response.status_code}')
    assert response.status_code == HTTPStatus.CREATED
    LOGGER.info("Classification is glass") if response.json['classification'] == 'glass' else LOGGER.error("Classification is not glass")
    LOGGER.info('Test passed\n')

def test_classification_2(client):
    LOGGER.info('Test Classification 2')
    LOGGER.info('plastic')
    
    LOGGER.info('Creating User')
    user: dict = create_user("User", "user@gmail.com", "Testing193!", "USER")
    LOGGER.info("User created")
    
    LOGGER.info("Add Classifications")
    
    image = open('tests/test_data/images/plastic.jpeg', 'rb')
    assert image is not None
    LOGGER.info("Image opened")
    
    path = f'/wastewise/classify?email={user["email"]}&password={user["password"]}'
    LOGGER.info(f"Path: {path}")    
    
    LOGGER.info("Sending request")
    response = client.post(
            path,
            data=image,
            content_type='image/jpeg'
        )
    LOGGER.info(f'Response: {response.json}')
    LOGGER.info(f'Status code: {response.status_code}')
    assert response.status_code == HTTPStatus.CREATED
    LOGGER.info("Classification is plastic") if response.json['classification'] == 'plastic' else LOGGER.error("Classification is not plasric")
    LOGGER.info('Test passed\n')